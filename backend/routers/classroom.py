"""Teacher dashboard + classroom management API endpoints."""

import json
import logging
import uuid
from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from sqlalchemy import func

from backend.database.db import get_db
from backend.database.schema import (
    Class, ClassMember, ClassAssignment, LearnerProfile, Recording,
    SpacedRepetitionQueue, L1TransferPrediction, DailyProgress,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/classroom")


# ── Class management ─────────────────────────────────────────────────────────

@router.post("/class")
async def create_class(
    class_name: str = Form(...),
    teacher_name: str = Form(""),
    db: Session = Depends(get_db),
):
    """Create a new classroom."""
    class_id = str(uuid.uuid4())[:8]
    new_class = Class(
        class_id=class_id,
        class_name=class_name,
        teacher_name=teacher_name,
    )
    db.add(new_class)
    db.commit()
    return {"class_id": class_id, "class_name": class_name}


@router.get("/class/{class_id}")
async def get_class(class_id: str, db: Session = Depends(get_db)):
    """Get class info with member list."""
    cls = db.query(Class).filter_by(class_id=class_id).first()
    if not cls:
        return {"error": "Class not found"}

    members = (
        db.query(ClassMember.learner_id)
        .filter_by(class_id=class_id)
        .all()
    )
    learner_ids = [m.learner_id for m in members]

    learners = (
        db.query(LearnerProfile)
        .filter(LearnerProfile.learner_id.in_(learner_ids))
        .all()
    ) if learner_ids else []

    return {
        "class_id": cls.class_id,
        "class_name": cls.class_name,
        "teacher_name": cls.teacher_name,
        "member_count": len(learner_ids),
        "members": [
            {
                "learner_id": l.learner_id,
                "display_name": l.display_name or l.learner_id,
                "current_level": l.current_level,
                "xp_total": l.xp_total,
                "last_active": l.last_active_date.isoformat() if l.last_active_date else None,
            }
            for l in learners
        ],
    }


@router.post("/class/{class_id}/join")
async def join_class(
    class_id: str,
    learner_id: str = Form(...),
    db: Session = Depends(get_db),
):
    """Add a learner to a class."""
    cls = db.query(Class).filter_by(class_id=class_id).first()
    if not cls:
        return {"error": "Class not found"}

    existing = db.query(ClassMember).filter_by(
        class_id=class_id, learner_id=learner_id
    ).first()
    if existing:
        return {"status": "already_member"}

    db.add(ClassMember(class_id=class_id, learner_id=learner_id))
    db.commit()
    return {"status": "joined", "class_id": class_id}


# ── Assignments ──────────────────────────────────────────────────────────────

@router.post("/class/{class_id}/assignment")
async def create_assignment(
    class_id: str,
    target_objects: str = Form(""),
    target_level: str = Form("A1"),
    db: Session = Depends(get_db),
):
    """Create a practice assignment for the class (opens immediately)."""
    assignment = ClassAssignment(
        class_id=class_id,
        target_objects_json=target_objects,
        target_level=target_level,
        is_open=True,
    )
    db.add(assignment)
    db.commit()
    return {"assignment_id": assignment.id, "class_id": class_id}


@router.post("/assignment/{assignment_id}/close")
async def close_assignment(assignment_id: int, db: Session = Depends(get_db)):
    """Close an assignment — removes it from student view."""
    assignment = db.query(ClassAssignment).filter_by(id=assignment_id).first()
    if not assignment:
        return {"error": "Assignment not found"}
    assignment.is_open = False
    db.commit()
    return {"status": "closed", "assignment_id": assignment_id}


@router.post("/assignment/{assignment_id}/open")
async def open_assignment(assignment_id: int, db: Session = Depends(get_db)):
    """Re-open an assignment — makes it visible to students again."""
    assignment = db.query(ClassAssignment).filter_by(id=assignment_id).first()
    if not assignment:
        return {"error": "Assignment not found"}
    assignment.is_open = True
    db.commit()
    return {"status": "open", "assignment_id": assignment_id}


@router.get("/class/{class_id}/assignments")
async def get_assignments(class_id: str, db: Session = Depends(get_db)):
    """List all assignments for a class (teacher view)."""
    assignments = (
        db.query(ClassAssignment)
        .filter_by(class_id=class_id)
        .order_by(ClassAssignment.created_at.desc())
        .all()
    )
    return [
        {
            "id": a.id,
            "target_objects": a.target_objects_json,
            "target_level": a.target_level,
            "is_open": a.is_open,
            "created_at": a.created_at.isoformat() if a.created_at else None,
        }
        for a in assignments
    ]


@router.get("/class/{class_id}/assignments/active")
async def get_active_assignments(class_id: str, db: Session = Depends(get_db)):
    """List open assignments for a class (student view)."""
    assignments = (
        db.query(ClassAssignment)
        .filter_by(class_id=class_id, is_open=True)
        .order_by(ClassAssignment.created_at.desc())
        .all()
    )
    return [
        {
            "id": a.id,
            "target_objects": a.target_objects_json,
            "target_level": a.target_level,
        }
        for a in assignments
    ]


# ── Class-wide analytics ────────────────────────────────────────────────────

@router.get("/class/{class_id}/analytics")
async def class_analytics(class_id: str, db: Session = Depends(get_db)):
    """Aggregate analytics across all class members."""
    members = (
        db.query(ClassMember.learner_id)
        .filter_by(class_id=class_id)
        .all()
    )
    learner_ids = [m.learner_id for m in members]
    if not learner_ids:
        return {"member_count": 0, "analytics": {}}

    from collections import defaultdict

    # Fetch ALL recordings for the class in one query
    all_recs = (
        db.query(Recording)
        .filter(Recording.learner_id.in_(learner_ids))
        .order_by(Recording.created_at)
        .all()
    )

    # Group recordings by learner
    recs_by_learner = defaultdict(list)
    for rec in all_recs:
        recs_by_learner[rec.learner_id].append(rec)

    # Per-learner summary (with dimension averages)
    learner_stats = []
    for lid in learner_ids:
        recordings = recs_by_learner.get(lid, [])
        profile = db.query(LearnerProfile).filter_by(learner_id=lid).first()

        if recordings:
            scores = [r.utterance_total for r in recordings if r.utterance_total is not None]
            avg_score = sum(scores) / len(scores) if scores else None
            recent = max(r.created_at for r in recordings if r.created_at)
            # Per-dimension averages
            acc_vals = [r.utterance_accuracy for r in recordings if r.utterance_accuracy is not None]
            flu_vals = [r.utterance_fluency for r in recordings if r.utterance_fluency is not None]
            pro_vals = [r.utterance_prosody for r in recordings if r.utterance_prosody is not None]
            com_vals = [r.utterance_completeness for r in recordings if r.utterance_completeness is not None]
            avg_acc = sum(acc_vals) / len(acc_vals) if acc_vals else None
            avg_flu = sum(flu_vals) / len(flu_vals) if flu_vals else None
            avg_pro = sum(pro_vals) / len(pro_vals) if pro_vals else None
            avg_com = sum(com_vals) / len(com_vals) if com_vals else None
        else:
            avg_score = None
            recent = None
            avg_acc = avg_flu = avg_pro = avg_com = None

        learner_stats.append({
            "learner_id": lid,
            "display_name": profile.display_name if profile else lid,
            "level": profile.current_level if profile else "A1",
            "total_recordings": len(recordings),
            "avg_score": round(avg_score, 1) if avg_score else None,
            "avg_accuracy": round(avg_acc, 1) if avg_acc is not None else None,
            "avg_fluency": round(avg_flu, 1) if avg_flu is not None else None,
            "avg_prosody": round(avg_pro, 1) if avg_pro is not None else None,
            "avg_completeness": round(avg_com, 1) if avg_com is not None else None,
            "last_active": recent.isoformat() if recent else None,
        })

    # Class-wide aggregates (overall + per dimension)
    _avg = lambda vals: round(sum(vals) / len(vals), 1) if vals else None
    all_scores = [s["avg_score"] for s in learner_stats if s["avg_score"] is not None]
    class_avg = _avg(all_scores)
    class_dim_averages = {
        "accuracy": _avg([s["avg_accuracy"] for s in learner_stats if s["avg_accuracy"] is not None]),
        "fluency": _avg([s["avg_fluency"] for s in learner_stats if s["avg_fluency"] is not None]),
        "prosody": _avg([s["avg_prosody"] for s in learner_stats if s["avg_prosody"] is not None]),
        "completeness": _avg([s["avg_completeness"] for s in learner_stats if s["avg_completeness"] is not None]),
    }

    # Leaderboard — sorted by avg_score descending
    leaderboard = sorted(
        [s for s in learner_stats if s["avg_score"] is not None],
        key=lambda x: x["avg_score"],
        reverse=True,
    )
    for rank, entry in enumerate(leaderboard, 1):
        entry["rank"] = rank

    # Class progress trend — weekly averages over time
    progress_trend = []
    if all_recs:
        week_buckets = defaultdict(list)
        for rec in all_recs:
            if rec.utterance_total is not None and rec.created_at:
                # ISO week key
                dt = rec.created_at
                week_key = f"{dt.isocalendar()[0]}-W{dt.isocalendar()[1]:02d}"
                week_buckets[week_key].append(rec)

        for week_key in sorted(week_buckets.keys()):
            recs = week_buckets[week_key]
            totals = [r.utterance_total for r in recs if r.utterance_total is not None]
            acc = [r.utterance_accuracy for r in recs if r.utterance_accuracy is not None]
            flu = [r.utterance_fluency for r in recs if r.utterance_fluency is not None]
            pro = [r.utterance_prosody for r in recs if r.utterance_prosody is not None]
            # Use the date of the first recording in the week as the label
            first_date = min(r.created_at for r in recs if r.created_at)
            progress_trend.append({
                "week": week_key,
                "date": first_date.strftime("%b %d"),
                "avg_total": _avg(totals),
                "avg_accuracy": _avg(acc),
                "avg_fluency": _avg(flu),
                "avg_prosody": _avg(pro),
                "recordings": len(recs),
            })

    # Struggling words — most commonly missed/substituted words across the class
    word_errors = defaultdict(lambda: {"errors": 0, "total": 0, "students": set()})
    for rec in all_recs:
        if not rec.word_scores_json:
            continue
        try:
            words = json.loads(rec.word_scores_json)
            for w in words:
                if isinstance(w, dict):
                    word = (w.get("word") or w.get("reference") or "").lower().strip()
                    if not word or len(word) < 2:
                        continue
                    word_errors[word]["total"] += 1
                    label = w.get("label", w.get("type", ""))
                    if label in ("substitution", "deletion", "mispronounced", "error"):
                        word_errors[word]["errors"] += 1
                        word_errors[word]["students"].add(rec.learner_id)
        except (json.JSONDecodeError, TypeError):
            pass

    struggling_words = []
    for word, counts in word_errors.items():
        if counts["errors"] >= 2 and counts["total"] >= 2:
            error_rate = counts["errors"] / counts["total"] * 100
            struggling_words.append({
                "word": word,
                "error_rate": round(error_rate),
                "error_count": counts["errors"],
                "total": counts["total"],
                "student_count": len(counts["students"]),
            })
    struggling_words.sort(key=lambda x: x["error_rate"], reverse=True)

    # Common problem phonemes across the class
    phone_counts = defaultdict(lambda: {"errors": 0, "total": 0})
    for rec in all_recs:
        if not rec.problematic_phonemes_json:
            continue
        try:
            phonemes = json.loads(rec.problematic_phonemes_json)
            for ph in phonemes:
                label = ""
                error_type = "error"
                if isinstance(ph, dict):
                    label = ph.get("canonical", ph.get("phoneme", ""))
                    error_type = ph.get("error_type", "error")
                elif isinstance(ph, str):
                    label = ph
                if label:
                    phone_counts[label]["total"] += 1
                    if error_type != "correct":
                        phone_counts[label]["errors"] += 1
        except (json.JSONDecodeError, TypeError):
            pass

    problem_phonemes = []
    for ph, counts in phone_counts.items():
        acc = max(0, 100 - (counts["errors"] / max(counts["total"], 1)) * 100)
        problem_phonemes.append({
            "phoneme": ph,
            "avg_score": round(acc, 1),
            "learner_count": counts["errors"],
        })
    problem_phonemes.sort(key=lambda x: x["avg_score"])

    # Score distribution — histogram buckets for class overview
    score_dist = {"0-20": 0, "20-40": 0, "40-60": 0, "60-80": 0, "80-100": 0}
    for s in learner_stats:
        if s["avg_score"] is not None:
            v = s["avg_score"]
            if v < 20: score_dist["0-20"] += 1
            elif v < 40: score_dist["20-40"] += 1
            elif v < 60: score_dist["40-60"] += 1
            elif v < 80: score_dist["60-80"] += 1
            else: score_dist["80-100"] += 1

    result = {
        "member_count": len(learner_ids),
        "class_avg_score": class_avg,
        "class_dim_averages": class_dim_averages,
        "score_distribution": score_dist,
        "learners": learner_stats,
        "leaderboard": leaderboard[:20],
        "progress_trend": progress_trend,
        "struggling_words": struggling_words[:15],
        "common_problem_phonemes": problem_phonemes[:10],
    }

    # Generate class-level insights for teacher
    try:
        from backend.services.insight_generator import generate_class_insights
        result["insights"] = generate_class_insights(result)
    except Exception:
        pass

    return result


# ── Teacher view of a single student (with class comparison) ─────────────

@router.get("/class/{class_id}/student/{learner_id}")
async def student_detail_for_teacher(
    class_id: str, learner_id: str, db: Session = Depends(get_db),
):
    """
    Return a student's full dashboard data plus class averages for comparison.
    Used by the teacher's student detail page.
    """
    from backend.database.persistence import get_dashboard_data
    from backend.services.insight_generator import (
        generate_dashboard_insights, compute_skill_bars,
    )

    # Student's own data
    student_data = get_dashboard_data(db, learner_id)

    # Add insights + skill bars
    try:
        student_data["insights"] = generate_dashboard_insights(student_data)
        sessions = student_data.get("sessions", [])
        if sessions:
            latest = dict(sessions[-1])
            if "wpm" in latest and "words_per_minute" not in latest:
                latest["words_per_minute"] = latest["wpm"]
            # Compare latest against student's average performance
            avg_data = {}
            if len(sessions) >= 2:
                for key in ("accuracy", "fluency", "prosody", "completeness", "wpm"):
                    vals = [s.get(key) for s in sessions if s.get(key) is not None]
                    if vals:
                        avg_data[key] = sum(vals) / len(vals)
                if "wpm" in avg_data:
                    avg_data["words_per_minute"] = avg_data["wpm"]
            student_data["skill_bars"] = compute_skill_bars(latest, previous=avg_data if avg_data else None)
    except Exception:
        pass

    # Class averages for comparison
    members = (
        db.query(ClassMember.learner_id)
        .filter_by(class_id=class_id)
        .all()
    )
    class_learner_ids = [m.learner_id for m in members]

    class_recs = (
        db.query(Recording)
        .filter(Recording.learner_id.in_(class_learner_ids))
        .filter(Recording.utterance_total.isnot(None))
        .all()
    ) if class_learner_ids else []

    if class_recs:
        class_avg_accuracy = sum(r.utterance_accuracy or 0 for r in class_recs) / len(class_recs)
        class_avg_fluency = sum(r.utterance_fluency or 0 for r in class_recs) / len(class_recs)
        class_avg_prosody = sum(r.utterance_prosody or 0 for r in class_recs) / len(class_recs)
        class_avg_completeness = sum(r.utterance_completeness or 0 for r in class_recs) / len(class_recs)
        class_avg_total = sum(r.utterance_total or 0 for r in class_recs) / len(class_recs)
        class_avg_wpm = sum(r.words_per_minute or 0 for r in class_recs if r.words_per_minute) / max(
            sum(1 for r in class_recs if r.words_per_minute), 1
        )
    else:
        class_avg_accuracy = class_avg_fluency = class_avg_prosody = 0
        class_avg_completeness = class_avg_total = class_avg_wpm = 0

    student_data["class_averages"] = {
        "accuracy": round(class_avg_accuracy),
        "fluency": round(class_avg_fluency),
        "prosody": round(class_avg_prosody),
        "completeness": round(class_avg_completeness),
        "total": round(class_avg_total),
        "wpm": round(class_avg_wpm),
        "student_count": len(class_learner_ids),
    }

    # Rank among class
    per_student_avg = {}
    for lid in class_learner_ids:
        recs = [r for r in class_recs if r.learner_id == lid]
        if recs:
            per_student_avg[lid] = sum(r.utterance_total or 0 for r in recs) / len(recs)
    sorted_students = sorted(per_student_avg.items(), key=lambda x: x[1], reverse=True)
    rank = next((i + 1 for i, (lid, _) in enumerate(sorted_students) if lid == learner_id), None)
    student_data["class_rank"] = rank
    student_data["class_size"] = len(sorted_students)

    return student_data


# ── Learner-specific endpoints (used by both learner and teacher) ────────

@router.get("/learner/{learner_id}/phoneme-schedule")
async def learner_phoneme_schedule(learner_id: str, db: Session = Depends(get_db)):
    """Get spaced repetition schedule for a learner."""
    from backend.services.spaced_repetition import get_all_phoneme_schedules
    return get_all_phoneme_schedules(db, learner_id)


@router.get("/learner/{learner_id}/due-phonemes")
async def learner_due_phonemes(learner_id: str, db: Session = Depends(get_db)):
    """Get phonemes due for review."""
    from backend.services.spaced_repetition import get_due_phonemes
    return get_due_phonemes(db, learner_id)


@router.get("/learner/{learner_id}/l1-predictions")
async def learner_l1_predictions(learner_id: str, db: Session = Depends(get_db)):
    """Get L1 transfer predictions with actual performance."""
    from backend.services.l1_predictor import get_predictions_with_actuals
    return get_predictions_with_actuals(db, learner_id)
