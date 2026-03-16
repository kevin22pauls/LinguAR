from __future__ import annotations

"""
Reading accuracy — word-level alignment using jiwer.
Classifies each word as Correct / Substitution / Deletion / Insertion / Repetition.
"""

import re
from dataclasses import dataclass
from jiwer import process_words


@dataclass
class WordAlignment:
    ref_word: str        # expected word (empty for insertions)
    hyp_word: str        # spoken word (empty for deletions)
    label: str           # C (correct), S (substitution), D (deletion), I (insertion), R (repetition)


@dataclass
class ReadingResult:
    alignments: list[WordAlignment]
    accuracy: float          # % correct words (C count / ref length)
    wer: float               # word error rate
    completeness: float      # % of reference words attempted (non-deleted)
    correct_count: int
    substitution_count: int
    deletion_count: int
    insertion_count: int
    repetition_count: int
    classification: str      # CORRECT / PARTIAL / NEEDS_RETRY


def _normalize(text: str) -> str:
    """Lowercase, strip punctuation, collapse whitespace."""
    text = text.lower()
    text = re.sub(r"[^\w\s']", "", text)
    return " ".join(text.split())


def analyze_reading(reference: str, hypothesis: str) -> ReadingResult:
    """
    Compare reference text with ASR hypothesis (transcript of what the learner said).
    Returns word-level alignment and aggregate scores.
    """
    ref_norm = _normalize(reference)
    hyp_norm = _normalize(hypothesis)

    if not ref_norm:
        return ReadingResult(
            alignments=[], accuracy=0, wer=1.0, completeness=0,
            correct_count=0, substitution_count=0, deletion_count=0,
            insertion_count=0, repetition_count=0, classification="NEEDS_RETRY",
        )

    result = process_words(ref_norm, hyp_norm)

    alignments = []
    correct = 0
    substitutions = 0
    deletions = 0
    insertions = 0
    repetitions = 0

    # process_words returns alignment chunks
    for chunk in result.alignments[0]:
        chunk_type = chunk.type

        if chunk_type == "equal":
            for i in range(chunk.ref_end_idx - chunk.ref_start_idx):
                ref_w = result.references[0][chunk.ref_start_idx + i]
                hyp_w = result.hypotheses[0][chunk.hyp_start_idx + i]
                alignments.append(WordAlignment(ref_word=ref_w, hyp_word=hyp_w, label="C"))
                correct += 1

        elif chunk_type == "substitute":
            for i in range(max(chunk.ref_end_idx - chunk.ref_start_idx,
                               chunk.hyp_end_idx - chunk.hyp_start_idx)):
                ref_idx = chunk.ref_start_idx + i
                hyp_idx = chunk.hyp_start_idx + i
                ref_w = result.references[0][ref_idx] if ref_idx < chunk.ref_end_idx else ""
                hyp_w = result.hypotheses[0][hyp_idx] if hyp_idx < chunk.hyp_end_idx else ""
                alignments.append(WordAlignment(ref_word=ref_w, hyp_word=hyp_w, label="S"))
                substitutions += 1

        elif chunk_type == "delete":
            for i in range(chunk.ref_end_idx - chunk.ref_start_idx):
                ref_w = result.references[0][chunk.ref_start_idx + i]
                alignments.append(WordAlignment(ref_word=ref_w, hyp_word="", label="D"))
                deletions += 1

        elif chunk_type == "insert":
            for i in range(chunk.hyp_end_idx - chunk.hyp_start_idx):
                hyp_w = result.hypotheses[0][chunk.hyp_start_idx + i]
                alignments.append(WordAlignment(ref_word="", hyp_word=hyp_w, label="I"))
                insertions += 1

    # Detect repetitions: consecutive duplicate words in hypothesis not in reference
    hyp_words = hyp_norm.split()
    ref_words = ref_norm.split()
    for i in range(1, len(hyp_words)):
        if hyp_words[i] == hyp_words[i - 1]:
            # Check if this repetition isn't in the reference
            ref_pairs = [(ref_words[j], ref_words[j + 1]) for j in range(len(ref_words) - 1)]
            if (hyp_words[i - 1], hyp_words[i]) not in ref_pairs:
                # Mark the duplicate as repetition in alignments
                for a in alignments:
                    if a.hyp_word == hyp_words[i] and a.label == "I":
                        a.label = "R"
                        repetitions += 1
                        insertions -= 1
                        break

    ref_len = len(ref_words)
    accuracy = (correct / ref_len * 100) if ref_len > 0 else 0
    completeness = ((ref_len - deletions) / ref_len * 100) if ref_len > 0 else 0
    wer = result.wer if hasattr(result, "wer") else (substitutions + deletions + insertions) / ref_len

    if accuracy >= 90:
        classification = "CORRECT"
    elif accuracy >= 50:
        classification = "PARTIAL"
    else:
        classification = "NEEDS_RETRY"

    return ReadingResult(
        alignments=alignments,
        accuracy=round(accuracy, 1),
        wer=round(wer, 3),
        completeness=round(completeness, 1),
        correct_count=correct,
        substitution_count=substitutions,
        deletion_count=deletions,
        insertion_count=insertions,
        repetition_count=repetitions,
        classification=classification,
    )
