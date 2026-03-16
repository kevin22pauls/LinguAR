from __future__ import annotations

"""
Build the phoneme pool for retrieval-based MDD (Tu et al. 2025).

Two alignment modes:
  --mode mfa   : MFA forced alignment (requires conda env, most accurate)
  --mode ctc   : HuBERT CTC decoding (no MFA needed, good enough for pool)

MFA mode uses BATCH alignment — all files aligned in one MFA call, avoiding
the ~2 min conda startup overhead per file.

Supported datasets:
  - CMU ARCTIC  : native speaker recordings (BDL, SLT, CLB, RMS, etc.)
  - L2-ARCTIC   : uses annotation/ dir for transcripts
  - Any folder  : WAV files + .txt or .lab transcript files

Usage:
  python scripts/build_phoneme_pool.py --data-dir /path/to/audio --mode ctc
  python scripts/build_phoneme_pool.py --data-dir /path/to/arctic --mode mfa

Output (in backend/data/phoneme_pool/):
  embeddings.npy  — (~N, 1024) float32, L2-normalized
  labels.npy      — (~N,) string ARPAbet labels
  faiss_index.bin — FAISS IndexFlatIP for cosine similarity search
"""

import argparse
import logging
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)


# ──────────────────────────────────────────────────────────────────────
# Dataset discovery
# ──────────────────────────────────────────────────────────────────────

def find_audio_transcript_pairs(
    data_dir: Path, max_files: int = 500,
) -> list[tuple[Path, str]]:
    """
    Walk data_dir and return (wav_path, transcript_text) pairs.

    Handles multiple layouts:
      - CMU ARCTIC:  speaker/wav/*.wav + speaker/etc/txt.done.data
      - L2-ARCTIC:   speaker/wav/*.wav + speaker/annotation/*.TextGrid
      - Flat:        *.wav + *.txt (same stem)
    """
    pairs = []

    # Try CMU ARCTIC layout: look for etc/txt.done.data prompts file
    prompts_files = list(data_dir.rglob("txt.done.data"))
    if prompts_files:
        return _collect_cmu_arctic(data_dir, prompts_files, max_files)

    # Try directory-per-speaker layout with txt/ or transcript/
    for speaker_dir in sorted(data_dir.iterdir()):
        if not speaker_dir.is_dir():
            continue
        wav_dir = speaker_dir / "wav"
        if not wav_dir.exists():
            wav_dir = speaker_dir
        txt_dir = speaker_dir / "txt"
        if not txt_dir.exists():
            txt_dir = speaker_dir / "transcript"
        if not txt_dir.exists():
            txt_dir = wav_dir  # .txt next to .wav

        for wav in sorted(wav_dir.glob("*.wav")):
            txt = _find_transcript(wav, txt_dir)
            if txt:
                pairs.append((wav, txt))
            if len(pairs) >= max_files:
                return pairs

    # Flat layout
    if not pairs:
        for wav in sorted(data_dir.rglob("*.wav")):
            txt = _find_transcript(wav, wav.parent)
            if txt:
                pairs.append((wav, txt))
            if len(pairs) >= max_files:
                return pairs

    return pairs


def _collect_cmu_arctic(
    root: Path, prompts_files: list[Path], max_files: int,
) -> list[tuple[Path, str]]:
    """Parse CMU ARCTIC 'txt.done.data' prompt files."""
    pairs = []
    for pf in prompts_files:
        speaker_root = pf.parent.parent  # etc/ -> speaker_dir
        wav_dir = speaker_root / "wav"
        if not wav_dir.exists():
            continue
        for line in pf.read_text(
            encoding="utf-8", errors="ignore",
        ).splitlines():
            # Format: ( arctic_a0001 "Author of the ..." )
            line = line.strip()
            if not line.startswith("("):
                continue
            parts = line.split('"')
            if len(parts) < 2:
                continue
            utt_id = parts[0].strip("( ").strip()
            text = parts[1].strip()
            wav = wav_dir / f"{utt_id}.wav"
            if wav.exists():
                pairs.append((wav, text))
            if len(pairs) >= max_files:
                return pairs
    return pairs


def _find_transcript(wav_path: Path, txt_dir: Path) -> str | None:
    """Find transcript text for a wav file."""
    stem = wav_path.stem
    for ext in (".txt", ".lab"):
        txt_path = txt_dir / (stem + ext)
        if txt_path.exists():
            text = txt_path.read_text(
                encoding="utf-8", errors="ignore",
            ).strip()
            if text:
                return text
    return None


