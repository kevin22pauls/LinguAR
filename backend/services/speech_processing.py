from __future__ import annotations

"""
Speech processing — main pipeline orchestrator.

Full pipeline:
  1. Load audio → 16kHz mono
  2. CrisperWhisper → transcript + word timestamps + disfluencies
  3. Reading accuracy (jiwer) → word-level C/S/D/I/R labels
  4. MFA alignment → phone boundaries (optional, graceful failure)
  5. Prosody analysis → stress/intonation/rhythm scores
  6. Fluency analysis → speed/breakdown/repair scores (with nPVI from prosody)
  7. HuBERT MDD → phone-level error detection (optional, needs pool)
  8. Intelligibility scoring → FL-weighted pronunciation score
  9. Hierarchical scoring → aggregate all dimensions
  10. Return structured result
"""

import logging

import numpy as np
import torch
import torchaudio

from backend.config import settings

logger = logging.getLogger(__name__)


def _tag_phone_errors(mdd_result) -> list[dict]:
    """Build phone error list with L1-expected flag for each substitution."""
    if not mdd_result:
        return []
    try:
        from backend.services.intelligibility_scoring import is_l1_expected
    except ImportError:
        is_l1_expected = lambda c, p: (False, 1.0)

    errors = []
    for pe in mdd_result.phone_errors:
        entry = {
            "position": pe.position,
            "canonical": pe.canonical,
            "predicted": pe.predicted,
            "error_type": pe.error_type,
            "gop_score": round(pe.gop_score, 2),
        }
        if pe.error_type == "substitution":
            expected, _ = is_l1_expected(pe.canonical, pe.predicted)
            entry["l1_expected"] = expected
        else:
            entry["l1_expected"] = False
        errors.append(entry)
    return errors

def _build_word_feedback(alignments, word_phonemes, mdd_result) -> list[dict]:
    """
    Build word-level feedback with FL-weighted coloring.

    Colors:
      - correct (green): word pronounced correctly
      - fl-high (red): word has phone errors with high functional load (FL >= 0.5)
      - fl-low (yellow): word has phone errors with low FL (< 0.5)
      - error (red fallback): error but no MDD data to determine FL
      - partial (yellow): repetitions / insertions
    """
    try:
        from backend.services.intelligibility_scoring import get_functional_load
        has_fl = True
    except ImportError:
        has_fl = False

    # Map phone positions to word indices
    # word_phonemes is list[list[str]] — phonemes per reference word
    phone_to_word = {}
    pos = 0
    for word_idx, phones in enumerate(word_phonemes):
        for _ in phones:
            phone_to_word[pos] = word_idx
            pos += 1

    # Collect max FL per reference word from phone errors
    word_max_fl = {}
    if mdd_result and has_fl:
        for pe in mdd_result.phone_errors:
            if pe.error_type == "substitution":
                w_idx = phone_to_word.get(pe.position)
                if w_idx is not None:
                    fl = get_functional_load(pe.canonical, pe.predicted)
                    word_max_fl[w_idx] = max(word_max_fl.get(w_idx, 0), fl)
            elif pe.error_type == "deletion":
                w_idx = phone_to_word.get(pe.position)
                if w_idx is not None:
                    word_max_fl[w_idx] = max(word_max_fl.get(w_idx, 0), 0.6)

    feedback = []
    ref_word_idx = 0  # tracks position in reference words
    for alignment in alignments:
        if alignment.label == "C":
            feedback.append({
                "word": alignment.ref_word, "status": "correct", "fl": 0,
            })
            ref_word_idx += 1
        elif alignment.label in ("S", "D"):
            fl = word_max_fl.get(ref_word_idx, -1)
            if fl >= 0.5:
                status = "fl-high"
            elif fl >= 0:
                status = "fl-low"
            else:
                status = "error"
            feedback.append({
                "word": alignment.ref_word, "status": status,
                "fl": round(fl, 2) if fl >= 0 else None,
            })
            ref_word_idx += 1
        elif alignment.label == "R":
            feedback.append({
                "word": alignment.hyp_word, "status": "partial", "fl": None,
            })
        elif alignment.label == "I":
            feedback.append({
                "word": alignment.hyp_word, "status": "partial", "fl": None,
            })
    return feedback


FILLED_PAUSES = {"um", "uh", "uhm", "er", "erm", "ah", "hm", "hmm", "mm"}


