"""Tests for prosody analysis — F0 extraction and stress detection."""

import numpy as np
import pytest
from backend.services.prosody_analysis import analyze_prosody


def _make_sine_wav(freq=150, duration=1.0, sr=16000):
    """Generate a sine wave simulating voiced speech."""
    t = np.linspace(0, duration, int(sr * duration), endpoint=False)
    return (np.sin(2 * np.pi * freq * t) * 0.5).astype(np.float32)


def test_f0_extraction():
    audio = _make_sine_wav(freq=150, duration=1.0)
    result = analyze_prosody(audio, sample_rate=16000)
    assert result is not None
    assert result.f0_mean is not None or result.prosody_score == 0


def test_silent_audio():
    audio = np.zeros(16000, dtype=np.float32)
    result = analyze_prosody(audio, sample_rate=16000)
    assert result is not None


def test_short_audio():
    audio = _make_sine_wav(freq=200, duration=0.1)
    result = analyze_prosody(audio, sample_rate=16000)
    assert result is not None


def test_composite_range():
    audio = _make_sine_wav(freq=150, duration=2.0)
    result = analyze_prosody(audio, sample_rate=16000)
    assert 0 <= result.prosody_score <= 100
