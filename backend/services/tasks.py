"""
Celery task definitions for async analysis pipeline.

POST /api/record → enqueue task → return job_id
GET /api/recording/{job_id} → check Redis → return result when done

Requires: Redis running on localhost:6379 (or configured in settings).
"""

import json
import logging

from celery import Celery

from backend.config import settings

logger = logging.getLogger(__name__)

celery_app = Celery(
    "linguar",
    broker=settings.redis_url,
    backend=settings.redis_url,
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    task_track_started=True,
    result_expires=3600,  # results expire after 1 hour
    worker_max_tasks_per_child=50,  # restart worker after 50 tasks (memory management for ML models)
)


@celery_app.task(bind=True, name="linguar.analyze")
def analyze_task(self, audio_bytes_hex: str, reference_text: str, object_name: str, learner_id: str):
    """
    Async analysis task. Audio is passed as hex-encoded bytes.
    Returns the full analysis result dict.
    """
    from backend.services.speech_processing import analyze_recording
    from backend.database.db import SessionLocal
    from backend.database.persistence import save_recording

    # Decode audio
    audio_bytes = bytes.fromhex(audio_bytes_hex)

    # Run analysis
    self.update_state(state="ANALYZING", meta={"step": "Running ML pipeline..."})
    result = analyze_recording(audio_bytes, reference_text, object_name)

    # Save to DB
    try:
        db = SessionLocal()
        save_recording(
            db,
            learner_id=learner_id,
            session_id=self.request.id,
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
        )
        db.close()
    except Exception as e:
        logger.warning("Failed to save recording in task: %s", e)

    return result
