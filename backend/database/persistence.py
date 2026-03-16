from __future__ import annotations

"""CRUD operations for LinguAR database."""

import json
from datetime import datetime, date
from collections import defaultdict
from sqlalchemy.orm import Session
from sqlalchemy import func

from backend.database.schema import (
    LearnerProfile, Recording, LearnerVocabulary, DailyProgress, SessionProgress,
    L1TransferPrediction, SpacedRepetitionQueue,
)


# ── Learner Profiles ─────────────────────────────────────────────────────────

def get_or_create_learner(db: Session, learner_id: str = "default") -> LearnerProfile:
    learner = db.query(LearnerProfile).filter_by(learner_id=learner_id).first()
    if not learner:
        learner = LearnerProfile(learner_id=learner_id, display_name="Learner")
        db.add(learner)
        db.commit()
        db.refresh(learner)
    return learner


# ── Recordings ────────────────────────────────────────────────────────────────

def save_recording(db: Session, **kwargs) -> Recording:
    rec = Recording(**kwargs)
    db.add(rec)
    db.commit()
    db.refresh(rec)
    return rec


def award_xp_and_streak(db: Session, learner_id: str, total_score: float | None) -> dict:
    """
    Award XP and update streak after a recording.

    XP formula:
      - Base: 10 XP per recording
      - Score bonus: total_score / 10 (0-10 XP)
      - Streak bonus: +2 XP per streak day (max +20)

    Streak: increments if last_active_date was yesterday, resets if > 1 day gap.
    Returns {xp_earned, xp_total, streak, streak_longest}.
    """
    learner = db.query(LearnerProfile).filter_by(learner_id=learner_id).first()
    if not learner:
        return {"xp_earned": 0, "xp_total": 0, "streak": 0, "streak_longest": 0}

    today = date.today()

    # Streak logic
    if learner.last_active_date:
        days_since = (today - learner.last_active_date).days
        if days_since == 1:
            learner.streak_current = (learner.streak_current or 0) + 1
        elif days_since > 1:
            learner.streak_current = 1
        # days_since == 0: same day, don't change streak
    else:
        learner.streak_current = 1

    learner.last_active_date = today
    if (learner.streak_current or 0) > (learner.streak_longest or 0):
        learner.streak_longest = learner.streak_current

    # XP calculation
    base_xp = 10
    score_bonus = int((total_score or 0) / 10)
    streak_bonus = min(20, (learner.streak_current or 0) * 2)
    xp_earned = base_xp + score_bonus + streak_bonus

    learner.xp_total = (learner.xp_total or 0) + xp_earned
    db.commit()

    return {
        "xp_earned": xp_earned,
        "xp_total": learner.xp_total,
        "streak": learner.streak_current,
        "streak_longest": learner.streak_longest,
    }


def get_recording(db: Session, recording_id: int) -> Recording | None:
    return db.query(Recording).filter_by(id=recording_id).first()


def get_learner_recordings(db: Session, learner_id: str, limit: int = 50) -> list[Recording]:
    return (
        db.query(Recording)
        .filter_by(learner_id=learner_id)
        .order_by(Recording.created_at.desc())
        .limit(limit)
        .all()
    )


def get_previous_recording_data(db: Session, learner_id: str) -> dict | None:
    """Get the most recent recording's key scores for improvement comparison."""
    rec = (
        db.query(Recording)
        .filter_by(learner_id=learner_id)
        .order_by(Recording.created_at.desc())
        .first()
    )
    if not rec:
        return None
    return {
        "accuracy": rec.utterance_accuracy,
        "fluency": rec.utterance_fluency,
        "prosody": rec.utterance_prosody,
        "completeness": rec.utterance_completeness,
        "total": rec.utterance_total,
        "words_per_minute": rec.words_per_minute,
        "mean_length_of_run": rec.mean_length_of_run,
        "stress_accuracy": rec.stress_accuracy,
        "intonation_accuracy": rec.intonation_accuracy,
        "filler_count": rec.filler_count,
        "repetition_count": rec.repetition_count,
    }


# ── Dashboard Aggregation ────────────────────────────────────────────────────

