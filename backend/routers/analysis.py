"""API endpoints — connected to full ML analysis pipeline."""

import json
import logging
import uuid

from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session

from backend.database.db import get_db
from backend.database.persistence import get_or_create_learner, get_dashboard_data, save_recording, update_vocabulary, get_previous_recording_data, award_xp_and_streak
from backend.config import settings

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api")


@router.post("/session/start")
async def start_session(db: Session = Depends(get_db)):
    """Create a new practice session, return session_id."""
    learner = get_or_create_learner(db)
    session_id = str(uuid.uuid4())
    return {"session_id": session_id, "learner_id": learner.learner_id}


@router.post("/record")
async def record(
    audio: UploadFile = File(...),
    reference_text: str = Form(""),
    object_name: str = Form(""),
    learner_id: str = Form("default"),
    db: Session = Depends(get_db),
):
    """Accept audio upload, run full analysis pipeline, return scores.

    In server mode: enqueues a Celery task and returns a job_id for polling.
    In local mode: runs synchronously and returns results immediately.
    """
    audio_bytes = await audio.read()
    learner = get_or_create_learner(db, learner_id=learner_id)

    # --- Server mode: enqueue to Celery and return job_id ---
    if settings.deployment_mode == "server":
        from backend.services.tasks import analyze_task
        task = analyze_task.delay(
            audio_bytes.hex(), reference_text, object_name, learner.learner_id,
        )
        return {"status": "queued", "job_id": task.id}

    # --- Local mode: run synchronously ---
    from backend.services.speech_processing import analyze_recording

    try:
        result = analyze_recording(audio_bytes, reference_text, object_name)
    except Exception as e:
        logger.exception("Analysis pipeline failed")
        return {"status": "error", "message": str(e)}

    # Update L1 transfer predictions with actual performance
    try:
        from backend.services.l1_predictor import update_prediction
        for pe_dict in result.get("phone_errors", []):
            if pe_dict.get("canonical"):
                accuracy = 100.0 if pe_dict["error_type"] == "correct" else 0.0
                update_prediction(db, learner.learner_id, pe_dict["canonical"], accuracy)
    except Exception as e:
        logger.debug("L1 prediction update skipped: %s", e)

    # Persist to database
    try:
        save_recording(
            db,
            learner_id=learner.learner_id,
            session_id=str(uuid.uuid4()),
            object_name=object_name or None,
            sentence_text=reference_text,
            transcript=result.get("transcript"),
            reading_accuracy=result.get("accuracy"),
            reading_classification=result.get("classification"),
            wer=result.get("wer"),
            word_alignment_json=json.dumps(result.get("words")),
            filler_count=result.get("filler_count"),
            repetition_count=result.get("repetition_count"),
            pronunciation_score=result.get("pronunciation_score"),
            prosody_score=result.get("prosody"),
            stress_accuracy=result.get("stress_accuracy"),
            intonation_accuracy=result.get("intonation_accuracy"),
            rhythm_npvi_v=result.get("rhythm_npvi_v"),
            pitch_range_st=result.get("pitch_range_st"),
            words_per_minute=result.get("words_per_minute"),
            articulation_rate=result.get("articulation_rate"),
            mean_length_of_run=result.get("mean_length_of_run"),
            longest_fluent_phrase=result.get("longest_fluent_phrase"),
            fluency_score=result.get("fluency"),
            utterance_accuracy=result.get("accuracy"),
            utterance_completeness=result.get("completeness"),
            utterance_fluency=result.get("fluency"),
            utterance_prosody=result.get("prosody"),
            utterance_total=result.get("total"),
            word_scores_json=json.dumps(result.get("word_scores")),
            # MDD phone-level results (all phones for per-phoneme accuracy)
            problematic_phonemes_json=json.dumps(
                result.get("phone_errors", [])
            ) if result.get("phone_errors") else None,
            per_ml=result.get("phone_error_rate"),
        )
    except Exception as e:
        logger.warning("Failed to save recording: %s", e)

    # Update vocabulary mastery for each word in the reference text
    try:
        word_scores = {ws["word"].lower(): ws["accuracy"] for ws in result.get("word_scores", []) if ws.get("word")}
        for word in reference_text.split():
            clean = word.strip(".,!?;:\"'()-").lower()
            if clean:
                score = word_scores.get(clean, result.get("accuracy", 50))
                update_vocabulary(
                    db, learner.learner_id, clean,
                    pronunciation_score=float(score),
                    object_name=object_name,
                    sentence=reference_text,
                )
    except Exception as e:
        logger.debug("Vocabulary update skipped: %s", e)

    # Update spaced repetition queue from phoneme-level MDD results
    try:
        from backend.services.spaced_repetition import update_from_mdd_results
        if result.get("phone_errors"):
            update_from_mdd_results(
                db, learner.learner_id, result["phone_errors"]
            )
    except Exception as e:
        logger.debug("Spaced repetition update skipped: %s", e)

    # Award XP and update streak
    try:
        gamification = award_xp_and_streak(
            db, learner.learner_id, result.get("total")
        )
        result["xp_earned"] = gamification["xp_earned"]
        result["xp_total"] = gamification["xp_total"]
        result["streak"] = gamification["streak"]
    except Exception as e:
        logger.debug("XP/streak update skipped: %s", e)

    # Generate human-readable insights + skill bars (with improvement delta)
    try:
        from backend.services.insight_generator import generate_recording_insights, compute_skill_bars
        result["insights"] = generate_recording_insights(result)
        prev_data = get_previous_recording_data(db, learner.learner_id)
        result["skill_bars"] = compute_skill_bars(result, previous=prev_data)
    except Exception as e:
        logger.debug("Insight generation skipped: %s", e)

    return result


