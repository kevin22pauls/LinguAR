from __future__ import annotations

"""
Minimal pair targeting.

Detects phoneme confusions from MDD results and generates practice sentences
containing minimal pair words that target those specific contrasts.
"""

import json
import logging
import random
from pathlib import Path

from backend.config import DATA_DIR

logger = logging.getLogger(__name__)

_pairs_data = None


def _load_pairs():
    global _pairs_data
    if _pairs_data is not None:
        return

    path = DATA_DIR / "minimal_pairs.json"
    if path.exists():
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        _pairs_data = data.get("pairs", {})
    else:
        logger.warning("Minimal pairs data not found at %s", path)
        _pairs_data = {}


def get_contrast_key(phone_a: str, phone_b: str) -> str | None:
    """Find the minimal pair contrast key for two phonemes (order-independent)."""
    _load_pairs()
    a = phone_a.rstrip("012").upper()
    b = phone_b.rstrip("012").upper()

    forward = f"{a}-{b}"
    reverse = f"{b}-{a}"

    if forward in _pairs_data:
        return forward
    if reverse in _pairs_data:
        return reverse
    return None


def get_minimal_pairs(phone_a: str, phone_b: str) -> list[str]:
    """Return minimal pair word entries (e.g. 'right/light') for a contrast."""
    _load_pairs()
    key = get_contrast_key(phone_a, phone_b)
    if key is None:
        return []
    return _pairs_data.get(key, [])


def detect_confusions(phone_errors: list) -> list[dict]:
    """
    Detect phoneme confusions from MDD results.
    phone_errors: list of PhoneError from mdd_engine.
    Returns list of {canonical, actual, contrast_key, count}.
    """
    _load_pairs()
    confusion_counts = {}

    for err in phone_errors:
        if err.error_type != "substitution":
            continue
        canonical = err.canonical.rstrip("012").upper() if err.canonical else None
        actual = err.actual.rstrip("012").upper() if err.actual else None
        if not canonical or not actual:
            continue

        key = get_contrast_key(canonical, actual)
        if key is None:
            continue

        pair_key = (canonical, actual)
        if pair_key not in confusion_counts:
            confusion_counts[pair_key] = {
                "canonical": canonical,
                "actual": actual,
                "contrast_key": key,
                "count": 0,
            }
        confusion_counts[pair_key]["count"] += 1

    # Sort by frequency
    return sorted(confusion_counts.values(), key=lambda x: x["count"], reverse=True)


def generate_minimal_pair_sentence(contrast_key: str, difficulty: str = "A2") -> dict:
    """
    Generate a practice sentence using a minimal pair from the given contrast.
    Returns {word_a, word_b, sentence_a, sentence_b, contrast_key}.
    """
    _load_pairs()
    pairs = _pairs_data.get(contrast_key, [])
    if not pairs:
        return {}

    pair_str = random.choice(pairs)
    parts = pair_str.split("/")
    if len(parts) != 2:
        return {}

    word_a, word_b = parts[0].strip(), parts[1].strip()

    # Simple sentence templates by difficulty
    templates = {
        "A1": [
            "I can see a {word}.",
            "This is a {word}.",
            "I have a {word}.",
        ],
        "A2": [
            "Please give me the {word}.",
            "Can you find the {word}?",
            "I want to {word} it.",
            "The {word} is on the table.",
        ],
        "B1": [
            "She noticed the {word} on the shelf.",
            "They decided to {word} the project.",
            "He picked up the {word} carefully.",
        ],
        "B2": [
            "The {word} was essential for the experiment.",
            "After consideration, they chose to {word} immediately.",
            "It was difficult to distinguish the {word} from the rest.",
        ],
    }

    level_templates = templates.get(difficulty, templates["A2"])
    template = random.choice(level_templates)

    return {
        "word_a": word_a,
        "word_b": word_b,
        "sentence_a": template.format(word=word_a),
        "sentence_b": template.format(word=word_b),
        "contrast_key": contrast_key,
    }


def get_targeted_pairs(
    phone_errors: list,
    predicted_difficult: list[str] | None = None,
    max_pairs: int = 3,
) -> list[dict]:
    """
    Get minimal pair exercises targeting the learner's weakest contrasts.
    Combines MDD confusion data with L1 predictions.
    """
    _load_pairs()

    # Detected confusions from actual performance
    confusions = detect_confusions(phone_errors)
    targeted = []

    # Add pairs from detected confusions
    for conf in confusions[:max_pairs]:
        pair_data = generate_minimal_pair_sentence(conf["contrast_key"])
        if pair_data:
            pair_data["source"] = "detected"
            pair_data["confusion_count"] = conf["count"]
            targeted.append(pair_data)

    # Fill remaining slots from L1 predictions
    if predicted_difficult and len(targeted) < max_pairs:
        used_keys = {t["contrast_key"] for t in targeted}
        for phoneme in predicted_difficult:
            if len(targeted) >= max_pairs:
                break
            # Find contrasts involving this phoneme
            for key in _pairs_data:
                if key in used_keys:
                    continue
                phones = key.split("-")
                if phoneme.upper() in phones:
                    pair_data = generate_minimal_pair_sentence(key)
                    if pair_data:
                        pair_data["source"] = "l1_predicted"
                        pair_data["confusion_count"] = 0
                        targeted.append(pair_data)
                        used_keys.add(key)
                        break

    return targeted
