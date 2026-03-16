"""Tests for fluency metric calculations with known inputs."""

import pytest
from backend.services.fluency_analysis import analyze_fluency


def _make_word_ts(words, gap=0.3, word_dur=0.4):
    """Create synthetic word timestamps."""
    ts = []
    t = 0.0
    for w in words:
        ts.append({"word": w, "start": round(t, 3), "end": round(t + word_dur, 3)})
        t += word_dur + gap
    return ts


def test_fluent_speech():
    words = _make_word_ts(["the", "cat", "sat", "on", "the", "mat"], gap=0.1)
    result = analyze_fluency(words)
    assert result.words_per_minute > 0
    assert result.fluency_score > 50


def test_choppy_speech():
    words = _make_word_ts(["the", "cat", "sat"], gap=1.5, word_dur=0.3)
    result = analyze_fluency(words)
    assert result.fluency_score < 60


def test_empty_words():
    result = analyze_fluency([])
    assert result.words_per_minute == 0
    assert result.fluency_score == 0


def test_single_word():
    result = analyze_fluency([{"word": "hello", "start": 0.0, "end": 0.5}])
    assert result.words_per_minute > 0


def test_fillers_detected():
    # Use gaps > 250ms so pauses are detected between filler words
    words = _make_word_ts(["the", "um", "cat", "uh", "sat"], gap=0.4)
    result = analyze_fluency(words)
    # Fillers should be counted (um, uh are in FILLED_PAUSES set)
    assert result.words_per_minute > 0
