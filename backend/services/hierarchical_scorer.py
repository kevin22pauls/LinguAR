from __future__ import annotations

"""
Hierarchical scorer — aggregates phone→word→utterance level scores.

Four dimensions:
  Accuracy:     phone-level MDD + FL weighting → word mean → utterance mean
  Completeness: word-level C/S/D/I counts → percentage correct
  Fluency:      from fluency_analysis module
  Prosody:      from prosody_analysis module

Utterance total: 0.35*Accuracy + 0.25*Fluency + 0.25*Prosody + 0.15*Completeness
"""

from dataclasses import dataclass, field


@dataclass
class WordScore:
    word: str
    accuracy: float       # 0-100 (phone-level, FL-weighted)
    stress: float         # 0-100 (from prosody)
    completeness: str     # "C", "S", "D", "I", "R"
    total: float          # combined word score


@dataclass
class HierarchicalScores:
    # Per-word
    word_scores: list[WordScore] = field(default_factory=list)

    # Utterance-level (0-100)
    utterance_accuracy: float = 0.0
    utterance_completeness: float = 0.0
    utterance_fluency: float = 0.0
    utterance_prosody: float = 0.0
    utterance_total: float = 0.0


def compute_hierarchical_scores(
    reading_result=None,           # ReadingResult from reading_accuracy
    mdd_result=None,               # MDDResult from mdd_engine
    fluency_result=None,           # FluencyResult from fluency_analysis
    prosody_result=None,           # ProsodyResult from prosody_analysis
    intelligibility_score: float | None = None,  # from intelligibility_scoring
) -> HierarchicalScores:
    """
    Aggregate all analysis results into hierarchical scores.
    Handles missing components gracefully (uses available data).
    """
    scores = HierarchicalScores()

    # ── Accuracy (phone-level → utterance) ───────────────────────────────
    if intelligibility_score is not None:
        scores.utterance_accuracy = intelligibility_score
    elif reading_result:
        # Fallback: use reading accuracy as proxy for pronunciation accuracy
        scores.utterance_accuracy = reading_result.accuracy
    else:
        scores.utterance_accuracy = 0.0

    # ── Completeness (word-level) ────────────────────────────────────────
    if reading_result:
        scores.utterance_completeness = reading_result.completeness
    else:
        scores.utterance_completeness = 0.0

    # ── Fluency ──────────────────────────────────────────────────────────
    if fluency_result:
        scores.utterance_fluency = fluency_result.fluency_score
    else:
        scores.utterance_fluency = 0.0

    # ── Prosody ──────────────────────────────────────────────────────────
    if prosody_result:
        scores.utterance_prosody = prosody_result.prosody_score
    else:
        scores.utterance_prosody = 0.0

    # ── Per-word scores ──────────────────────────────────────────────────
    # Build per-word stress lookup from prosody result
    word_stress_map = {}
    if prosody_result and prosody_result.per_word_stress:
        word_stress_map = prosody_result.per_word_stress

    if reading_result:
        for alignment in reading_result.alignments:
            word = alignment.ref_word or alignment.hyp_word
            label = alignment.label

            if label == "C":
                word_acc = 100.0
            elif label == "S":
                word_acc = 30.0
            elif label == "R":
                word_acc = 50.0
            else:
                word_acc = 0.0

            # Per-word stress: use MFA-based result if available
            word_lower = word.lower() if word else ""
            if word_lower in word_stress_map:
                word_stress = 100.0 if word_stress_map[word_lower] else 30.0
            else:
                # Fallback: utterance-level prosody as proxy
                word_stress = scores.utterance_prosody

            word_total = word_acc * 0.7 + word_stress * 0.3
            scores.word_scores.append(WordScore(
                word=word,
                accuracy=word_acc,
                stress=round(word_stress, 1),
                completeness=label,
                total=round(word_total, 1),
            ))

    # ── Utterance total ──────────────────────────────────────────────────
    scores.utterance_total = round(
        0.35 * scores.utterance_accuracy
        + 0.25 * scores.utterance_fluency
        + 0.25 * scores.utterance_prosody
        + 0.15 * scores.utterance_completeness,
        1,
    )

    # Round all
    scores.utterance_accuracy = round(scores.utterance_accuracy, 1)
    scores.utterance_completeness = round(scores.utterance_completeness, 1)
    scores.utterance_fluency = round(scores.utterance_fluency, 1)
    scores.utterance_prosody = round(scores.utterance_prosody, 1)

    return scores