def load_audio(audio_bytes: bytes, target_sr: int = 16000) -> np.ndarray:
    """Load audio from bytes (WAV or WebM) → 16kHz mono float32 numpy array."""
    import io
    import soundfile as sf

    try:
        # Try soundfile first (handles WAV, FLAC, OGG)
        data, sr = sf.read(io.BytesIO(audio_bytes), dtype="float32")
    except Exception:
        # Fallback: use PyAV for WebM/other container formats
        data, sr = _load_audio_pyav(audio_bytes)

    # Handle stereo → mono
    if data.ndim > 1:
        data = data.mean(axis=1)

    # Resample if needed
    if sr != target_sr:
        resampler = torchaudio.transforms.Resample(orig_freq=sr, new_freq=target_sr)
        data = resampler(torch.from_numpy(data).unsqueeze(0)).squeeze().numpy()

    return data


def _load_audio_pyav(audio_bytes: bytes):
    """Decode audio bytes using PyAV (handles WebM, MP4, etc.)."""
    import io
    import av

    container = av.open(io.BytesIO(audio_bytes))
    stream = container.streams.audio[0]
    sr = stream.rate or 48000

    frames = []
    for frame in container.decode(audio=0):
        arr = frame.to_ndarray()
        # PyAV returns shape (channels, samples) for planar or (samples, channels) for interleaved
        if arr.ndim > 1:
            arr = arr.mean(axis=0) if arr.shape[0] <= arr.shape[1] else arr.mean(axis=1)
        frames.append(arr)
    container.close()

    if not frames:
        raise ValueError("No audio frames decoded from input")

    data = np.concatenate(frames).astype(np.float32)
    # Normalize int formats to [-1, 1]
    if data.max() > 1.0 or data.min() < -1.0:
        max_val = max(abs(data.max()), abs(data.min()))
        if max_val > 0:
            data = data / max_val

    return data, sr


def transcribe(audio_array: np.ndarray) -> dict:
    """Run ASR → text + word timestamps + disfluencies."""
    from backend.models.crisperwhisper_model import (
        get_asr_pipeline,
        adjust_pauses_for_hf_pipeline_output,
    )

    pipe = get_asr_pipeline()
    result = pipe(
        audio_array.astype(np.float32),
        generate_kwargs={"language": "en", "task": "transcribe"},
    )

    # CrisperWhisper: adjust pause boundaries for accurate timestamps
    result = adjust_pauses_for_hf_pipeline_output(result)

    words = []
    disfluencies = []

    if "chunks" in result:
        for chunk in result["chunks"]:
            word_text = chunk.get("text", "").strip()
            timestamps = chunk.get("timestamp", (None, None))
            start = timestamps[0] if timestamps[0] is not None else 0.0
            end = timestamps[1] if timestamps[1] is not None else start

            entry = {"word": word_text, "start": start, "end": end}
            words.append(entry)

            if word_text.lower() in FILLED_PAUSES:
                disfluencies.append(entry)
    else:
        for w in result.get("text", "").split():
            words.append({"word": w, "start": 0.0, "end": 0.0})

    return {
        "text": result.get("text", "").strip(),
        "words": words,
        "disfluencies": disfluencies,
    }


