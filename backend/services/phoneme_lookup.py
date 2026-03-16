from __future__ import annotations

"""
Phoneme lookup — CMUdict with g2p-en fallback for OOV words.
All output is ARPAbet (no IPA conversion).
"""

import re
from functools import lru_cache
from nltk.corpus import cmudict
from g2p_en import G2p

# Load CMUdict once
_cmudict = cmudict.dict()
_g2p = G2p()

# Strip stress digits for comparison (e.g. 'AE1' → 'AE')
_STRESS_RE = re.compile(r"\d$")


def strip_stress(phone: str) -> str:
    """Remove stress marker from ARPAbet phone: 'AE1' → 'AE'."""
    return _STRESS_RE.sub("", phone)


def get_phonemes(word: str) -> list[str]:
    """
    Return ARPAbet phoneme list for a single word.
    Uses CMUdict first, falls back to g2p-en for OOV words.
    Returns first pronunciation variant from CMUdict.
    """
    w = word.lower().strip()
    if w in _cmudict:
        return list(_cmudict[w][0])  # first pronunciation variant

    # g2p-en fallback — returns a mix of ARPAbet phones and graphemes
    raw = _g2p(w)
    # Filter: g2p-en returns single chars for graphemes, ARPAbet phones are 2+ chars or known singles
    phones = [p for p in raw if len(p) >= 2 or p in (" ",)]
    # Remove any space tokens
    return [p for p in phones if p.strip()]


def get_phonemes_for_sentence(text: str) -> list[list[str]]:
    """
    Return per-word phoneme lists for a sentence.
    Filters out punctuation-only tokens.
    """
    words = re.findall(r"[a-zA-Z']+", text)
    return [get_phonemes(w) for w in words]


def get_stressed_vowel_index(phones: list[str]) -> int | None:
    """
    Return the index of the primary-stressed vowel (marked with '1') in a phone list.
    Returns None if no stress marker found.
    """
    for i, p in enumerate(phones):
        if p.endswith("1"):
            return i
    return None


@lru_cache(maxsize=4096)
def get_phonemes_cached(word: str) -> tuple[str, ...]:
    """Cached version returning a tuple (hashable)."""
    return tuple(get_phonemes(word))
