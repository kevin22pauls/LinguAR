from __future__ import annotations

"""
Spaced repetition engine — SM-2 algorithm applied to phoneme-level practice.

Each phoneme the learner struggles with gets scheduled for review.
Due phonemes are injected into the prompt generator for targeted practice.
"""

import logging
from datetime import datetime, timedelta, date

from sqlalchemy.orm import Session

from backend.database.schema import SpacedRepetitionQueue

logger = logging.getLogger(__name__)

# Map pronunciation score (0-100) to SM-2 quality (0-5)
def _score_to_quality(score: float) -> int:
    if score >= 90:
        return 5
    elif score >= 75:
        return 4
    elif score >= 60:
        return 3
    elif score >= 40:
        return 2
    elif score >= 20:
        return 1
    return 0


def update_phoneme(db: Session, learner_id: str, phoneme: str, score: float):
    """
    Update spaced repetition schedule for a phoneme after assessment.
    Uses SM-2 algorithm.
    """
    quality = _score_to_quality(score)

    entry = (
        db.query(SpacedRepetitionQueue)
        .filter_by(learner_id=learner_id, phoneme=phoneme)
        .first()
    )

    if not entry:
        entry = SpacedRepetitionQueue(
            learner_id=learner_id,
            phoneme=phoneme,
            interval_days=1,
            due_date=date.today() + timedelta(days=1),
            easiness_factor=2.5,
            repetitions=0,
            last_score=score,
            last_reviewed=datetime.utcnow(),
        )
        db.add(entry)
    else:
        entry.last_score = score
        entry.last_reviewed = datetime.utcnow()

    # SM-2 algorithm
    if quality >= 3:  # passing
        if entry.repetitions == 0:
            interval = 1
        elif entry.repetitions == 1:
            interval = 3
        else:
            interval = entry.interval_days * entry.easiness_factor
        entry.repetitions += 1
    else:  # failing — reset
        entry.repetitions = 0
        interval = 1

    # Update easiness factor
    ef = entry.easiness_factor + 0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)
    entry.easiness_factor = max(1.3, ef)

    entry.interval_days = round(interval, 1)
    entry.due_date = date.today() + timedelta(days=interval)

    db.commit()


def get_due_phonemes(db: Session, learner_id: str, limit: int = 5) -> list[dict]:
    """
    Get phonemes due for review (overdue first, then soonest).
    Returns list of {phoneme, due_date, last_score, days_overdue}.
    """
    today = date.today()
    entries = (
        db.query(SpacedRepetitionQueue)
        .filter_by(learner_id=learner_id)
        .filter(SpacedRepetitionQueue.due_date <= today)
        .order_by(SpacedRepetitionQueue.due_date.asc())
        .limit(limit)
        .all()
    )

    return [
        {
            "phoneme": e.phoneme,
            "due_date": e.due_date.isoformat() if e.due_date else None,
            "last_score": round(e.last_score, 1) if e.last_score else None,
            "days_overdue": (today - e.due_date).days if e.due_date else 0,
            "repetitions": e.repetitions,
        }
        for e in entries
    ]


def get_all_phoneme_schedules(db: Session, learner_id: str) -> list[dict]:
    """Get all phoneme schedules for dashboard display."""
    entries = (
        db.query(SpacedRepetitionQueue)
        .filter_by(learner_id=learner_id)
        .order_by(SpacedRepetitionQueue.due_date.asc())
        .all()
    )

    today = date.today()
    return [
        {
            "phoneme": e.phoneme,
            "interval_days": e.interval_days,
            "due_date": e.due_date.isoformat() if e.due_date else None,
            "easiness_factor": round(e.easiness_factor, 2),
            "repetitions": e.repetitions,
            "last_score": round(e.last_score, 1) if e.last_score else None,
            "status": "overdue" if e.due_date and e.due_date <= today else "upcoming",
            "mastery": _mastery_level(e.last_score, e.repetitions),
        }
        for e in entries
    ]


def _mastery_level(score: float | None, repetitions: int) -> str:
    if score is None:
        return "new"
    if score >= 90 and repetitions >= 5:
        return "mastered"
    if score >= 75 and repetitions >= 3:
        return "practiced"
    if score >= 50:
        return "learning"
    return "struggling"


def update_from_mdd_results(db: Session, learner_id: str, phone_errors: list):
    """
    Batch update spaced repetition from MDD results.
    phone_errors: list of PhoneError from mdd_engine.
    """
    # Group by phoneme and compute average accuracy
    phoneme_scores = {}
    for err in phone_errors:
        phone = err.canonical.rstrip("012") if err.canonical else None
        if not phone:
            continue
        if phone not in phoneme_scores:
            phoneme_scores[phone] = {"correct": 0, "total": 0}
        phoneme_scores[phone]["total"] += 1
        if err.error_type == "correct":
            phoneme_scores[phone]["correct"] += 1

    for phone, counts in phoneme_scores.items():
        if counts["total"] > 0:
            accuracy = counts["correct"] / counts["total"] * 100
            update_phoneme(db, learner_id, phone, accuracy)
