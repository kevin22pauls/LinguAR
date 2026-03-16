"""Tests for articulatory distance matrix."""

import pytest
from backend.services.phoneme_features import articulatory_distance


def test_identical_phones():
    dist = articulatory_distance("P", "P")
    assert dist == 0.0


def test_voicing_contrast():
    """P/B differ only in voicing."""
    dist = articulatory_distance("P", "B")
    assert 0 < dist < 0.5


def test_large_distance():
    """S and UW are very different (consonant vs vowel)."""
    dist = articulatory_distance("S", "UW")
    assert dist > 0.5


def test_similar_consonants():
    """T and D are very similar (same place/manner, different voicing)."""
    dist_td = articulatory_distance("T", "D")
    dist_ts = articulatory_distance("T", "S")
    assert dist_td < dist_ts


def test_vowel_pair():
    """IY and IH are close vowels."""
    dist = articulatory_distance("IY", "IH")
    assert dist < 0.5


def test_unknown_phone():
    dist = articulatory_distance("XX", "YY")
    assert dist == 1.0
