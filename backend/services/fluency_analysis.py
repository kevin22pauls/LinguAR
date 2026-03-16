from __future__ import annotations

"""
Fluency analysis — uses CrisperWhisper word timestamps for pause detection.
DO NOT use Silero VAD here (per spec: removed from server-side fluency).

Metrics:
  Speed:     WPM, articulation rate, MLR (mean length of run)
  Breakdown: hesitation ratio, mid-phrase pause rate, longest fluent phrase
  Repair:    filled pause rate, repetition rate
  Rhythm:    (placeholder — full nPVI comes from prosody_analysis with MFA data)

Composite: 0.30*Speed + 0.35*Breakdown + 0.20*Repair + 0.15*Rhythm
"""

from dataclasses import dataclass, field
import re


# Pause thresholds (seconds)
PAUSE_BRIEF = 0.250      # 250ms
PAUSE_EXTENDED = 0.500   # 500ms
PAUSE_LONG = 1.000       # 1s

# Filled pauses (CrisperWhisper preserves these)
FILLED_PAUSES = {"um", "uh", "uhm", "er", "erm", "ah", "hm", "hmm", "mm"}

# Simple syllable estimation: count vowel clusters
_VOWEL_RE = re.compile(r"[aeiouy]+", re.IGNORECASE)


def _count_syllables(word: str) -> int:
    """Rough syllable count by vowel clusters. Minimum 1."""
    matches = _VOWEL_RE.findall(word)
    return max(1, len(matches))


@dataclass
class PauseInfo:
    start: float
    end: float
    duration: float
    category: str          # "brief", "extended", "long"
    context: str           # "between_words", "mid_phrase", "phrase_boundary"
    before_word: str
    after_word: str


@dataclass
class FluencyResult:
    # Speed fluency
    words_per_minute: float
    articulation_rate: float    # syllables/sec excluding pauses
    mean_length_of_run: float   # mean words between pauses > 250ms

    # Breakdown fluency
    hesitation_ratio: float     # pause time / total time
    mid_phrase_pause_rate: float  # mid-phrase pauses / total words
    longest_fluent_phrase: int  # max words without a pause > 250ms

    # Repair fluency
    filled_pause_rate: float    # fillers per minute
    repetition_rate: float      # repetitions per minute

    # Counts
    total_pauses: int
    hesitation_count: int
    speaking_rate: float        # syllables/sec including pauses

    # Composite score
    fluency_score: float        # 0-100

    # Detailed pause data
    pauses: list[PauseInfo] = field(default_factory=list)

    # Sub-scores for composite breakdown
    speed_score: float = 0.0
    breakdown_score: float = 0.0
    repair_score: float = 0.0
    rhythm_score: float = 50.0   # placeholder until prosody provides nPVI


