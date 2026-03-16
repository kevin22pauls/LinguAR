from __future__ import annotations

"""
MFA (Montreal Forced Aligner) integration.

MFA requires Kaldi binaries via conda. It runs as a subprocess.
Handles failures gracefully — returns None so scoring continues without prosody.

Setup:
  conda create -n mfa_env -c conda-forge montreal-forced-aligner python=3.11 -y
  conda run -n mfa_env mfa model download acoustic english_us_arpa
  conda run -n mfa_env mfa model download dictionary english_us_arpa
"""

import logging
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

import numpy as np

logger = logging.getLogger(__name__)


def _find_conda() -> str:
    """Find the conda executable on the system."""
    # Check common locations
    candidates = [
        "conda",                             # on PATH
        "D:/Miniconda3/_conda.exe",          # Windows custom install
        "D:/Miniconda3/condabin/conda.bat",
        Path.home() / "miniconda3" / "_conda.exe",
        Path.home() / "miniconda3" / "condabin" / "conda",
        Path.home() / "anaconda3" / "condabin" / "conda",
    ]
    for c in candidates:
        p = Path(c)
        if p.exists():
            return str(p)
    # Fallback: assume conda is on PATH
    return "conda"


@dataclass
class PhoneAlignment:
    phone: str       # ARPAbet label (e.g. "K", "AE1")
    start: float     # seconds
    end: float       # seconds

    @property
    def duration(self) -> float:
        return self.end - self.start


@dataclass
class WordAlignment:
    word: str
    start: float
    end: float
    phones: list[PhoneAlignment]

    @property
    def duration(self) -> float:
        return self.end - self.start


@dataclass
class MFAResult:
    words: list[WordAlignment]
    phones: list[PhoneAlignment]
    textgrid_path: str | None


def run_mfa_alignment(
    audio_array: np.ndarray,
    transcript: str,
    sample_rate: int = 16000,
    timeout_sec: int = 120,
) -> MFAResult | None:
    """
    Run MFA forced alignment on audio + transcript.
    Returns phone-level alignments or None on failure.
    """
    tmpdir = tempfile.mkdtemp(prefix="mfa_")
    corpus_dir = Path(tmpdir) / "corpus"
    output_dir = Path(tmpdir) / "output"
    corpus_dir.mkdir()
    output_dir.mkdir()

    try:
        # Write audio as WAV
        import soundfile as sf
        wav_path = corpus_dir / "utterance.wav"
        sf.write(str(wav_path), audio_array, sample_rate)

        # Write transcript as .lab file (same name as wav)
        lab_path = corpus_dir / "utterance.lab"
        lab_path.write_text(transcript.strip(), encoding="utf-8")

        # Run MFA via conda subprocess
        # Find conda executable
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
        ]

        logger.info("Running MFA: %s", " ".join(cmd))
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout_sec,
        )

        if result.returncode != 0:
            logger.warning("MFA failed (exit %d): %s", result.returncode, result.stderr[:500])
            return None

        # Find output TextGrid
        textgrid_files = list(output_dir.rglob("*.TextGrid"))
        if not textgrid_files:
            logger.warning("MFA produced no TextGrid output.")
            return None

        return parse_textgrid(str(textgrid_files[0]))

    except subprocess.TimeoutExpired:
        logger.warning("MFA alignment timed out after %ds.", timeout_sec)
        return None
    except FileNotFoundError:
        logger.warning("conda/mfa not found. MFA alignment skipped.")
        return None
    except Exception as e:
        logger.warning("MFA alignment error: %s", e)
        return None
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


def parse_textgrid(textgrid_path: str) -> MFAResult:
    """Parse a Praat TextGrid file into structured phone/word alignments."""
    from praatio import textgrid as tgio

    tg = tgio.openTextgrid(textgrid_path, includeEmptyIntervals=False)

    words = []
    all_phones = []

    # Parse word tier
    word_entries = []
    if "words" in tg.tierNames:
        word_tier = tg.getTier("words")
        for interval in word_tier.entries:
            word_entries.append({
                "word": interval.label,
                "start": interval.start,
                "end": interval.end,
            })

    # Parse phone tier
    phone_entries = []
    if "phones" in tg.tierNames:
        phone_tier = tg.getTier("phones")
        for interval in phone_tier.entries:
            pa = PhoneAlignment(
                phone=interval.label,
                start=interval.start,
                end=interval.end,
            )
            phone_entries.append(pa)
            all_phones.append(pa)

    # Associate phones with words by time overlap
    for we in word_entries:
        word_phones = [
            p for p in phone_entries
            if p.start >= we["start"] - 0.001 and p.end <= we["end"] + 0.001
        ]
        words.append(WordAlignment(
            word=we["word"],
            start=we["start"],
            end=we["end"],
            phones=word_phones,
        ))

    return MFAResult(
        words=words,
        phones=all_phones,
        textgrid_path=textgrid_path,
    )