@router.get("/recording/{job_id}")
async def get_recording(job_id: str):
    """Poll for analysis results via Celery task status."""
    from celery.result import AsyncResult
    from backend.services.tasks import celery_app

    task = AsyncResult(job_id, app=celery_app)

    if task.state == "PENDING":
        return {"job_id": job_id, "status": "pending", "message": "Waiting in queue..."}
    elif task.state == "ANALYZING":
        meta = task.info or {}
        return {"job_id": job_id, "status": "analyzing", "message": meta.get("step", "Analyzing...")}
    elif task.state == "STARTED":
        return {"job_id": job_id, "status": "started", "message": "Processing..."}
    elif task.state == "SUCCESS":
        return {"job_id": job_id, "status": "complete", "result": task.result}
    elif task.state == "FAILURE":
        return {"job_id": job_id, "status": "error", "message": str(task.result)}
    else:
        return {"job_id": job_id, "status": task.state.lower(), "message": "Processing..."}


@router.get("/recording-detail/{recording_id}")
async def recording_detail(recording_id: int, db: Session = Depends(get_db)):
    """Return full detail for a single recording (exercise detail view)."""
    from backend.database.persistence import get_recording as get_rec
    rec = get_rec(db, recording_id)
    if not rec:
        return {"error": "Recording not found"}

    def safe_json(val):
        if not val:
            return None
        try:
            return json.loads(val)
        except (json.JSONDecodeError, TypeError):
            return None

    result = {
        "id": rec.id,
        "session_id": rec.session_id,
        "date": rec.created_at.strftime(
            "%Y-%m-%d %H:%M"
        ) if rec.created_at else "",
        "object_name": rec.object_name or "",
        "sentence_text": rec.sentence_text or "",
        "transcript": rec.transcript or "",
        "classification": rec.reading_classification or "",
        "accuracy": round(rec.utterance_accuracy or 0),
        "fluency": round(rec.utterance_fluency or 0),
        "prosody": round(rec.utterance_prosody or 0),
        "completeness": round(
            rec.utterance_completeness or 0
        ),
        "total": round(rec.utterance_total or 0),
        "wer": round(rec.wer or 0, 3),
        "words": safe_json(rec.word_alignment_json),
        "word_scores": safe_json(rec.word_scores_json),
        "filler_count": rec.filler_count or 0,
        "repetition_count": rec.repetition_count or 0,
        "pronunciation_score": round(
            rec.pronunciation_score or 0
        ),
        "stress_accuracy": round(
            rec.stress_accuracy or 0
        ),
        "intonation_accuracy": round(
            rec.intonation_accuracy or 0
        ),
        "rhythm_npvi_v": (
            round(rec.rhythm_npvi_v or 0, 1)
            if rec.rhythm_npvi_v else None
        ),
        "pitch_range_st": (
            round(rec.pitch_range_st or 0, 1)
            if rec.pitch_range_st else None
        ),
        "words_per_minute": (
            round(rec.words_per_minute or 0, 1)
            if rec.words_per_minute else None
        ),
        "articulation_rate": (
            round(rec.articulation_rate or 0, 1)
            if rec.articulation_rate else None
        ),
        "mean_length_of_run": (
            round(rec.mean_length_of_run or 0, 1)
            if rec.mean_length_of_run else None
        ),
        "longest_fluent_phrase": rec.longest_fluent_phrase,
        "fluency_score": round(rec.fluency_score or 0),
        "phone_errors": safe_json(
            rec.problematic_phonemes_json
        ),
        "phone_error_rate": (
            round(rec.per_ml or 0, 1)
            if rec.per_ml else None
        ),
        "pauses": safe_json(rec.pauses_json),
    }

    try:
        from backend.services.insight_generator import (
            generate_recording_insights, compute_skill_bars,
        )
        result["insights"] = generate_recording_insights(
            result
        )
        result["skill_bars"] = compute_skill_bars(result)
    except Exception as e:
        logger.debug(
            "Recording insight generation skipped: %s", e
        )

    return result