def get_dashboard_data(db: Session, learner_id: str) -> dict:
    """Return all data needed for the full learner dashboard (spec 3.7)."""
    learner = get_or_create_learner(db, learner_id)
    recordings = get_learner_recordings(db, learner_id, limit=200)

    if not recordings:
        return {
            "profile": _profile_dict(learner),
            "metric_cards": _empty_metric_cards(),
            "sessions": [],
            "total_recordings": 0,
            "phoneme_errors": [],
            "vocabulary": [],
            "l1_predictions": [],
            "wpm_trend": [],
        }

    # Sessions (chronological order for charts)
    sessions = []
    for rec in reversed(recordings):
        sessions.append({
            "id": rec.id,
            "date": rec.created_at.strftime("%Y-%m-%d") if rec.created_at else "",
            "time": rec.created_at.strftime("%H:%M") if rec.created_at else "",
            "object": rec.object_name or "",
            "sentence": rec.sentence_text or "",
            "accuracy": round(rec.utterance_accuracy or 0),
            "fluency": round(rec.utterance_fluency or 0),
            "prosody": round(rec.utterance_prosody or 0),
            "completeness": round(rec.utterance_completeness or 0),
            "total": round(rec.utterance_total or 0),
            "wpm": round(rec.words_per_minute or 0),
            "pronunciation_score": round(rec.pronunciation_score or 0),
        })

    # Metric cards
    recent = recordings[:10]  # most recent 10
    avg_acc = _safe_avg([r.utterance_accuracy for r in recent])
    avg_flu = _safe_avg([r.utterance_fluency for r in recent])
    avg_pro = _safe_avg([r.utterance_prosody for r in recent])
    avg_com = _safe_avg([r.utterance_completeness for r in recent])

    unique_objects = set()
    for r in recordings:
        if r.object_name:
            unique_objects.add(r.object_name)

    # Total practice time estimate (sum of session durations)
    total_minutes = len(recordings) * 0.5  # rough estimate: 30s per recording

    metric_cards = {
        "streak": learner.streak_current or 0,
        "xp": learner.xp_total or 0,
        "level": learner.current_level or "beginner",
        "objects_scanned": len(unique_objects),
        "total_recordings": len(recordings),
        "practice_minutes": round(total_minutes, 1),
        "avg_accuracy": round(avg_acc),
        "avg_fluency": round(avg_flu),
        "avg_prosody": round(avg_pro),
        "avg_completeness": round(avg_com),
        "avg_total": round(_safe_avg([
            r.utterance_total for r in recent
        ])),
    }

    # Phoneme error aggregation (from word_scores_json and problematic_phonemes_json)
    phoneme_errors = _aggregate_phoneme_errors(recordings)

    # Vocabulary mastery
    vocab_entries = (
        db.query(LearnerVocabulary)
        .filter_by(learner_id=learner_id)
        .order_by(LearnerVocabulary.last_practiced.desc())
        .limit(50)
        .all()
    )
    vocabulary = [{
        "word": v.word,
        "times_practiced": v.times_practiced,
        "avg_score": round(v.avg_pronunciation or 0),
        "mastery": v.mastery_level or "new",
        "object": v.detected_object or "",
    } for v in vocab_entries]

    # L1 predictions vs actuals
    l1_preds = (
        db.query(L1TransferPrediction)
        .filter_by(learner_id=learner_id)
        .all()
    )
    l1_predictions = [{
        "phoneme": p.phoneme,
        "predicted_difficult": p.predicted_difficult,
        "actual_accuracy": round(p.actual_accuracy or 0),
        "confirmed": p.confirmed,
    } for p in l1_preds]

    # WPM trend
    wpm_trend = [{
        "date": s["date"],
        "wpm": s["wpm"],
    } for s in sessions if s["wpm"] > 0]

    return {
        "profile": _profile_dict(learner),
        "metric_cards": metric_cards,
        "sessions": sessions,
        "total_recordings": len(recordings),
        "phoneme_errors": phoneme_errors,
        "vocabulary": vocabulary,
        "l1_predictions": l1_predictions,
        "wpm_trend": wpm_trend,
    }


