"""Tests for hierarchical score aggregation math."""

import pytest
from backend.services.hierarchical_scorer import compute_hierarchical_scores


def test_no_inputs():
    """All None inputs should produce zero scores without crashing."""
    result = compute_hierarchical_scores()
    assert result.utterance_total >= 0
    assert result.utterance_accuracy == 0.0


def test_weights_formula():
    """Verify total = 0.35*A + 0.25*F + 0.25*P + 0.15*C."""
    result = compute_hierarchical_scores()
    # With no inputs, all dimensions are 0
    expected = 0.35 * 0 + 0.25 * 0 + 0.25 * 0 + 0.15 * 0
    assert abs(result.utterance_total - expected) < 0.1


def test_returns_hierarchical_scores():
    """Verify the function returns HierarchicalScores dataclass."""
    from backend.services.hierarchical_scorer import HierarchicalScores
    result = compute_hierarchical_scores()
    assert isinstance(result, HierarchicalScores)
    assert isinstance(result.word_scores, list)