# ──────────────────────────────────────────────────────────────────────
# CTC-based phone labeling (no MFA needed)
# ──────────────────────────────────────────────────────────────────────

# Simple char → ARPAbet mapping for HuBERT CTC character vocab
_CHAR_TO_ARPABET = {
    "A": "AH", "B": "B", "C": "K", "D": "D", "E": "EH",
    "F": "F", "G": "G", "H": "HH", "I": "IH", "J": "JH",
    "K": "K", "L": "L", "M": "M", "N": "N", "O": "AA",
    "P": "P", "Q": "K", "R": "R", "S": "S", "T": "T",
    "U": "AH", "V": "V", "W": "W", "X": "K", "Y": "Y",
    "Z": "Z",
}


def ctc_decode_phones(audio, ctc_model, processor):
    """
    Run HuBERT CTC → frame-level phone predictions.
    Returns: list of (arpabet_label, frame_index).
    """
    import torch

    device = next(ctc_model.parameters()).device
    inputs = processor(
        audio, sampling_rate=16000,
        return_tensors="pt", padding=True,
    )
    input_values = inputs.input_values.to(device)

    with torch.no_grad():
        logits = ctc_model(input_values).logits

    pred_ids = logits.argmax(dim=-1).squeeze(0).cpu().numpy()
    vocab = processor.tokenizer.get_vocab()
    id_to_token = {v: k for k, v in vocab.items()}

    results = []
    prev_id = -1
    for frame_idx, token_id in enumerate(pred_ids):
        if token_id == prev_id:
            continue  # CTC repeat
        prev_id = token_id
        token = id_to_token.get(token_id, "")
        if not token or token in ("<pad>", "<s>", "</s>", "<unk>", "|"):
            continue
        arpabet = _CHAR_TO_ARPABET.get(token.upper())
        if arpabet:
            results.append((arpabet, frame_idx))

    return results


# ──────────────────────────────────────────────────────────────────────
# Batch MFA alignment (all files at once)
# ──────────────────────────────────────────────────────────────────────

def _find_conda() -> str:
    """Find the conda executable on the system."""
    candidates = [
        "conda",
        "D:/Miniconda3/_conda.exe",
        "D:/Miniconda3/condabin/conda.bat",
        Path.home() / "miniconda3" / "_conda.exe",
        Path.home() / "miniconda3" / "condabin" / "conda",
        Path.home() / "anaconda3" / "condabin" / "conda",
    ]
    for c in candidates:
        p = Path(c)
        if p.exists():
            return str(p)
    return "conda"