@router.get("/learner/{learner_id}/dashboard")
async def learner_dashboard(learner_id: str, db: Session = Depends(get_db)):
    """Return aggregated analytics for a learner, including class comparison."""
    data = get_dashboard_data(db, learner_id)
    try:
        from backend.services.insight_generator import generate_dashboard_insights, compute_skill_bars
        data["insights"] = generate_dashboard_insights(data)
        # Skill bars from student's average across all sessions (no delta)
        sessions = data.get("sessions", [])
        if sessions:
            avg_data = {}
            for key in ("accuracy", "fluency", "prosody", "completeness", "wpm"):
                vals = [s.get(key) for s in sessions if s.get(key) is not None]
                if vals:
                    avg_data[key] = sum(vals) / len(vals)
            if "wpm" in avg_data:
                avg_data["words_per_minute"] = avg_data["wpm"]
            data["skill_bars"] = compute_skill_bars(avg_data)
        else:
            data["skill_bars"] = []
    except Exception as e:
        logger.debug("Dashboard insight generation skipped: %s", e)

    # Class comparison: find student's class and compute averages
    try:
        from backend.database.schema import ClassMember, Recording
        membership = db.query(ClassMember).filter_by(learner_id=learner_id).first()
        if membership:
            class_id = membership.class_id
            members = db.query(ClassMember.learner_id).filter_by(class_id=class_id).all()
            class_learner_ids = [m.learner_id for m in members]

            class_recs = (
                db.query(Recording)
                .filter(Recording.learner_id.in_(class_learner_ids))
                .filter(Recording.utterance_total.isnot(None))
                .all()
            ) if class_learner_ids else []

            if class_recs:
                data["class_averages"] = {
                    "accuracy": round(sum(r.utterance_accuracy or 0 for r in class_recs) / len(class_recs)),
                    "fluency": round(sum(r.utterance_fluency or 0 for r in class_recs) / len(class_recs)),
                    "prosody": round(sum(r.utterance_prosody or 0 for r in class_recs) / len(class_recs)),
                    "completeness": round(sum(r.utterance_completeness or 0 for r in class_recs) / len(class_recs)),
                    "total": round(sum(r.utterance_total or 0 for r in class_recs) / len(class_recs)),
                }

                # Rank among class
                per_student_avg = {}
                for lid in class_learner_ids:
                    recs = [r for r in class_recs if r.learner_id == lid]
                    if recs:
                        per_student_avg[lid] = sum(r.utterance_total or 0 for r in recs) / len(recs)
                sorted_students = sorted(per_student_avg.items(), key=lambda x: x[1], reverse=True)
                rank = next((i + 1 for i, (lid, _) in enumerate(sorted_students) if lid == learner_id), None)
                data["class_rank"] = rank
                data["class_size"] = len(sorted_students)
    except Exception as e:
        logger.debug("Class comparison skipped: %s", e)

    return data


@router.get("/objects")
async def list_objects():
    """Return list of available objects from the sentence bank."""
    from backend.services.llm_prompt_generator import _load_sentence_bank
    bank = _load_sentence_bank()
    return {"objects": sorted(bank.keys())}


@router.post("/generate")
async def generate_sentence_endpoint(
    object_name: str = Form("bottle"),
    difficulty: str = Form("beginner"),
    problem_phonemes: str = Form(""),
):
    """Select a practice sentence from the sentence bank."""
    from backend.services.llm_prompt_generator import generate_sentence
    phonemes = (
        [p.strip() for p in problem_phonemes.split(",") if p.strip()]
        if problem_phonemes else None
    )
    sentence = await generate_sentence(
        object_name, difficulty, problem_phonemes=phonemes,
    )
    return {"sentence": sentence, "object": object_name}