def analyze_fluency(
    word_timestamps: list[dict],
    disfluencies: list[dict] | None = None,
    repetition_count: int = 0,
    duration_sec: float | None = None,
    npvi_v: float | None = None,
) -> FluencyResult:
    """
    Analyze fluency from word-level timestamps.

    word_timestamps: [{"word": str, "start": float, "end": float}, ...]
    disfluencies: list of filled pause entries from ASR
    """
    if not word_timestamps:
        return _empty_result()

    disfluencies = disfluencies or []

    # ── Timing basics ────────────────────────────────────────────────────
    first_start = word_timestamps[0]["start"]
    last_end = word_timestamps[-1]["end"]
    total_time = duration_sec if duration_sec else (last_end - first_start)
    if total_time <= 0:
        return _empty_result()

    # Filter content words (exclude filled pauses for speaking time)
    content_words = [w for w in word_timestamps if w["word"].lower().strip() not in FILLED_PAUSES]
    word_count = len(content_words)
    total_word_count = len(word_timestamps)

    # Total syllables
    total_syllables = sum(_count_syllables(w["word"]) for w in content_words)

    # Speaking time (sum of word durations)
    speaking_time = sum(max(0, w["end"] - w["start"]) for w in word_timestamps)
    if speaking_time <= 0:
        speaking_time = total_time  # fallback

    # ── Pause detection ──────────────────────────────────────────────────
    pauses = []
    for i in range(1, len(word_timestamps)):
        gap = word_timestamps[i]["start"] - word_timestamps[i - 1]["end"]
        if gap >= PAUSE_BRIEF:
            if gap >= PAUSE_LONG:
                cat = "long"
            elif gap >= PAUSE_EXTENDED:
                cat = "extended"
            else:
                cat = "brief"

            pauses.append(PauseInfo(
                start=word_timestamps[i - 1]["end"],
                end=word_timestamps[i]["start"],
                duration=gap,
                category=cat,
                context="between_words",  # refined below
                before_word=word_timestamps[i - 1]["word"],
                after_word=word_timestamps[i]["word"],
            ))

    total_pause_time = sum(p.duration for p in pauses)

    # Classify mid-phrase vs phrase-boundary pauses
    # Simple heuristic: phrase boundary if pause > 500ms or before a capitalized word
    mid_phrase_pauses = 0
    for p in pauses:
        if p.duration < PAUSE_EXTENDED:
            p.context = "mid_phrase"
            mid_phrase_pauses += 1
        else:
            p.context = "phrase_boundary"

    # ── Runs (fluent phrases between pauses) ─────────────────────────────
    runs = []
    current_run = 0
    word_idx = 0
    pause_starts = {round(p.start, 3) for p in pauses}

    for i, w in enumerate(word_timestamps):
        current_run += 1
        # Check if there's a pause after this word
        if i < len(word_timestamps) - 1:
            gap = word_timestamps[i + 1]["start"] - w["end"]
            if gap >= PAUSE_BRIEF:
                runs.append(current_run)
                current_run = 0
    if current_run > 0:
        runs.append(current_run)

    mlr = sum(runs) / len(runs) if runs else word_count
    longest_run = max(runs) if runs else word_count

    # ── Metrics ──────────────────────────────────────────────────────────
    minutes = total_time / 60
    wpm = word_count / minutes if minutes > 0 else 0
    articulation_rate = total_syllables / speaking_time if speaking_time > 0 else 0
    speaking_rate = total_syllables / total_time if total_time > 0 else 0
    hesitation_ratio = total_pause_time / total_time if total_time > 0 else 0
    mid_phrase_rate = mid_phrase_pauses / total_word_count if total_word_count > 0 else 0
    filler_count = len(disfluencies)
    filled_pause_rate_val = filler_count / minutes if minutes > 0 else 0
    repetition_rate_val = repetition_count / minutes if minutes > 0 else 0

    # ── Scoring (0-100 per dimension) ────────────────────────────────────

    # Speed score: target WPM ~130-160 for read speech
    if wpm >= 130:
        speed_score = min(100, 70 + (wpm - 130) * 0.5)
    elif wpm >= 80:
        speed_score = 30 + (wpm - 80) * 0.8
    else:
        speed_score = max(0, wpm * 0.375)

    # Breakdown score: lower hesitation = better
    breakdown_score = max(0, 100 - hesitation_ratio * 200 - mid_phrase_rate * 100)

    # Repair score: fewer fillers/repetitions = better
    repair_penalty = filled_pause_rate_val * 5 + repetition_rate_val * 8
    repair_score = max(0, 100 - repair_penalty)

    # Rhythm: use actual nPVI from prosody if available
    if npvi_v is not None:
        # English nPVI-V target ~55-65. Closer to 57.5 = better.
        if 45 <= npvi_v <= 75:
            rhythm_score = 100 - abs(npvi_v - 57.5) * 2
        else:
            rhythm_score = max(0, 50 - abs(npvi_v - 57.5))
    else:
        rhythm_score = 50.0  # fallback when prosody unavailable

    # Composite: 0.30*Speed + 0.35*Breakdown + 0.20*Repair + 0.15*Rhythm
    fluency_score = (
        0.30 * speed_score
        + 0.35 * breakdown_score
        + 0.20 * repair_score
        + 0.15 * rhythm_score
    )

    return FluencyResult(
        words_per_minute=round(wpm, 1),
        articulation_rate=round(articulation_rate, 2),
        mean_length_of_run=round(mlr, 1),
        hesitation_ratio=round(hesitation_ratio, 3),
        mid_phrase_pause_rate=round(mid_phrase_rate, 3),
        longest_fluent_phrase=longest_run,
        filled_pause_rate=round(filled_pause_rate_val, 1),
        repetition_rate=round(repetition_rate_val, 1),
        total_pauses=len(pauses),
        hesitation_count=mid_phrase_pauses,
        speaking_rate=round(speaking_rate, 2),
        fluency_score=round(fluency_score, 1),
        pauses=pauses,
        speed_score=round(speed_score, 1),
        breakdown_score=round(breakdown_score, 1),
        repair_score=round(repair_score, 1),
        rhythm_score=round(rhythm_score, 1),
    )


def _empty_result() -> FluencyResult:
    return FluencyResult(
        words_per_minute=0, articulation_rate=0, mean_length_of_run=0,
        hesitation_ratio=0, mid_phrase_pause_rate=0, longest_fluent_phrase=0,
        filled_pause_rate=0, repetition_rate=0, total_pauses=0,
        hesitation_count=0, speaking_rate=0, fluency_score=0, pauses=[],
    )