def batch_mfa_align(
    pairs: list[tuple[Path, str]],
    timeout_sec: int = 3600,
) -> dict[str, list[tuple[str, float, float]]]:
    """
    Run MFA alignment on ALL files in one batch call.

    1. Copy/symlink WAV files + write .lab transcript files into one corpus dir
    2. Run single `mfa align` on the entire corpus
    3. Parse all output TextGrid files

    Returns: {utterance_stem: [(phone, start, end), ...]} or empty dict on failure.
    """
    from backend.services.mfa_alignment import parse_textgrid

    tmpdir = tempfile.mkdtemp(prefix="mfa_batch_")
    corpus_dir = Path(tmpdir) / "corpus"
    output_dir = Path(tmpdir) / "output"
    corpus_dir.mkdir()
    output_dir.mkdir()

    stem_map = {}  # stem -> original wav_path (for tracking)

    try:
        # Step 1: Prepare corpus — copy WAV + write .lab files
        logger.info("Preparing MFA corpus with %d files...", len(pairs))
        for i, (wav_path, transcript) in enumerate(pairs):
            # Use unique stem to avoid collisions across speakers
            stem = f"utt_{i:05d}"
            stem_map[stem] = wav_path

            # Copy WAV file
            dst_wav = corpus_dir / f"{stem}.wav"
            shutil.copy2(str(wav_path), str(dst_wav))

            # Write transcript as .lab
            dst_lab = corpus_dir / f"{stem}.lab"
            dst_lab.write_text(transcript.strip(), encoding="utf-8")

        logger.info("Corpus prepared: %d files in %s", len(pairs), corpus_dir)

        # Step 2: Run MFA align (single batch call)
        conda_exe = _find_conda()
        cmd = [
            conda_exe, "run", "-n", "mfa_env",
            "mfa", "align",
            str(corpus_dir),
            "english_us_arpa",     # dictionary
            "english_us_arpa",     # acoustic model
            str(output_dir),
            "--single_speaker",
            "--clean",
            "--overwrite",
            "--num_jobs", "2",
        ]

        logger.info("Running batch MFA: %s", " ".join(cmd))
        logger.info("This may take 15-30 minutes for %d files. Timeout: %ds", len(pairs), timeout_sec)

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout_sec,
        )

        if result.returncode != 0:
            logger.error("MFA batch failed (exit %d):\nSTDOUT: %s\nSTDERR: %s",
                         result.returncode, result.stdout[:1000], result.stderr[:1000])
            return {}

        logger.info("MFA batch alignment complete.")

        # Step 3: Parse all output TextGrid files
        textgrid_files = list(output_dir.rglob("*.TextGrid"))
        logger.info("Found %d TextGrid files in output.", len(textgrid_files))

        alignments = {}
        for tg_path in textgrid_files:
            stem = tg_path.stem
            try:
                mfa_result = parse_textgrid(str(tg_path))
                phones = []
                for p in mfa_result.phones:
                    if p.phone and p.phone not in ("sil", "sp", "spn", ""):
                        label = p.phone.rstrip("012").upper()
                        phones.append((label, p.start, p.end))
                if phones:
                    alignments[stem] = phones
            except Exception as e:
                logger.warning("Error parsing TextGrid %s: %s", tg_path.name, e)

        logger.info("Successfully parsed %d/%d alignments.", len(alignments), len(textgrid_files))
        return alignments

    except subprocess.TimeoutExpired:
        logger.error("MFA batch alignment timed out after %ds.", timeout_sec)
        return {}
    except FileNotFoundError:
        logger.error("conda/mfa not found. Is mfa_env set up?")
        return {}
    except Exception as e:
        logger.error("MFA batch alignment error: %s", e)
        return {}
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


# ──────────────────────────────────────────────────────────────────────
# Main pool builder
# ──────────────────────────────────────────────────────────────────────

