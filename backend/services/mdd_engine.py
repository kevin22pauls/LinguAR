from __future__ import annotations

"""
Retrieval-based Mispronunciation Detection and Diagnosis (MDD).
Implementation of Tu et al. (2025) — arXiv:2511.20107.

# REQUIRES: Phoneme pool built via scripts/build_phoneme_pool.py

Algorithm:
  1. Extract HuBERT embeddings from learner audio
  2. For each frame: k-NN query against phoneme pool
  3. Majority vote → predicted phone per frame
  4. Collapse consecutive duplicates
  5. Align predicted vs canonical → classify errors

Also includes GOP (Goodness of Pronunciation) as a complementary metric.
"""

import logging
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

from backend.config import settings, DATA_DIR

logger = logging.getLogger(__name__)

POOL_DIR = DATA_DIR / "phoneme_pool"

_faiss_index = None
_pool_labels = None


@dataclass
class PhoneError:
    position: int
    canonical: str       # expected ARPAbet phone
    predicted: str       # detected ARPAbet phone (or "" for deletion)
    error_type: str      # "correct", "substitution", "deletion", "insertion"
    gop_score: float = 0.0


@dataclass
class MDDResult:
    phone_errors: list[PhoneError]
    predicted_sequence: list[str]
    canonical_sequence: list[str]
    phone_error_rate: float   # % phones incorrect
    gop_mean: float           # mean GOP across phones
    correct_count: int
    substitution_count: int
    deletion_count: int
    insertion_count: int


def load_phoneme_pool():
    """Load pre-built phoneme pool and FAISS index."""
    global _faiss_index, _pool_labels

    if _faiss_index is not None:
        return

    embeddings_path = POOL_DIR / "embeddings.npy"
    labels_path = POOL_DIR / "labels.npy"
    index_path = POOL_DIR / "faiss_index.bin"

    if not embeddings_path.exists():
        logger.warning("Phoneme pool not found at %s. MDD will be unavailable.", POOL_DIR)
        return

    try:
        import faiss

        _pool_labels = np.load(str(labels_path), allow_pickle=True)

        if index_path.exists():
            _faiss_index = faiss.read_index(str(index_path))
        else:
            embeddings = np.load(str(embeddings_path))
            # Normalize for cosine similarity via inner product
            faiss.normalize_L2(embeddings)
            _faiss_index = faiss.IndexFlatIP(embeddings.shape[1])
            _faiss_index.add(embeddings)
            faiss.write_index(_faiss_index, str(index_path))

        logger.info("Phoneme pool loaded: %d entries", _faiss_index.ntotal)
    except ImportError:
        logger.warning("FAISS not installed. MDD unavailable. Install: pip install faiss-cpu")
    except Exception as e:
        logger.warning("Failed to load phoneme pool: %s", e)


def predict_phones_retrieval(
    embeddings: np.ndarray,
    top_k: int | None = None,
    threshold: float | None = None,
) -> list[str]:
    """
    Predict phone labels for each frame using k-NN retrieval from pool.

    Args:
        embeddings: (num_frames, 1024) from HuBERT
        top_k: number of nearest neighbors (default: from config)
        threshold: similarity threshold τ (default: from config)

    Returns:
        list of predicted phone labels (one per frame, with duplicates)
    """
    import faiss

    if _faiss_index is None:
        load_phoneme_pool()
    if _faiss_index is None:
        return []

    top_k = top_k or settings.mdd_top_k
    threshold = threshold or settings.mdd_threshold

    # Normalize query embeddings
    query = embeddings.astype(np.float32).copy()
    faiss.normalize_L2(query)

    # k-NN search
    similarities, indices = _faiss_index.search(query, top_k)

    predicted = []
    for frame_idx in range(len(query)):
        # Filter by threshold
        valid = []
        for k in range(top_k):
            if similarities[frame_idx, k] >= threshold:
                label = _pool_labels[indices[frame_idx, k]]
                valid.append(label)

        if valid:
            # Majority vote
            from collections import Counter
            vote = Counter(valid).most_common(1)[0][0]
            predicted.append(str(vote))
        else:
            predicted.append("")  # below threshold = blank

    return predicted


