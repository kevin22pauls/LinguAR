from __future__ import annotations

"""
Sentence bank service — JSON-based sentence selection with phoneme-targeted filtering.

Replaces the Ollama LLM runtime dependency with pre-generated sentence banks.
Supports single-object sentences, multi-object scene descriptions, and dialogues.
"""

import json
import logging
import random
from functools import lru_cache
from pathlib import Path

logger = logging.getLogger(__name__)

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

# Level mapping: old CEFR codes → new level names
_LEVEL_MAP = {
    "A1": "beginner",
    "A2": "elementary",
    "B1": "intermediate",
    "B2": "upper_intermediate",
    "C1": "advanced",
    "C2": "advanced",
}

VALID_LEVELS = {"beginner", "elementary", "intermediate", "upper_intermediate", "advanced"}


def _normalize_level(difficulty: str) -> str:
    """Map CEFR codes or raw level names to canonical level names."""
    if difficulty in VALID_LEVELS:
        return difficulty
    return _LEVEL_MAP.get(difficulty.upper(), "beginner")


@lru_cache(maxsize=1)
def _load_sentence_bank() -> dict:
    path = DATA_DIR / "sentence_bank.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)


@lru_cache(maxsize=1)
def _load_dialogue_bank() -> dict:
    path = DATA_DIR / "dialogue_bank.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)


@lru_cache(maxsize=1)
def _load_scene_templates() -> dict:
    path = DATA_DIR / "scene_templates.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _filter_by_phonemes(
    sentences: list[dict],
    problem_phonemes: list[str] | None,
) -> list[dict]:
    """
    Filter and rank sentences by overlap with the learner's problem phonemes.
    Returns all sentences if no problem phonemes provided, otherwise returns
    sentences sorted by relevance (most overlapping phonemes first).
    """
    if not problem_phonemes:
        return sentences

    problem_set = set(problem_phonemes)
    scored = []
    for entry in sentences:
        target = set(entry.get("target_phonemes", []))
        overlap = len(target & problem_set)
        scored.append((overlap, entry))

    # Sort descending by overlap count
    scored.sort(key=lambda x: x[0], reverse=True)

    # Return sentences that have at least 1 overlap, or all if none match
    filtered = [entry for overlap, entry in scored if overlap > 0]
    return filtered if filtered else sentences


async def generate_sentence(
    object_name: str,
    difficulty: str = "beginner",
    context: str = "",
    problem_phonemes: list[str] | None = None,
) -> str:
    """
    Select a practice sentence from the sentence bank.

    Args:
        object_name: The detected object (bottle, remote, person).
        difficulty: Level name or CEFR code.
        problem_phonemes: Learner's problem phonemes (ARPAbet) for filtering.

    Returns:
        A sentence string.
    """
    level = _normalize_level(difficulty)
    bank = _load_sentence_bank()

    obj_key = object_name.lower().strip()
    if obj_key not in bank:
        # Fallback: generic sentence
        return f"I can see a {object_name}."

    level_sentences = bank[obj_key].get(level)
    if not level_sentences:
        # Try beginner as fallback
        level_sentences = bank[obj_key].get("beginner", [])

    if not level_sentences:
        return f"I can see a {object_name}."

    candidates = _filter_by_phonemes(level_sentences, problem_phonemes)

    # Pick randomly from top candidates (top 5 by phoneme overlap, or all)
    top = candidates[:5] if problem_phonemes else candidates
    chosen = random.choice(top)
    return chosen["sentence"]


def get_dialogue(
    object_name: str,
    difficulty: str = "beginner",
) -> dict | None:
    """
    Get a dialogue for conversation scaffolding mode.

    Returns: {id, turns: [{speaker, line}, ...]} or None.
    """
    level = _normalize_level(difficulty)
    bank = _load_dialogue_bank()

    obj_key = object_name.lower().strip()
    if obj_key not in bank:
        return None

    dialogues = bank[obj_key].get(level)
    if not dialogues:
        return None

    return random.choice(dialogues)


def get_scene_templates() -> dict:
    """Return the loaded scene templates."""
    return _load_scene_templates()