@router.post("/dialogue")
async def dialogue_endpoint(
    object_name: str = Form("bottle"),
    difficulty: str = Form("beginner"),
):
    """Get a conversation dialogue for scaffolding mode."""
    from backend.services.llm_prompt_generator import get_dialogue
    dialogue = get_dialogue(object_name, difficulty)
    if dialogue is None:
        return {"error": "No dialogues available for this object/level"}
    return dialogue


@router.get("/tts")
async def tts(text: str):
    """Generate reference TTS audio for a sentence. Returns WAV."""
    from fastapi.responses import Response, JSONResponse
    from backend.services.tts_engine import synthesize

    wav_bytes = synthesize(text)
    if wav_bytes is None:
        return JSONResponse(
            status_code=503,
            content={"error": "TTS unavailable"},
        )

    return Response(content=wav_bytes, media_type="audio/wav")


@router.post("/scene-describe")
async def scene_describe(
    detections: str = Form("[]"),
    difficulty: str = Form("A2"),
):
    """Generate a practice sentence describing a multi-object scene."""
    from backend.services.scene_description import generate_scene_description
    det_list = json.loads(detections)
    result = generate_scene_description(det_list, difficulty)
    return result


@router.post("/minimal-pairs")
async def minimal_pairs_endpoint(
    contrast: str = Form(""),
    difficulty: str = Form("A2"),
):
    """Generate a minimal pair exercise for a phoneme contrast."""
    from backend.services.minimal_pairs import generate_minimal_pair_sentence
    if not contrast:
        return {"error": "contrast parameter required (e.g. R-L)"}
    result = generate_minimal_pair_sentence(contrast, difficulty)
    return result


@router.post("/learner/onboard")
async def onboard_learner(
    display_name: str = Form(""),
    native_language: str = Form(""),
    current_level: str = Form("A1"),
    db: Session = Depends(get_db),
):
    """Onboard a new learner — set profile and initialize L1 predictions."""
    from backend.services.l1_predictor import initialize_predictions, get_supported_languages

    learner = get_or_create_learner(db)
    learner.display_name = display_name or learner.display_name
    learner.native_language = native_language or learner.native_language
    learner.current_level = current_level
    db.commit()

    if native_language:
        initialize_predictions(db, learner.learner_id, native_language)

    return {
        "learner_id": learner.learner_id,
        "display_name": learner.display_name,
        "native_language": learner.native_language,
        "current_level": learner.current_level,
        "supported_languages": get_supported_languages(),
    }


@router.get("/languages")
async def list_languages():
    """List supported L1 languages for onboarding."""
    from backend.services.l1_predictor import get_supported_languages
    return get_supported_languages()


@router.get("/learner/{learner_id}/due-phonemes")
async def due_phonemes(learner_id: str, limit: int = 5, db: Session = Depends(get_db)):
    """Return phonemes due for spaced repetition review."""
    from backend.services.spaced_repetition import get_due_phonemes, get_all_phoneme_schedules
    due = get_due_phonemes(db, learner_id, limit=limit)
    all_schedules = get_all_phoneme_schedules(db, learner_id)
    return {"due": due, "all_schedules": all_schedules}


@router.get("/learner/{learner_id}/vocabulary")
async def learner_vocabulary(learner_id: str, db: Session = Depends(get_db)):
    """Return vocabulary mastery data for a learner."""
    from backend.database.schema import LearnerVocabulary
    vocab = (
        db.query(LearnerVocabulary)
        .filter_by(learner_id=learner_id)
        .order_by(LearnerVocabulary.last_practiced.desc())
        .limit(100)
        .all()
    )
    return {
        "vocabulary": [
            {
                "word": v.word,
                "times_practiced": v.times_practiced,
                "avg_pronunciation": round(v.avg_pronunciation or 0, 1),
                "mastery_level": v.mastery_level,
                "last_practiced": v.last_practiced.isoformat() if v.last_practiced else None,
                "detected_object": v.detected_object,
            }
            for v in vocab
        ],
        "summary": {
            "total": len(vocab),
            "mastered": sum(1 for v in vocab if v.mastery_level == "mastered"),
            "learning": sum(1 for v in vocab if v.mastery_level == "learning"),
            "struggling": sum(1 for v in vocab if v.mastery_level == "struggling"),
            "new": sum(1 for v in vocab if v.mastery_level == "new"),
        },
    }


@router.get("/learner/{learner_id}/l1-predictions")
async def l1_predictions(learner_id: str, db: Session = Depends(get_db)):
    """Return L1 transfer predictions with actual accuracy data."""
    from backend.services.l1_predictor import get_predictions_with_actuals
    predictions = get_predictions_with_actuals(db, learner_id)
    return {"predictions": predictions}