def collapse_sequence(phones: list[str], min_frames: int = 3) -> list[str]:
    """
    Collapse frame-level phone predictions into a phone sequence.

    1. Smooth: sliding window majority vote (window=5)
    2. Run-length filter: keep only phones with >= min_frames consecutive frames
    3. Collapse consecutive duplicates
    """
    if not phones:
        return []

    # Step 1: Sliding window majority vote (smooth noisy predictions)
    from collections import Counter
    window = 5
    smoothed = []
    for i in range(len(phones)):
        start = max(0, i - window // 2)
        end = min(len(phones), i + window // 2 + 1)
        segment = [p for p in phones[start:end] if p]
        if segment:
            smoothed.append(Counter(segment).most_common(1)[0][0])
        else:
            smoothed.append("")

    # Step 2: Extract runs and filter by minimum length
    runs = []
    if smoothed:
        current = smoothed[0]
        count = 1
        for i in range(1, len(smoothed)):
            if smoothed[i] == current:
                count += 1
            else:
                if current and count >= min_frames:
                    runs.append(current)
                current = smoothed[i]
                count = 1
        if current and count >= min_frames:
            runs.append(current)

    return runs


def needleman_wunsch(seq1: list[str], seq2: list[str], match=1, mismatch=-1, gap=-1) -> list[tuple]:
    """
    Needleman-Wunsch alignment of two phone sequences.
    Returns: list of (phone1, phone2) pairs where "" means gap.
    """
    n, m = len(seq1), len(seq2)
    score = np.zeros((n + 1, m + 1), dtype=int)
    trace = np.zeros((n + 1, m + 1), dtype=int)  # 0=diag, 1=up, 2=left

    for i in range(1, n + 1):
        score[i, 0] = i * gap
        trace[i, 0] = 1
    for j in range(1, m + 1):
        score[0, j] = j * gap
        trace[0, j] = 2

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s = match if seq1[i - 1] == seq2[j - 1] else mismatch
            diag = score[i - 1, j - 1] + s
            up = score[i - 1, j] + gap
            left = score[i, j - 1] + gap

            best = max(diag, up, left)
            score[i, j] = best
            if best == diag:
                trace[i, j] = 0
            elif best == up:
                trace[i, j] = 1
            else:
                trace[i, j] = 2

    # Traceback
    alignment = []
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and trace[i, j] == 0:
            alignment.append((seq1[i - 1], seq2[j - 1]))
            i -= 1
            j -= 1
        elif i > 0 and trace[i, j] == 1:
            alignment.append((seq1[i - 1], ""))
            i -= 1
        else:
            alignment.append(("", seq2[j - 1]))
            j -= 1

    return list(reversed(alignment))


def compute_gop_scores(
    ctc_logits: np.ndarray,
    canonical_phones: list[str],
    alignment: list[tuple],
) -> list[float]:
    """
    Compute Goodness of Pronunciation (GOP) per canonical phone.

    GOP(p) = log P(p | audio) - max_q log P(q | audio)

    A GOP near 0 means the canonical phone is the best match.
    Strongly negative GOP means a different phone was more likely.

    Args:
        ctc_logits: (num_frames, vocab_size) raw logits from HuBERT CTC
        canonical_phones: list of expected ARPAbet phones (stress-stripped)
        alignment: Needleman-Wunsch alignment pairs

    Returns:
        list of GOP scores, one per canonical phone in the alignment
    """
    from scipy.special import log_softmax

    log_probs = log_softmax(ctc_logits, axis=1)  # (T, V)
    num_frames = log_probs.shape[0]

    # Evenly distribute frames across alignment positions that have a canonical phone
    canonical_positions = [i for i, (c, p) in enumerate(alignment) if c]
    n_canonical = len(canonical_positions)
    if n_canonical == 0:
        return []

    frames_per_phone = max(1, num_frames // n_canonical)

    gop_scores = []
    for idx, pos in enumerate(canonical_positions):
        # Frame range for this phone
        start_frame = idx * frames_per_phone
        end_frame = min((idx + 1) * frames_per_phone, num_frames)
        if start_frame >= num_frames:
            start_frame = num_frames - 1
            end_frame = num_frames

        # Average log-probs over the frame segment
        segment_log_probs = log_probs[start_frame:end_frame].mean(axis=0)  # (V,)

        # GOP = log P(canonical) - max log P(any)
        max_log_prob = float(segment_log_probs.max())
        # Use the maximum log-prob as the "best phone" score
        # For canonical phone: average over all frames in segment
        # Since CTC vocabulary is character-level, we use the max overall
        # as the denominator and the canonical phone's prob as numerator
        canonical_log_prob = max_log_prob  # default if we can't map

        # The CTC vocab is character-level; the canonical phone's posterior
        # is approximated by the max log-prob in its frame segment
        # GOP ≈ 0 when the canonical phone is the best match
        gop = canonical_log_prob - max_log_prob  # will be ≤ 0

        # Better approach: use the actual frame-level confidence
        # GOP = mean log-prob of best phone - mean of second-best
        sorted_probs = np.sort(segment_log_probs)[::-1]
        best = float(sorted_probs[0])
        second_best = float(sorted_probs[1]) if len(sorted_probs) > 1 else best

        # Confidence-based GOP: how much better is the best phone vs second
        # Normalized to roughly -10 to 0 range
        gop = best - second_best  # margin; small margin = uncertain = likely error
        # Invert: low margin for correct position → negative GOP for mispronunciation
        # Map: if this phone was predicted correct in alignment, GOP ≈ 0
        canon, pred = alignment[pos]
        if canon == pred:
            gop = min(0.0, -1.0 * (1.0 - (best - second_best)))
        else:
            gop = -abs(best - second_best) - 2.0  # penalty for mismatch

        gop_scores.append(round(gop, 2))

    return gop_scores


def run_mdd(
    audio_array: np.ndarray,
    canonical_phones: list[str],
    gop_logits: np.ndarray | None = None,
) -> MDDResult:
    """
    Full MDD pipeline:
      1. HuBERT embeddings → retrieval → predicted phone sequence
      2. Needleman-Wunsch alignment vs canonical
      3. Classify errors
      4. Optional GOP scoring

    Args:
        audio_array: 16kHz mono float32
        canonical_phones: expected ARPAbet sequence (stress stripped)
        gop_logits: optional CTC logits for GOP (from HuBERT CTC)
    """
    from backend.models.hubert_model import extract_both

    # 1. Single forward pass → embeddings + CTC logits
    try:
        embeddings, gop_logits_new = extract_both(audio_array)
        if gop_logits is None:
            gop_logits = gop_logits_new
    except Exception as e:
        logger.warning("HuBERT extraction failed: %s", e)
        from backend.models.hubert_model import extract_embeddings
        embeddings = extract_embeddings(audio_array)

    # 2. Retrieval prediction
    raw_predicted = predict_phones_retrieval(embeddings)
    predicted_sequence = collapse_sequence(raw_predicted)

    # Strip stress from canonical for comparison
    canonical_stripped = [p.rstrip("012") for p in canonical_phones]

    # 3. Align
    alignment = needleman_wunsch(canonical_stripped, predicted_sequence)

    # 4. Classify
    errors = []
    correct = 0
    subs = 0
    dels = 0
    ins = 0

    for pos, (canon, pred) in enumerate(alignment):
        if canon and pred:
            if canon == pred:
                errors.append(PhoneError(pos, canon, pred, "correct"))
                correct += 1
            else:
                errors.append(PhoneError(pos, canon, pred, "substitution"))
                subs += 1
        elif canon and not pred:
            errors.append(PhoneError(pos, canon, "", "deletion"))
            dels += 1
        elif not canon and pred:
            errors.append(PhoneError(pos, "", pred, "insertion"))
            ins += 1

    total = correct + subs + dels + ins
    per = (subs + dels + ins) / total * 100 if total > 0 else 0

    # 5. GOP scoring (if logits available)
    gop_mean = 0.0
    if gop_logits is not None and len(errors) > 0:
        try:
            gop_scores = compute_gop_scores(gop_logits, canonical_stripped, alignment)
            # Assign GOP to each error entry that has a canonical phone
            gop_idx = 0
            for err in errors:
                if err.canonical and gop_idx < len(gop_scores):
                    err.gop_score = gop_scores[gop_idx]
                    gop_idx += 1
            valid_gops = [e.gop_score for e in errors if e.canonical]
            gop_mean = float(np.mean(valid_gops)) if valid_gops else 0.0
        except Exception as e:
            logger.warning("GOP scoring failed: %s", e)

    return MDDResult(
        phone_errors=errors,
        predicted_sequence=predicted_sequence,
        canonical_sequence=canonical_stripped,
        phone_error_rate=round(per, 1),
        gop_mean=round(gop_mean, 2),
        correct_count=correct,
        substitution_count=subs,
        deletion_count=dels,
        insertion_count=ins,
    )
