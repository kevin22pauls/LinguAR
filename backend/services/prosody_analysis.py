from __future__ import annotations

"""
Prosody analysis — F0 (pitch), intensity, lexical stress, intonation, rhythm.

Uses parselmouth (Praat) for F0/intensity extraction.
Uses MFA phone boundaries for rhythm (nPVI-V) and stress detection.

Composite: 0.35*Stress + 0.30*Intonation + 0.20*Rhythm + 0.15*PitchRange
"""

import math
import logging
from dataclasses import dataclass, field

import numpy as np
import parselmouth
from parselmouth.praat import call

logger = logging.getLogger(__name__)

# ARPAbet vowels (for rhythm/stress analysis)
ARPABET_VOWELS = {
    "AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY",
    "IH", "IY", "OW", "OY", "UH", "UW",
}


def _is_vowel(phone: str) -> bool:
    """Check if ARPAbet phone is a vowel (strip stress digit)."""
    base = phone.rstrip("012")
    return base in ARPABET_VOWELS


def _has_primary_stress(phone: str) -> bool:
    """Check if phone has primary stress marker '1'."""
    return phone.endswith("1")


@dataclass
class ProsodyResult:
    # Sub-scores (0-100)
    stress_accuracy: float
    intonation_accuracy: float
    rhythm_npvi_v: float       # raw nPVI value (typically 30-70 for English)
    pitch_range_st: float      # F0 std dev in semitones

    # Composite
    prosody_score: float       # 0-100

    # Details
    f0_mean: float
    f0_std: float
    intensity_mean: float
    words_with_correct_stress: int
    words_total_checked: int
    per_word_stress: dict = field(default_factory=dict)  # {word: True/False}
    details: list[dict] = field(default_factory=list)


