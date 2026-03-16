from __future__ import annotations

"""
Intelligibility scoring — FL-weighted pronunciation assessment with L1 awareness.

Each phoneme error is weighted by the functional load (communicative importance)
of the phoneme pair involved. High-FL errors (e.g., /r/-/l/) penalize more than
low-FL errors (e.g., /θ/-/s/).

L1-aware adjustment: expected substitution patterns for the learner's L1 receive
a reduced penalty. These are accent features that don't impede intelligibility
(e.g., Tamil speakers: TH→T, F→P, W→V).
"""

import json
import logging
from pathlib import Path

from backend.config import DATA_DIR, settings
from backend.services.phoneme_features import articulatory_distance

logger = logging.getLogger(__name__)

_fl_data = None
_l1_expected_subs: dict[tuple[str, str], float] | None = None


def _load_fl():
    global _fl_data
    if _fl_data is not None:
        return

    fl_path = DATA_DIR / "functional_load.json"
    if fl_path.exists():
        with open(fl_path) as f:
            raw = json.load(f)
        _fl_data = {}
        for section in ("consonant_pairs", "vowel_pairs"):
            for pair, value in raw.get(section, {}).items():
                p1, p2 = pair.split("-")
                _fl_data[(p1, p2)] = value
                _fl_data[(p2, p1)] = value  # symmetric
    else:
        logger.warning("functional_load.json not found at %s", fl_path)
        _fl_data = {}


def _load_l1_substitutions():
    """Load expected substitution patterns for the configured L1."""
    global _l1_expected_subs
    if _l1_expected_subs is not None:
        return

    _l1_expected_subs = {}

    path = DATA_DIR / "l1_transfer_profiles.json"
    if not path.exists():
        return

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    profiles = data.get("profiles", {})
    lang = settings.default_l1.lower()
    profile = profiles.get(lang)
    if not profile:
        return

    for pattern in profile.get("substitution_patterns", []):
        target = pattern["target"]       # canonical (expected) phone
        likely = pattern["likely_sub"]   # what the learner will say instead
        if target and likely:
            # Penalty reduction factor: 0.3 means only 30% of normal penalty
            _l1_expected_subs[(target, likely)] = 0.3
            logger.info("L1 expected substitution: %s → %s (penalty ×0.3)", target, likely)


def get_functional_load(phone1: str, phone2: str) -> float:
    """
    Get functional load weight for a phoneme pair.
    Returns 0.0-1.0, default 0.3 for unknown pairs.
    """
    _load_fl()
    p1 = phone1.rstrip("012")
    p2 = phone2.rstrip("012")
    if p1 == p2:
        return 0.0
    return _fl_data.get((p1, p2), 0.3)


def is_l1_expected(canonical: str, predicted: str) -> tuple[bool, float]:
    """
    Check if a substitution is an expected L1 transfer pattern.
    Returns (is_expected, penalty_factor).
    penalty_factor = 0.3 for expected patterns, 1.0 otherwise.
    """
    _load_l1_substitutions()
    c = canonical.rstrip("012")
    p = predicted.rstrip("012")
    factor = _l1_expected_subs.get((c, p), 1.0)
    return factor < 1.0, factor


def score_phone_error(canonical: str, predicted: str) -> dict:
    """
    Score a single phone error with FL weighting and L1 adjustment.
    Returns dict with severity, fl_weight, weighted_score, l1_expected.
    """
    if canonical == predicted or canonical.rstrip("012") == predicted.rstrip("012"):
        return {"severity": 0.0, "fl_weight": 0.0, "weighted_score": 0.0,
                "error_type": "correct", "l1_expected": False}

    art_dist = articulatory_distance(canonical, predicted)
    fl = get_functional_load(canonical, predicted)
    l1_expected, l1_factor = is_l1_expected(canonical, predicted)

    # Severity = articulatory distance * FL weight * L1 factor
    severity = art_dist * (0.5 + 0.5 * fl) * l1_factor
    weighted_score = severity * fl

    return {
        "severity": round(severity, 3),
        "fl_weight": round(fl, 3),
        "weighted_score": round(weighted_score, 3),
        "error_type": "substitution",
        "l1_expected": l1_expected,
    }


def compute_intelligibility_score(phone_errors: list) -> float:
    """
    Compute overall intelligibility score (0-100) from phone errors.
    L1-expected substitutions receive reduced penalty.
    phone_errors: list of PhoneError from mdd_engine.
    """
    _load_fl()
    _load_l1_substitutions()

    if not phone_errors:
        return 100.0

    total_weight = 0.0
    error_weight = 0.0

    for err in phone_errors:
        if err.error_type == "correct":
            total_weight += 1.0
        elif err.error_type == "substitution":
            fl = get_functional_load(err.canonical, err.predicted)
            _, l1_factor = is_l1_expected(err.canonical, err.predicted)
            penalty = articulatory_distance(err.canonical, err.predicted) * (0.5 + 0.5 * fl) * l1_factor
            error_weight += penalty
            total_weight += 1.0
        elif err.error_type == "deletion":
            error_weight += 0.8  # deletions are severe
            total_weight += 1.0
        elif err.error_type == "insertion":
            error_weight += 0.3  # insertions are less severe
            total_weight += 0.5

    if total_weight <= 0:
        return 100.0

    raw_score = max(0, 1 - error_weight / total_weight) * 100
    return round(raw_score, 1)