def analyze_recording(audio_bytes: bytes, reference_text: str, object_name: str = "") -> dict:
    """
    Full analysis pipeline. Each stage handles failures gracefully.
    """
    from backend.services.reading_accuracy import analyze_reading
    from backend.services.fluency_analysis import analyze_fluency
    from backend.services.prosody_analysis import analyze_prosody
    from backend.services.phoneme_lookup import get_phonemes_for_sentence
    from backend.services.hierarchical_scorer import compute_hierarchical_scores

    # ── 1. Load audio ────────────────────────────────────────────────────
    audio_array = load_audio(audio_bytes)
    duration_sec = len(audio_array) / settings.sample_rate

    # ── 2. ASR ───────────────────────────────────────────────────────────
    asr_result = transcribe(audio_array)
    transcript = asr_result["text"]

    # ── 3. Reading accuracy ──────────────────────────────────────────────
    reading = analyze_reading(reference_text, transcript)

    # ── 4. MFA alignment — SKIPPED for live analysis (too slow) ─────────
    # MFA adds ~2 min per recording due to conda subprocess startup.
    # Prosody analysis works without it (uses F0 contour only).
    # MFA is used only for offline phoneme pool building.
    mfa_result = None

    # ── 5. Prosody analysis ──────────────────────────────────────────────
    word_phonemes = get_phonemes_for_sentence(reference_text)
    prosody = analyze_prosody(
        audio_array=audio_array,
        sample_rate=settings.sample_rate,
        mfa_result=mfa_result,
        word_phonemes=word_phonemes,
    )

    # ── 6. Fluency analysis (with nPVI from prosody) ───────────────────
    fluency = analyze_fluency(
        word_timestamps=asr_result["words"],
        disfluencies=asr_result["disfluencies"],
        repetition_count=reading.repetition_count,
        duration_sec=duration_sec,
        npvi_v=prosody.rhythm_npvi_v if prosody.rhythm_npvi_v > 0 else None,
    )

    # ── 7. HuBERT MDD (optional — needs phoneme pool) ───────────────────
    mdd_result = None
    intelligibility = None
    l1_expected_errors = []
    try:
        from backend.services.mdd_engine import run_mdd, load_phoneme_pool
        from backend.services.intelligibility_scoring import (
            compute_intelligibility_score, is_l1_expected,
        )

        load_phoneme_pool()

        # Flatten canonical phones
        canonical_flat = [p for word_phones in word_phonemes for p in word_phones]
        if canonical_flat:
            mdd_result = run_mdd(audio_array, canonical_flat)
            intelligibility = compute_intelligibility_score(mdd_result.phone_errors)

            # Tag L1-expected errors for UI feedback
            for pe in mdd_result.phone_errors:
                if pe.error_type == "substitution":
                    expected, _ = is_l1_expected(pe.canonical, pe.predicted)
                    if expected:
                        l1_expected_errors.append({
                            "canonical": pe.canonical,
                            "predicted": pe.predicted,
                            "position": pe.position,
                        })
    except Exception as e:
        logger.info("MDD scoring skipped: %s", e)

    # ── 8. Hierarchical scoring ──────────────────────────────────────────
    scores = compute_hierarchical_scores(
        reading_result=reading,
        mdd_result=mdd_result,
        fluency_result=fluency,
        prosody_result=prosody,
        intelligibility_score=intelligibility,
    )

    # ── 9. Build word-level feedback for UI (FL-weighted coloring) ──────
    word_feedback = _build_word_feedback(
        reading.alignments, word_phonemes, mdd_result,
    )

    # ── 10. Build response ───────────────────────────────────────────────
    return {
        "status": "complete",
        "transcript": transcript,
        "reference": reference_text,
        "duration_sec": round(duration_sec, 2),

        # 4-dimension scores
        "accuracy": round(scores.utterance_accuracy),
        "fluency": round(scores.utterance_fluency),
        "prosody": round(scores.utterance_prosody),
        "completeness": round(scores.utterance_completeness),
        "total": round(scores.utterance_total),

        # Reading detail
        "wer": reading.wer,
        "classification": reading.classification,

        # Word-level feedback
        "words": word_feedback,
        "word_scores": [
            {"word": ws.word, "accuracy": ws.accuracy, "label": ws.completeness}
            for ws in scores.word_scores
        ],

        # Fluency details
        "words_per_minute": fluency.words_per_minute,
        "articulation_rate": fluency.articulation_rate,
        "mean_length_of_run": fluency.mean_length_of_run,
        "longest_fluent_phrase": fluency.longest_fluent_phrase,

        # Prosody details
        "stress_accuracy": prosody.stress_accuracy,
        "intonation_accuracy": prosody.intonation_accuracy,
        "rhythm_npvi_v": prosody.rhythm_npvi_v,
        "pitch_range_st": prosody.pitch_range_st,

        # Counts
        "filler_count": len(asr_result["disfluencies"]),
        "repetition_count": reading.repetition_count,

        # MDD details (if available)
        "pronunciation_score": intelligibility,
        "phone_error_rate": mdd_result.phone_error_rate if mdd_result else None,

        # Phoneme-level analysis (with L1 awareness)
        "phone_errors": _tag_phone_errors(mdd_result),
        "predicted_phones": mdd_result.predicted_sequence if mdd_result else [],
        "canonical_phones": mdd_result.canonical_sequence if mdd_result else [],
        "mdd_counts": {
            "correct": mdd_result.correct_count,
            "substitution": mdd_result.substitution_count,
            "deletion": mdd_result.deletion_count,
            "insertion": mdd_result.insertion_count,
        } if mdd_result else None,

        # L1 transfer info (Tamil)
        "l1": settings.default_l1,
        "l1_expected_errors": l1_expected_errors,
    }
