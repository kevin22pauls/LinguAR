"""Tests for retrieval MDD — Needleman-Wunsch alignment."""

import numpy as np
import pytest
from backend.services.mdd_engine import needleman_wunsch


def test_nw_identical():
    canonical = ["K", "AE", "T"]
    predicted = ["K", "AE", "T"]
    alignment = needleman_wunsch(canonical, predicted)
    assert all(a == b for a, b in alignment)


def test_nw_substitution():
    canonical = ["K", "AE", "T"]
    predicted = ["K", "EH", "T"]
    alignment = needleman_wunsch(canonical, predicted)
    mismatches = [(a, b) for a, b in alignment if a != b and a != "" and b != ""]
    assert len(mismatches) >= 1
    assert ("AE", "EH") in mismatches


def test_nw_deletion():
    canonical = ["K", "AE", "T"]
    predicted = ["K", "T"]
    alignment = needleman_wunsch(canonical, predicted)
    deletions = [(a, b) for a, b in alignment if b == "" and a != ""]
    assert len(deletions) >= 1


def test_nw_insertion():
    canonical = ["K", "AE", "T"]
    predicted = ["K", "AE", "S", "T"]
    alignment = needleman_wunsch(canonical, predicted)
    insertions = [(a, b) for a, b in alignment if a == "" and b != ""]
    assert len(insertions) >= 1


def test_nw_empty_canonical():
    alignment = needleman_wunsch([], ["K", "AE"])
    assert all(a == "" for a, b in alignment)
    assert len(alignment) == 2


def test_nw_empty_predicted():
    alignment = needleman_wunsch(["K", "AE", "T"], [])
    assert all(b == "" for a, b in alignment)
    assert len(alignment) == 3
