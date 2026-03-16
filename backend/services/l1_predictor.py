"""
L1 transfer error prediction.

Loads L1 profiles and predicts which English phonemes will be difficult
for a learner based on their native language. Predictions are validated
against actual performance over time.
"""

import json
import logging
from pathlib import Path

from sqlalchemy.orm import Session

from backend.config import DATA_DIR
from backend.database.schema import L1TransferPrediction, LearnerProfile

logger = logging.getLogger(__name__)

_profiles = None


def _load_profiles():
    global _profiles
    if _profiles is not None:
        return

    path = DATA_DIR / "l1_transfer_profiles.json"
    if path.exists():
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        _profiles = data.get("profiles", {})
    else:
        logger.warning("L1 transfer profiles not found at %s", path)
        _profiles = {}


def get_supported_languages() -> list[dict]:
    """Return list of supported L1 languages."""
    _load_profiles()
    return [
        {"code": code, "name": prof["display_name"]}
        for code, prof in _profiles.items()
    ]


def get_predicted_difficulties(native_language: str) -> list[str]:
    """Return list of predicted difficult ARPAbet phonemes for the L1."""
    _load_profiles()
    lang_key = native_language.lower().replace(" ", "_").replace("/", "_")

    if lang_key in _profiles:
        return _profiles[lang_key]["predicted_difficult"]

    # Try partial match
    for key, prof in _profiles.items():
        if lang_key in key or key in lang_key:
            return prof["predicted_difficult"]

    return []


def get_substitution_patterns(native_language: str) -> list[dict]:
    """Return common substitution patterns for the L1."""
    _load_profiles()
    lang_key = native_language.lower().replace(" ", "_").replace("/", "_")

    for key, prof in _profiles.items():
        if lang_key == key or lang_key in key or key in lang_key:
            return prof.get("substitution_patterns", [])
    return []


def initialize_predictions(db: Session, learner_id: str, native_language: str):
    """
    Create L1 transfer predictions for a new learner.
    Called during onboarding when learner sets their native language.
    """
    predictions = get_predicted_difficulties(native_language)
    if not predictions:
        return

    for phoneme in predictions:
        existing = (
            db.query(L1TransferPrediction)
            .filter_by(learner_id=learner_id, phoneme=phoneme)
            .first()
        )
        if not existing:
            db.add(L1TransferPrediction(
                learner_id=learner_id,
                phoneme=phoneme,
                predicted_difficult=True,
                actual_accuracy=None,
                confirmed=None,
            ))

    db.commit()
    logger.info("Initialized %d L1 predictions for learner %s (L1: %s)",
                len(predictions), learner_id, native_language)


def update_prediction(db: Session, learner_id: str, phoneme: str, accuracy: float):
    """
    Update actual accuracy for a predicted phoneme.
    After 5+ observations, confirm or reject the prediction.
    """
    pred = (
        db.query(L1TransferPrediction)
        .filter_by(learner_id=learner_id, phoneme=phoneme)
        .first()
    )
    if not pred:
        return

    # Running average
    if pred.actual_accuracy is None:
        pred.actual_accuracy = accuracy
    else:
        pred.actual_accuracy = pred.actual_accuracy * 0.7 + accuracy * 0.3

    # Confirm/reject after enough data (threshold: 70% accuracy = not difficult)
    if pred.actual_accuracy is not None:
        if pred.actual_accuracy < 70:
            pred.confirmed = True   # prediction was correct — phoneme IS difficult
        elif pred.actual_accuracy >= 85:
            pred.confirmed = False  # prediction was wrong — phoneme is fine

    db.commit()


def get_predictions_with_actuals(db: Session, learner_id: str) -> list[dict]:
    """Return all predictions with actual accuracy for dashboard display."""
    preds = (
        db.query(L1TransferPrediction)
        .filter_by(learner_id=learner_id)
        .all()
    )
    return [
        {
            "phoneme": p.phoneme,
            "predicted_difficult": p.predicted_difficult,
            "actual_accuracy": round(p.actual_accuracy, 1) if p.actual_accuracy is not None else None,
            "confirmed": p.confirmed,
        }
        for p in preds
    ]
