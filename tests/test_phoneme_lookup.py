"""Tests for CMUdict + g2p-en phoneme lookup."""

import pytest
from backend.services.phoneme_lookup import get_phonemes, get_phonemes_for_sentence


def test_common_word():
    phones = get_phonemes("cat")
    assert phones == ["K", "AE1", "T"]


def test_case_insensitive():
    assert get_phonemes("Cat") == get_phonemes("cat")


def test_multi_syllable():
    phones = get_phonemes("computer")
    assert len(phones) >= 6
    assert "K" in phones


def test_g2p_fallback():
    """OOV word should fall back to g2p-en without crashing."""
    phones = get_phonemes("kerfuffle")
    assert len(phones) > 0


def test_sentence():
    result = get_phonemes_for_sentence("the cat sat")
    assert len(result) == 3
    assert result[1] == ["K", "AE1", "T"]


def test_empty_string():
    result = get_phonemes("")
    assert isinstance(result, list)


def test_nonexistent_word():
    phones = get_phonemes("zzyzx")
    assert isinstance(phones, list)