def analyze_prosody(
    audio_array: np.ndarray,
    sample_rate: int = 16000,
    mfa_result=None,          # MFAResult from mfa_alignment
    word_phonemes: list[list[str]] | None = None,  # canonical phonemes per word
) -> ProsodyResult:
    """
    Analyze prosody of a speech recording.

    audio_array: 16kHz mono float32
    mfa_result: optional MFA alignment for phone-level analysis
    word_phonemes: canonical ARPAbet phonemes per word (from phoneme_lookup)
    """
    # ── F0 extraction via parselmouth ────────────────────────────────────
    sound = parselmouth.Sound(audio_array, sampling_frequency=sample_rate)
    pitch = call(sound, "To Pitch", 0.0, 75.0, 500.0)  # time_step=0, min=75Hz, max=500Hz
    intensity = call(sound, "To Intensity", 100, 0.0)    # min_pitch=100Hz

    # Get F0 values (0 = unvoiced)
    f0_values = pitch.selected_array["frequency"].flatten()
    voiced = f0_values[f0_values > 0]

    if len(voiced) < 2:
        return _empty_prosody()

    f0_mean = float(np.mean(voiced))
    f0_std = float(np.std(voiced))

    # Pitch range in semitones: 12 * log2(max/min)
    f0_min = float(np.percentile(voiced, 5))
    f0_max = float(np.percentile(voiced, 95))
    if f0_min > 0:
        pitch_range_st = 12 * math.log2(f0_max / f0_min)
    else:
        pitch_range_st = 0.0

    # Mean intensity
    int_values = [call(intensity, "Get value at time", t, "cubic")
                  for t in np.linspace(sound.xmin, sound.xmax, 100)]
    int_values = [v for v in int_values if v is not None and not math.isnan(v)]
    intensity_mean = float(np.mean(int_values)) if int_values else 0.0

    # ── Lexical stress detection ─────────────────────────
    stress_correct = 0
    stress_total = 0
    per_word_stress = {}
    details = []

    if mfa_result and word_phonemes:
        for mfa_word, canonical_phones in zip(mfa_result.words, word_phonemes):
            if not mfa_word.phones or not canonical_phones:
                continue

            # Find canonical stressed vowel
            stressed_idx = None
            for i, p in enumerate(canonical_phones):
                if _has_primary_stress(p):
                    stressed_idx = i
                    break
            if stressed_idx is None:
                continue

            # Find vowels in MFA alignment
            vowel_phones = [(i, p) for i, p in enumerate(mfa_word.phones) if _is_vowel(p.phone)]
            if len(vowel_phones) < 2:
                continue  # can't evaluate stress with < 2 vowels

            stress_total += 1

            # For each vowel: get mean F0 and intensity
            vowel_features = []
            for idx, phone_align in vowel_phones:
                mid_time = (phone_align.start + phone_align.end) / 2
                f0_at = call(pitch, "Get value at time", mid_time, "Hertz", "linear")
                int_at = call(intensity, "Get value at time", mid_time, "cubic")
                dur = phone_align.duration
                vowel_features.append({
                    "phone": phone_align.phone,
                    "f0": f0_at if f0_at and not math.isnan(f0_at) else 0,
                    "intensity": int_at if int_at and not math.isnan(int_at) else 0,
                    "duration": dur,
                })

            # The stressed vowel should have higher F0, intensity, or duration
            # than the mean of unstressed vowels
            canonical_stressed_vowel_idx = None
            vowel_count = 0
            for i, p in enumerate(canonical_phones):
                if _is_vowel(p):
                    if i == stressed_idx:
                        canonical_stressed_vowel_idx = vowel_count
                    vowel_count += 1

            if canonical_stressed_vowel_idx is not None and canonical_stressed_vowel_idx < len(vowel_features):
                stressed_feat = vowel_features[canonical_stressed_vowel_idx]
                other_feats = [v for j, v in enumerate(vowel_features) if j != canonical_stressed_vowel_idx]

                if other_feats:
                    avg_other_dur = np.mean([v["duration"] for v in other_feats])
                    avg_other_int = np.mean([v["intensity"] for v in other_feats])

                    # Correct stress if stressed vowel has longer duration or higher intensity
                    dur_ok = stressed_feat["duration"] > avg_other_dur * 0.9
                    int_ok = stressed_feat["intensity"] > avg_other_int - 2

                    correct = dur_ok or int_ok
                    per_word_stress[mfa_word.word] = correct
                    if correct:
                        stress_correct += 1

            details.append({
                "word": mfa_word.word,
                "vowels": vowel_features,
            })

    stress_accuracy = (stress_correct / stress_total * 100) if stress_total > 0 else 50.0

    # ── Intonation (phrase-final F0 pattern) ─────────────────────────────
    # Simple: check if F0 falls at the end (declarative sentences)
    n_frames = len(voiced)
    if n_frames >= 10:
        last_quarter = voiced[int(n_frames * 0.75):]
        first_quarter = voiced[:int(n_frames * 0.25)]
        f0_final = float(np.mean(last_quarter))
        f0_initial = float(np.mean(first_quarter))

        # For declarative sentences: F0 should fall
        if f0_final < f0_initial:
            intonation_accuracy = 80.0 + min(20, (f0_initial - f0_final) / f0_initial * 100)
        else:
            intonation_accuracy = max(20.0, 60.0 - (f0_final - f0_initial) / f0_initial * 100)
    else:
        intonation_accuracy = 50.0

    intonation_accuracy = min(100.0, max(0.0, intonation_accuracy))

    # ── Rhythm (nPVI-V) ──────────────────────────────────────────────────
    npvi_v = 50.0  # default

    if mfa_result:
        vowel_durations = []
        for phone in mfa_result.phones:
            if _is_vowel(phone.phone):
                vowel_durations.append(phone.duration)

        if len(vowel_durations) >= 2:
            # nPVI = 100 * mean(|d_k - d_{k+1}| / ((d_k + d_{k+1}) / 2))
            diffs = []
            for i in range(len(vowel_durations) - 1):
                d1 = vowel_durations[i]
                d2 = vowel_durations[i + 1]
                mean_d = (d1 + d2) / 2
                if mean_d > 0:
                    diffs.append(abs(d1 - d2) / mean_d)

            npvi_v = 100 * np.mean(diffs) if diffs else 50.0

    # Rhythm score: English nPVI-V is typically 50-70. Closer to 55-65 = better.
    if 45 <= npvi_v <= 75:
        rhythm_score = 100 - abs(npvi_v - 57.5) * 2
    else:
        rhythm_score = max(0, 50 - abs(npvi_v - 57.5))

    # ── Pitch range score ────────────────────────────────────────────────
    # Good English speech has ~6-12 semitone range
    if 5 <= pitch_range_st <= 14:
        pitch_score = 100 - abs(pitch_range_st - 9) * 5
    else:
        pitch_score = max(0, 50 - abs(pitch_range_st - 9) * 5)

    # ── Composite ────────────────────────────────────────────────────────
    prosody_score = (
        0.35 * stress_accuracy
        + 0.30 * intonation_accuracy
        + 0.20 * rhythm_score
        + 0.15 * pitch_score
    )

    return ProsodyResult(
        stress_accuracy=round(stress_accuracy, 1),
        intonation_accuracy=round(intonation_accuracy, 1),
        rhythm_npvi_v=round(npvi_v, 1),
        pitch_range_st=round(pitch_range_st, 1),
        prosody_score=round(prosody_score, 1),
        f0_mean=round(f0_mean, 1),
        f0_std=round(f0_std, 1),
        intensity_mean=round(intensity_mean, 1),
        words_with_correct_stress=stress_correct,
        words_total_checked=stress_total,
        per_word_stress=per_word_stress,
        details=details,
    )


def _empty_prosody() -> ProsodyResult:
    return ProsodyResult(
        stress_accuracy=0, intonation_accuracy=0, rhythm_npvi_v=0,
        pitch_range_st=0, prosody_score=0, f0_mean=0, f0_std=0,
        intensity_mean=0, words_with_correct_stress=0,
        words_total_checked=0,
    )