def build_pool(
    data_dir: str,
    output_dir: str,
    mode: str = "ctc",
    max_files: int = 500,
    layer: int = -1,
    mfa_timeout: int = 3600,
):
    import torch
    import soundfile as sf
    import torchaudio
    from backend.models.hubert_model import extract_embeddings

    data_path = Path(data_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    if not data_path.exists():
        logger.error("Data directory not found: %s", data_path)
        logger.info(
            "Download CMU ARCTIC: http://festvox.org/cmu_arctic/\n"
            "Or L2-ARCTIC: https://psi.engr.tamu.edu/l2-arctic-corpus/"
        )
        return

    # 1. Discover audio files
    pairs = find_audio_transcript_pairs(data_path, max_files)
    logger.info("Found %d audio files to process.", len(pairs))

    if not pairs:
        logger.error("No audio-transcript pairs found in %s", data_path)
        return

    # 2. Run batch MFA alignment if needed (BEFORE loading HuBERT to save memory)
    mfa_alignments = {}
    if mode == "mfa":
        logger.info("=" * 60)
        logger.info("STEP 1/3: Running batch MFA alignment on %d files...", len(pairs))
        logger.info("=" * 60)
        mfa_alignments = batch_mfa_align(pairs, timeout_sec=mfa_timeout)
        if not mfa_alignments:
            logger.error("MFA alignment produced no results. Aborting.")
            return
        logger.info("MFA done: %d/%d files aligned successfully.", len(mfa_alignments), len(pairs))

    # 3. Load CTC model if needed
    ctc_model = None
    ctc_processor = None
    if mode == "ctc":
        from transformers import HubertForCTC, Wav2Vec2Processor
        from backend.config import settings
        device = "cuda:0" if torch.cuda.is_available() else "cpu"
        logger.info("Loading HuBERT CTC for phone labeling on %s...", device)
        ctc_processor = Wav2Vec2Processor.from_pretrained(
            settings.hubert_model,
        )
        ctc_model = (
            HubertForCTC.from_pretrained(settings.hubert_model)
            .to(device).eval()
        )

    # 4. Extract HuBERT embeddings and collect phone-level samples
    logger.info("=" * 60)
    logger.info("STEP 2/3: Extracting HuBERT embeddings...")
    logger.info("=" * 60)

    all_embeddings = []
    all_labels = []
    processed = 0
    skipped = 0

    for i, (wav_path, transcript) in enumerate(pairs):
        stem = f"utt_{i:05d}"  # matches batch_mfa_align naming

        try:
            data, sr = sf.read(str(wav_path), dtype="float32")
            if data.ndim > 1:
                data = data.mean(axis=1)
            if sr != 16000:
                resampler = torchaudio.transforms.Resample(sr, 16000)
                data = resampler(
                    torch.from_numpy(data).unsqueeze(0)
                ).squeeze().numpy()
            audio = data

            if len(audio) < 1600:  # < 0.1s
                skipped += 1
                continue

            # Extract HuBERT embeddings
            embeddings = extract_embeddings(audio, layer=layer)

            if mode == "mfa":
                if stem not in mfa_alignments:
                    skipped += 1
                    continue

                phone_info = mfa_alignments[stem]
                fps = embeddings.shape[0] / (len(audio) / 16000)
                for label, start, end in phone_info:
                    mid_time = (start + end) / 2
                    fi = int(mid_time * fps)
                    if 0 <= fi < embeddings.shape[0]:
                        all_embeddings.append(embeddings[fi])
                        all_labels.append(label)

            elif mode == "ctc":
                phone_frames = ctc_decode_phones(
                    audio, ctc_model, ctc_processor,
                )
                for label, fi in phone_frames:
                    if 0 <= fi < embeddings.shape[0]:
                        all_embeddings.append(embeddings[fi])
                        all_labels.append(label)

            processed += 1
            if processed % 25 == 0:
                logger.info(
                    "Processed %d/%d (%d skipped), pool: %d phonemes",
                    processed, len(pairs), skipped, len(all_labels),
                )

        except Exception as e:
            logger.warning("Error processing %s: %s", wav_path.name, e)
            skipped += 1

    if not all_embeddings:
        logger.error("No embeddings extracted.")
        return

    # 5. Stack and L2-normalize
    logger.info("=" * 60)
    logger.info("STEP 3/3: Building pool and FAISS index...")
    logger.info("=" * 60)

    emb = np.array(all_embeddings, dtype=np.float32)
    lab = np.array(all_labels)

    norms = np.linalg.norm(emb, axis=1, keepdims=True)
    norms[norms == 0] = 1
    emb /= norms

    unique = sorted(set(all_labels))
    logger.info(
        "Pool: %s, %d unique phones: %s", emb.shape, len(unique), unique,
    )

    # 6. Save
    np.save(str(output_path / "embeddings.npy"), emb)
    np.save(str(output_path / "labels.npy"), lab)
    logger.info("Saved embeddings (%d MB)", emb.nbytes // (1024 * 1024))

    # 7. FAISS index
    try:
        import faiss
        index = faiss.IndexFlatIP(emb.shape[1])
        index.add(emb)
        faiss.write_index(index, str(output_path / "faiss_index.bin"))
        logger.info("FAISS index: %d entries.", index.ntotal)
    except ImportError:
        logger.warning(
            "FAISS not installed. Index built on first use. "
            "Install: pip install faiss-cpu"
        )

    logger.info("=" * 60)
    logger.info("DONE! %d files processed, %d skipped, %d phoneme entries → %s",
                processed, skipped, len(lab), output_path)
    logger.info("=" * 60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Build phoneme pool for retrieval-based MDD",
    )
    parser.add_argument(
        "--data-dir", required=True,
        help="Path to audio dataset (CMU ARCTIC, L2-ARCTIC, or WAV+txt)",
    )
    parser.add_argument(
        "--output-dir", default="backend/data/phoneme_pool",
        help="Output directory",
    )
    parser.add_argument(
        "--mode", choices=["mfa", "ctc"], default="ctc",
        help="'mfa' (accurate, needs conda) or 'ctc' (no MFA needed)",
    )
    parser.add_argument(
        "--max-files", type=int, default=500,
        help="Max audio files to process",
    )
    parser.add_argument(
        "--layer", type=int, default=-1,
        help="HuBERT layer (-1 = last)",
    )
    parser.add_argument(
        "--mfa-timeout", type=int, default=3600,
        help="MFA batch timeout in seconds (default: 3600 = 1 hour)",
    )
    args = parser.parse_args()

    build_pool(
        args.data_dir, args.output_dir,
        args.mode, args.max_files, args.layer,
        args.mfa_timeout,
    )
