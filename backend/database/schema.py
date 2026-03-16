"""SQLAlchemy ORM models — all tables from the LinguAR spec (Section 5)."""

from datetime import datetime, date
from sqlalchemy import (
    Column, Integer, Text, Float, Boolean, DateTime, Date, UniqueConstraint,
)
from backend.database.db import Base


class LearnerProfile(Base):
    __tablename__ = "learner_profiles"

    learner_id = Column(Text, primary_key=True)
    display_name = Column(Text)
    native_language = Column(Text)
    current_level = Column(Text, default="A1")
    classroom = Column(Text, default="")
    role = Column(Text, default="learner")  # learner / teacher
    xp_total = Column(Integer, default=0)
    streak_current = Column(Integer, default=0)
    streak_longest = Column(Integer, default=0)
    last_active_date = Column(Date)
    daily_goal_minutes = Column(Integer, default=10)
    created_at = Column(DateTime, default=datetime.utcnow)


class Recording(Base):
    __tablename__ = "recordings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(Text)
    learner_id = Column(Text)

    # Content
    object_name = Column(Text)
    scene_objects_json = Column(Text)
    sentence_text = Column(Text)
    difficulty_level = Column(Text)
    sentence_type = Column(Text)
    grammar_focus = Column(Text)

    # Audio
    audio_path = Column(Text)
    transcript = Column(Text)

    # Reading accuracy
    reading_accuracy = Column(Float)
    reading_classification = Column(Text)
    wer = Column(Float)
    word_alignment_json = Column(Text)
    missed_words_json = Column(Text)
    filler_count = Column(Integer)
    repetition_count = Column(Integer)

    # Pronunciation (HuBERT MDD + FL-weighted)
    pronunciation_score = Column(Float)
    per_ml = Column(Float)
    ml_gop = Column(Float)
    ml_confidence = Column(Float)
    ml_detected_phonemes_json = Column(Text)
    ml_detected_ipa_json = Column(Text)
    ml_alignment_json = Column(Text)
    ml_phoneme_scores_json = Column(Text)
    problematic_phonemes_json = Column(Text)
    speech_rate = Column(Float)

    # Prosody
    prosody_score = Column(Float)
    stress_accuracy = Column(Float)
    intonation_accuracy = Column(Float)
    rhythm_npvi_v = Column(Float)
    pitch_range_st = Column(Float)
    mfa_textgrid_path = Column(Text)
    prosody_details_json = Column(Text)

    # Fluency
    words_per_minute = Column(Float)
    articulation_rate = Column(Float)
    mean_length_of_run = Column(Float)
    longest_fluent_phrase = Column(Integer)
    hesitation_ratio = Column(Float)
    mid_phrase_pause_rate = Column(Float)
    filled_pause_rate = Column(Float)
    repetition_rate = Column(Float)
    total_pauses = Column(Integer)
    hesitation_count = Column(Integer)
    speaking_rate = Column(Float)
    fluency_score = Column(Float)
    pauses_json = Column(Text)

    # Hierarchical scores
    word_scores_json = Column(Text)
    utterance_accuracy = Column(Float)
    utterance_completeness = Column(Float)
    utterance_fluency = Column(Float)
    utterance_prosody = Column(Float)
    utterance_total = Column(Float)

    # Metadata
    analysis_mode = Column(Text)
    tts_audio_path = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)


class LearnerVocabulary(Base):
    __tablename__ = "learner_vocabulary"
    __table_args__ = (UniqueConstraint("learner_id", "word"),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    learner_id = Column(Text)
    word = Column(Text)
    phonemes_arpabet = Column(Text)
    times_practiced = Column(Integer, default=0)
    avg_pronunciation = Column(Float)
    mastery_level = Column(Text, default="new")
    last_practiced = Column(DateTime)
    context_sentence = Column(Text)
    detected_object = Column(Text)


class SpacedRepetitionQueue(Base):
    __tablename__ = "spaced_repetition_queue"
    __table_args__ = (UniqueConstraint("learner_id", "phoneme"),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    learner_id = Column(Text)
    phoneme = Column(Text)
    interval_days = Column(Float)
    due_date = Column(Date)
    easiness_factor = Column(Float, default=2.5)
    repetitions = Column(Integer, default=0)
    last_score = Column(Float)
    last_reviewed = Column(DateTime)


class L1TransferPrediction(Base):
    __tablename__ = "l1_transfer_predictions"

    learner_id = Column(Text, primary_key=True)
    phoneme = Column(Text, primary_key=True)
    predicted_difficult = Column(Boolean)
    actual_accuracy = Column(Float)
    confirmed = Column(Boolean)


class Class(Base):
    __tablename__ = "classes"

    class_id = Column(Text, primary_key=True)
    teacher_name = Column(Text)
    class_name = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)


class ClassMember(Base):
    __tablename__ = "class_members"

    class_id = Column(Text, primary_key=True)
    learner_id = Column(Text, primary_key=True)


class ClassAssignment(Base):
    __tablename__ = "class_assignments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    class_id = Column(Text)
    target_objects_json = Column(Text)
    target_level = Column(Text)
    is_open = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class DailyProgress(Base):
    __tablename__ = "daily_progress"
    __table_args__ = (UniqueConstraint("learner_id", "date"),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    learner_id = Column(Text)
    date = Column(Date)
    sessions_completed = Column(Integer, default=0)
    sentences_practiced = Column(Integer, default=0)
    minutes_practiced = Column(Float, default=0)
    avg_pronunciation = Column(Float)
    avg_fluency = Column(Float)
    xp_earned = Column(Integer, default=0)
    new_words_learned = Column(Integer, default=0)


class GeneratedPrompt(Base):
    __tablename__ = "generated_prompts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    object_name = Column(Text)
    difficulty_level = Column(Text)
    prompt_json = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)


class SessionProgress(Base):
    __tablename__ = "session_progress"

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(Text)
    learner_id = Column(Text)
    avg_pronunciation = Column(Float)
    avg_fluency = Column(Float)
    sentences_completed = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