def _profile_dict(learner: LearnerProfile) -> dict:
    return {
        "learner_id": learner.learner_id,
        "display_name": learner.display_name or "Learner",
        "native_language": learner.native_language or "",
        "level": learner.current_level or "beginner",
        "xp": learner.xp_total or 0,
        "streak": learner.streak_current or 0,
        "streak_longest": learner.streak_longest or 0,
    }


def _empty_metric_cards() -> dict:
    return {
        "streak": 0, "xp": 0, "level": "beginner",
        "objects_scanned": 0, "total_recordings": 0,
        "practice_minutes": 0,
        "avg_accuracy": 0, "avg_fluency": 0,
        "avg_prosody": 0, "avg_completeness": 0,
        "avg_total": 0,
    }


def _safe_avg(values: list) -> float:
    nums = [v for v in values if v is not None]
    return sum(nums) / len(nums) if nums else 0


def _aggregate_phoneme_errors(recordings: list[Recording]) -> list[dict]:
    """Aggregate phoneme-level errors across all recordings for the 'Sounds to Practice' chart."""
    phone_stats = defaultdict(lambda: {"correct": 0, "errors": 0, "subs": defaultdict(int)})

    for rec in recordings:
        if not rec.problematic_phonemes_json:
            continue
        try:
            phonemes = json.loads(rec.problematic_phonemes_json)
            for ph in phonemes:
                if isinstance(ph, dict):
                    label = ph.get("canonical", ph.get("phoneme", ""))
                    error_type = ph.get("error_type", "")
                    predicted = ph.get("predicted", "")
                elif isinstance(ph, str):
                    label = ph
                    error_type = "error"
                    predicted = ""
                else:
                    continue
                if not label:
                    continue  # skip insertions (no canonical phone)
                if error_type == "correct":
                    phone_stats[label]["correct"] += 1
                else:
                    phone_stats[label]["errors"] += 1
                    if predicted and error_type == "substitution":
                        phone_stats[label]["subs"][predicted] += 1
        except (json.JSONDecodeError, TypeError):
            pass

    # Get FL lookup if available
    try:
        from backend.services.intelligibility_scoring import get_functional_load
        has_fl = True
    except ImportError:
        has_fl = False

    # Convert to sorted list (worst phonemes first)
    result = []
    for ph, counts in phone_stats.items():
        total = counts["correct"] + counts["errors"]
        acc = (counts["correct"] / total * 100) if total > 0 else 0
        entry = {
            "phoneme": ph,
            "accuracy": round(acc),
            "error_count": counts["errors"],
        }
        # Add most common substitution + FL weight
        if counts["subs"]:
            top_sub = max(counts["subs"], key=counts["subs"].get)
            entry["top_sub"] = top_sub
            entry["top_sub_count"] = counts["subs"][top_sub]
            if has_fl:
                entry["fl"] = round(get_functional_load(ph, top_sub), 2)
        result.append(entry)

    result.sort(key=lambda x: x["accuracy"])
    return result[:15]  # bottom 15 phonemes


# ── Vocabulary ────────────────────────────────────────────────────────────────

def update_vocabulary(db: Session, learner_id: str, word: str, pronunciation_score: float,
                      phonemes: str = "", object_name: str = "", sentence: str = ""):
    entry = (
        db.query(LearnerVocabulary)
        .filter_by(learner_id=learner_id, word=word.lower())
        .first()
    )
    if entry:
        entry.times_practiced += 1
        entry.avg_pronunciation = (
            (entry.avg_pronunciation * (entry.times_practiced - 1) + pronunciation_score)
            / entry.times_practiced
        )
        entry.last_practiced = datetime.utcnow()
    else:
        entry = LearnerVocabulary(
            learner_id=learner_id,
            word=word.lower(),
            phonemes_arpabet=phonemes,
            times_practiced=1,
            avg_pronunciation=pronunciation_score,
            mastery_level="new",
            last_practiced=datetime.utcnow(),
            context_sentence=sentence,
            detected_object=object_name,
        )
        db.add(entry)

    # Update mastery level based on practice count + score
    if entry.avg_pronunciation >= 80 and entry.times_practiced >= 3:
        entry.mastery_level = "mastered"
    elif entry.avg_pronunciation >= 50:
        entry.mastery_level = "learning"
    elif entry.times_practiced > 0:
        entry.mastery_level = "struggling"

    db.commit()
