"""Tests for jiwer reading accuracy alignment."""

from backend.services.reading_accuracy import analyze_reading


def test_perfect_match():
    result = analyze_reading("the cat sat on the mat", "the cat sat on the mat")
    assert result.accuracy == 100.0
    assert result.wer == 0.0


def test_substitution():
    result = analyze_reading("the cat sat", "the cat set")
    assert result.accuracy < 100
    labels = [a.label for a in result.alignments]
    assert "S" in labels


def test_deletion():
    result = analyze_reading("the cat sat on the mat", "the cat on the mat")
    labels = [a.label for a in result.alignments]
    assert "D" in labels


def test_insertion():
    result = analyze_reading("the cat", "the big cat")
    labels = [a.label for a in result.alignments]
    assert "I" in labels


def test_empty_hypothesis():
    result = analyze_reading("the cat sat", "")
    assert result.accuracy == 0.0


def test_empty_reference():
    result = analyze_reading("", "the cat sat")
    assert result is not None
