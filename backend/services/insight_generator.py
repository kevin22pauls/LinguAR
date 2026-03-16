from __future__ import annotations

"""
Insight generator — converts raw analysis numbers into plain-English feedback.

Two audiences:
  - student: simple, encouraging, actionable (grade 6 level)
  - teacher: detailed, diagnostic, research-backed

Research basis:
  - Munro & Derwing (2006): high FL errors dominate comprehensibility
  - De Jong (2016): mid-clause pauses indicate formulation difficulty
  - Tavakoli et al. (2020): MLR strongest predictor of perceived fluency
  - Hahn (2004): lexical stress #1 suprasegmental for intelligibility
  - Skehan (2009): accuracy-fluency tradeoff, repair fluency as confidence
  - Grabe & Low (2002): English stress-timed, nPVI-V should be 50-70
"""

import logging
from typing import Any

logger = logging.getLogger(__name__)

# ARPAbet to friendly name mapping for student-facing output
_PHONE_NAMES = {
    "TH": "th (as in think)", "DH": "th (as in this)",
    "S": "s", "Z": "z", "SH": "sh", "ZH": "zh",
    "R": "r", "L": "l", "F": "f", "V": "v",
    "W": "w", "P": "p", "B": "b", "T": "t", "D": "d",
    "K": "k", "G": "g", "N": "n", "M": "m", "NG": "ng",
    "CH": "ch", "JH": "j", "HH": "h", "Y": "y",
    "AE": "a (as in cat)", "AH": "uh", "AA": "ah",
    "IH": "i (as in sit)", "IY": "ee", "EH": "e (as in bed)",
    "UW": "oo", "UH": "u (as in put)", "OW": "oh", "AO": "aw",
    "AY": "eye", "EY": "ay", "OY": "oy", "AW": "ow",
    "ER": "er",
}


def _friendly_phone(arpabet: str) -> str:
    """Convert ARPAbet to a friendly name for students."""
    clean = arpabet.rstrip("012")
    return _PHONE_NAMES.get(clean, "/" + clean.lower() + "/")


# ── Single Recording Insights (shown after practice) ────────────────────────

def generate_recording_insights(data: dict) -> dict:
    """
    Generate insights for a single recording result.
    Returns {student: [...], teacher: [...]}.
    """
    student = []
    teacher = []

    accuracy = data.get("accuracy")
    fluency = data.get("fluency")
    prosody = data.get("prosody")
    completeness = data.get("completeness")
    total = data.get("total")
    wpm = data.get("words_per_minute")
    mlr = data.get("mean_length_of_run")
    art_rate = data.get("articulation_rate")
    stress_acc = data.get("stress_accuracy")
    intonation = data.get("intonation_accuracy")
    npvi = data.get("rhythm_npvi_v")
    fillers = data.get("filler_count", 0) or 0
    reps = data.get("repetition_count", 0) or 0
    per = data.get("phone_error_rate")
    phone_errors = data.get("phone_errors", []) or []
    word_scores = data.get("word_scores", []) or []
    longest_phrase = data.get("longest_fluent_phrase")

    # ── Overall verdict ─────────────────────────────────────────────
    if total is not None:
        if total >= 80:
            student.append({
                "type": "success",
                "text": "Great job! You read that really well.",
            })
        elif total >= 60:
            student.append({
                "type": "encouragement",
                "text": "Good effort! A few things to work on — keep practicing.",
            })
        elif total >= 40:
            student.append({
                "type": "encouragement",
                "text": "Nice try! Let's look at what you can improve.",
            })
        else:
            student.append({
                "type": "encouragement",
                "text": "Keep going! Every practice makes you better.",
            })

    # ── Specific sound errors (phoneme-level) ───────────────────────
    subs = [pe for pe in phone_errors if pe.get("error_type") == "substitution"]
    dels = [pe for pe in phone_errors if pe.get("error_type") == "deletion"]
    ins = [pe for pe in phone_errors if pe.get("error_type") == "insertion"]
    l1_errors = [pe for pe in subs if pe.get("l1_expected")]

    if subs:
        # Group by canonical→predicted pair
        pairs = {}
        for pe in subs:
            key = (pe.get("canonical", ""), pe.get("predicted", ""))
            pairs[key] = pairs.get(key, 0) + 1
        # Show top 3 substitution pairs
        top_pairs = sorted(pairs.items(), key=lambda x: x[1], reverse=True)[:3]
        for (canon, pred), count in top_pairs:
            friendly_canon = _friendly_phone(canon)
            friendly_pred = _friendly_phone(pred)
            student.append({
                "type": "pronunciation",
                "text": f'You said "{friendly_pred}" instead of "{friendly_canon}". '
                        f"Try saying the {friendly_canon} sound more clearly.",
            })
            teacher.append({
                "type": "pronunciation",
                "text": f"/{canon}/→/{pred}/ substitution ({count}×). "
                        + ("This is a common Tamil L1 transfer pattern." if any(
                            pe.get("canonical") == canon and pe.get("predicted") == pred and pe.get("l1_expected")
                            for pe in subs
                        ) else ""),
            })

    if l1_errors:
        count = len(l1_errors)
        student.append({
            "type": "accent",
            "text": f"{count} sound{'s' if count > 1 else ''} came out with your Tamil accent — "
                    "that's normal! With practice, you'll get closer to the target.",
        })

    if dels:
        missed = set(pe.get("canonical", "") for pe in dels)
        friendly = ", ".join(_friendly_phone(p) for p in list(missed)[:3])
        student.append({
            "type": "pronunciation",
            "text": f"You skipped the {friendly} sound{'s' if len(missed) > 1 else ''}. "
                    "Try to say every sound in the word.",
        })

    if len(ins) >= 3:
        student.append({
            "type": "pronunciation",
            "text": "You added some extra sounds between words. "
                    "Try to connect words smoothly without adding sounds.",
        })
        teacher.append({
            "type": "pronunciation",
            "text": f"{len(ins)} insertions detected — likely epenthesis, "
                    "common in syllable-timed L1 speakers. Will reduce with fluency practice.",
        })

    # ── Word-level feedback ─────────────────────────────────────────
    wrong_words = [ws for ws in word_scores if ws.get("label") in ("S", "D")]
    if wrong_words and len(wrong_words) <= 3:
        word_list = ", ".join(f'"{w["word"]}"' for w in wrong_words)
        student.append({
            "type": "words",
            "text": f"Practice these words: {word_list}.",
        })

    # ── Completeness ────────────────────────────────────────────────
    if completeness is not None and completeness < 80:
        skipped = [ws["word"] for ws in word_scores if ws.get("label") == "D"]
        if skipped:
            word_list = ", ".join(f'"{w}"' for w in skipped[:3])
            student.append({
                "type": "completeness",
                "text": f"You skipped some words: {word_list}. "
                        "Try reading the full sentence next time.",
            })
            teacher.append({
                "type": "completeness",
                "text": f"Completeness {completeness}% — {len(skipped)} word(s) skipped. "
                        "May indicate vocabulary gap; pre-teach vocabulary before reading.",
            })

    # ── Fluency insights ────────────────────────────────────────────
    _generate_fluency_insights(
        student, teacher, wpm, mlr, art_rate, fillers, reps,
        longest_phrase, accuracy, fluency,
    )

    # ── Prosody insights ────────────────────────────────────────────
    _generate_prosody_insights(
        student, teacher, stress_acc, intonation, npvi,
    )

    # ── Accuracy vs Fluency tradeoff ────────────────────────────────
    if accuracy is not None and fluency is not None:
        if accuracy >= 70 and fluency < 40:
            student.append({
                "type": "tip",
                "text": "Your sounds are good! Now try reading a bit faster and smoother.",
            })
            teacher.append({
                "type": "diagnostic",
                "text": "Accuracy-fluency gap: high accuracy ({}), low fluency ({}). "
                        "Student knows the sounds but needs more reading practice for automaticity.".format(
                            accuracy, fluency),
            })
        elif accuracy < 40 and fluency >= 60:
            student.append({
                "type": "tip",
                "text": "You're reading fast — great! Now slow down a little "
                        "and focus on saying each word clearly.",
            })
            teacher.append({
                "type": "diagnostic",
                "text": "Speed-accuracy tradeoff: low accuracy ({}), high fluency ({}). "
                        "Student reads fast but skips over difficult sounds. "
                        "Slow reading tasks with focus on problem words recommended.".format(
                            accuracy, fluency),
            })

    return {"student": student, "teacher": teacher}


def _generate_fluency_insights(
    student: list, teacher: list,
    wpm, mlr, art_rate, fillers, reps, longest_phrase, accuracy, fluency,
):
    """Fluency-specific insights."""
    if wpm is not None and mlr is not None:
        if wpm >= 90 and mlr is not None and mlr < 4:
            student.append({
                "type": "fluency",
                "text": "You're reading fast, but you're stopping a lot between words. "
                        "Try reading groups of words together without pausing.",
            })
            teacher.append({
                "type": "fluency",
                "text": f"High WPM ({wpm:.0f}) but low MLR ({mlr:.1f}) — "
                        "reading fast but choppy. Practice phrase-level reading.",
            })
        elif wpm is not None and wpm < 60 and mlr is not None and mlr < 3:
            student.append({
                "type": "fluency",
                "text": "You're reading word by word. Try listening to the sentence first, "
                        "then read it in one smooth go.",
            })
            teacher.append({
                "type": "fluency",
                "text": f"Low WPM ({wpm:.0f}) + low MLR ({mlr:.1f}) — "
                        "word-by-word reading indicates formulation difficulty. "
                        "More listening practice before reading aloud recommended.",
            })
        elif wpm is not None and mlr is not None and mlr >= 6:
            student.append({
                "type": "success",
                "text": "You read very smoothly — nice flowing speech!",
            })

    if longest_phrase is not None and longest_phrase >= 8:
        student.append({
            "type": "success",
            "text": f"Your longest smooth phrase was {longest_phrase} words — well done!",
        })

    if fillers >= 3:
        student.append({
            "type": "fluency",
            "text": "You used some filler sounds like \"um\" or \"uh\". "
                    "That's okay — try to read without them next time.",
        })
    elif fillers == 0 and reps == 0:
        teacher.append({
            "type": "confidence",
            "text": "Zero fillers and zero repetitions — student reads confidently "
                    "even when making errors. Focus on pronunciation, not confidence.",
        })

    if reps >= 2:
        student.append({
            "type": "fluency",
            "text": "You repeated some words. That shows you're trying to get it right! "
                    "Practice will help you say it smoothly the first time.",
        })


def _generate_prosody_insights(
    student: list, teacher: list,
    stress_acc, intonation, npvi,
):
    """Prosody-specific insights."""
    if stress_acc is not None:
        if stress_acc < 40:
            student.append({
                "type": "prosody",
                "text": "Try to emphasize the right part of each word. "
                        "Listen to the sentence first and notice which parts are louder.",
            })
            teacher.append({
                "type": "prosody",
                "text": f"Stress accuracy {stress_acc:.0f}% — student is placing emphasis on wrong syllables. "
                        "Lexical stress is the #1 suprasegmental for intelligibility (Hahn 2004). "
                        "Targeted stress pattern drills recommended.",
            })
        elif stress_acc >= 75:
            student.append({
                "type": "success",
                "text": "You're putting emphasis on the right parts of words — sounds natural!",
            })

    if npvi is not None:
        if npvi < 40:
            student.append({
                "type": "prosody",
                "text": "Try making some parts of words longer and some shorter. "
                        "English has a rhythm — some bits are quick and some are slow.",
            })
            teacher.append({
                "type": "prosody",
                "text": f"nPVI-V = {npvi:.1f} (< 40) — very syllable-timed. "
                        "English target is 50-70. Student reads each syllable with equal length. "
                        "Rhythm exercises recommended.",
            })


# ── Dashboard / Trend Insights ──────────────────────────────────────────────

def generate_dashboard_insights(dashboard_data: dict) -> dict:
    """
    Generate insights from dashboard aggregated data.
    Returns {student: [...], teacher: [...]}.
    """
    student = []
    teacher = []

    sessions = dashboard_data.get("sessions", [])
    mc = dashboard_data.get("metric_cards", {})
    phoneme_errors = dashboard_data.get("phoneme_errors", [])
    vocabulary = dashboard_data.get("vocabulary", [])
    l1_preds = dashboard_data.get("l1_predictions", [])

    if len(sessions) < 2:
        student.append({
            "type": "encouragement",
            "text": "Keep practicing! After a few more sessions, "
                    "you'll start to see your progress here.",
        })
        return {"student": student, "teacher": teacher}

    # ── Progress trend ──────────────────────────────────────────────
    _generate_trend_insights(student, teacher, sessions)

    # ── Problem phonemes ────────────────────────────────────────────
    _generate_phoneme_insights(student, teacher, phoneme_errors, l1_preds)

    # ── Vocabulary insights ─────────────────────────────────────────
    mastered = [v for v in vocabulary if v.get("mastery") == "mastered"]
    struggling = [v for v in vocabulary if v.get("mastery") == "struggling"]

    if mastered:
        student.append({
            "type": "success",
            "text": f"You've mastered {len(mastered)} word{'s' if len(mastered) > 1 else ''}! "
                    + (f'Including: {", ".join(v["word"] for v in mastered[:3])}.' if mastered else ""),
        })

    if struggling:
        word_list = ", ".join(f'"{v["word"]}"' for v in struggling[:3])
        student.append({
            "type": "words",
            "text": f"These words need more practice: {word_list}.",
        })

    # ── Overall averages ────────────────────────────────────────────
    avg_acc = mc.get("avg_accuracy", 0)
    avg_flu = mc.get("avg_fluency", 0)
    avg_pro = mc.get("avg_prosody", 0)

    if avg_acc >= 70 and avg_flu < 50:
        teacher.append({
            "type": "diagnostic",
            "text": f"Overall pattern: good accuracy ({avg_acc}) but weak fluency ({avg_flu}). "
                    "Student knows the sounds but reads haltingly. More extensive reading practice "
                    "recommended to build automaticity.",
        })
    if avg_pro < 40 and avg_acc >= 50:
        teacher.append({
            "type": "diagnostic",
            "text": f"Segmental accuracy is acceptable ({avg_acc}) but prosody is weak ({avg_pro}). "
                    "Focus on suprasegmentals: stress patterns, intonation, and rhythm.",
        })

    return {"student": student, "teacher": teacher}


def _generate_trend_insights(student: list, teacher: list, sessions: list):
    """Insights from score trends over sessions."""
    if len(sessions) < 3:
        return

    # Compare first third vs last third
    n = len(sessions)
    third = max(n // 3, 1)
    early = sessions[:third]
    recent = sessions[-third:]

    early_avg = sum(s.get("total", 0) for s in early) / len(early)
    recent_avg = sum(s.get("total", 0) for s in recent) / len(recent)
    diff = recent_avg - early_avg

    if diff >= 10:
        student.append({
            "type": "success",
            "text": f"You're improving! Your score went from {early_avg:.0f} to {recent_avg:.0f}. "
                    "Keep it up!",
        })
        teacher.append({
            "type": "progress",
            "text": f"Overall score improved by {diff:.0f} points "
                    f"(from {early_avg:.0f} to {recent_avg:.0f} over {n} sessions).",
        })
    elif diff <= -10:
        student.append({
            "type": "encouragement",
            "text": "Your recent scores are a bit lower — that's okay! "
                    "Sometimes harder sentences are trickier. Keep practicing.",
        })
        teacher.append({
            "type": "progress",
            "text": f"Score declined by {abs(diff):.0f} points recently. "
                    "May indicate harder material or decreased practice frequency.",
        })

    # WPM trend
    early_wpm = [s.get("wpm", 0) for s in early if s.get("wpm")]
    recent_wpm = [s.get("wpm", 0) for s in recent if s.get("wpm")]
    if early_wpm and recent_wpm:
        early_wpm_avg = sum(early_wpm) / len(early_wpm)
        recent_wpm_avg = sum(recent_wpm) / len(recent_wpm)
        wpm_diff = recent_wpm_avg - early_wpm_avg
        if wpm_diff >= 15:
            student.append({
                "type": "success",
                "text": f"You're reading faster! From {early_wpm_avg:.0f} to "
                        f"{recent_wpm_avg:.0f} words per minute.",
            })


def _generate_phoneme_insights(
    student: list, teacher: list,
    phoneme_errors: list, l1_preds: list,
):
    """Insights from aggregated phoneme error data."""
    if not phoneme_errors:
        return

    # Worst phonemes (lowest accuracy)
    worst = [p for p in phoneme_errors if p.get("accuracy", 100) < 50][:5]
    if worst:
        friendly = ", ".join(_friendly_phone(p["phoneme"]) for p in worst[:3])
        student.append({
            "type": "pronunciation",
            "text": f"Your trickiest sounds are: {friendly}. "
                    "Focus on these when you practice.",
        })

    # L1 predicted vs actual
    confirmed = [p for p in l1_preds if p.get("predicted_difficult") and p.get("actual_accuracy", 100) < 60]
    if confirmed:
        phones = ", ".join(_friendly_phone(p["phoneme"]) for p in confirmed[:3])
        teacher.append({
            "type": "l1_transfer",
            "text": f"L1 transfer confirmed for: {phones}. "
                    "These are predicted difficult sounds for Tamil speakers and "
                    "the student is indeed struggling with them.",
        })

    surprises = [p for p in l1_preds if p.get("predicted_difficult") and p.get("actual_accuracy", 0) >= 80]
    if surprises:
        phones = ", ".join(_friendly_phone(p["phoneme"]) for p in surprises[:3])
        teacher.append({
            "type": "l1_transfer",
            "text": f"Positive surprise: {phones} were predicted difficult "
                    "but the student handles them well (>{80}% accuracy).",
        })


# ── Teacher Class-Level Insights ────────────────────────────────────────────

def generate_class_insights(analytics: dict) -> list[dict]:
    """
    Generate teacher insights for the whole class.
    Returns list of insight dicts.
    """
    insights = []
    learners = analytics.get("learners", [])
    common_phones = analytics.get("common_problem_phonemes", [])

    if not learners:
        return insights

    active = [l for l in learners if l.get("total_recordings", 0) > 0]
    inactive = [l for l in learners if l.get("total_recordings", 0) == 0]

    if inactive:
        names = ", ".join(l["display_name"] for l in inactive[:3])
        more = f" and {len(inactive) - 3} more" if len(inactive) > 3 else ""
        insights.append({
            "type": "engagement",
            "text": f"{len(inactive)} student(s) haven't practiced yet: {names}{more}.",
        })

    # Class-wide phoneme issues
    if common_phones:
        class_wide = [p for p in common_phones if p.get("learner_count", 0) >= max(len(active) // 2, 2)]
        if class_wide:
            phones = ", ".join(_friendly_phone(p["phoneme"]) for p in class_wide[:4])
            insights.append({
                "type": "class_pattern",
                "text": f"Most of the class struggles with: {phones}. "
                        "Consider a group lesson focused on these sounds.",
            })

    # Identify students who need attention
    if active:
        low_scorers = [l for l in active if (l.get("avg_score") or 0) < 40]
        if low_scorers:
            names = ", ".join(l["display_name"] for l in low_scorers[:3])
            insights.append({
                "type": "attention",
                "text": f"These students may need extra help: {names} (avg score < 40).",
            })

        high_scorers = [l for l in active if (l.get("avg_score") or 0) >= 80]
        if high_scorers:
            names = ", ".join(l["display_name"] for l in high_scorers[:3])
            insights.append({
                "type": "success",
                "text": f"Top performers: {names}. Consider challenging them with harder levels.",
            })

    return insights


# ── Student-Friendly Skill Bars ─────────────────────────────────────────────

def compute_skill_bars(data: dict, previous: dict | None = None) -> list[dict]:
    """
    Compute student-friendly skill bars from raw analysis data.

    Returns list of {name, value (0-100), stars (1-5), prev_stars (1-5 or null), delta}.
    Research mapping:
      Speed      = WPM normalized (60=low, 150=high for grade 6)
      Smoothness = MLR normalized (1=choppy, 8+=smooth) — Tavakoli 2020
      Sounds     = accuracy score (pronunciation correctness)
      Natural    = (stress_accuracy + intonation) / 2 — Hahn 2004, Kang 2010
      Confidence = 100 - penalty(fillers + reps) — Skehan 2009
      Complete   = completeness score
    """
    # Compute previous bars for delta comparison
    prev_bars = {}
    if previous:
        prev_list = compute_skill_bars(previous, previous=None)
        for pb in prev_list:
            prev_bars[pb["name"]] = pb

    bars = []

    # Speed — WPM mapped to 0-100 (60 WPM=20, 100 WPM=60, 140+ WPM=100)
    wpm = data.get("words_per_minute")
    if wpm is not None:
        speed_val = max(0, min(100, (wpm - 40) * (100 / 120)))
    else:
        speed_val = 0
    bars.append(_bar("speed", speed_val, prev_bars))

    # Smoothness — MLR mapped to 0-100 (MLR 1=0, MLR 4=50, MLR 8+=100)
    mlr = data.get("mean_length_of_run")
    if mlr is not None:
        smooth_val = max(0, min(100, (mlr - 1) * (100 / 7)))
    else:
        smooth_val = 0
    bars.append(_bar("smoothness", smooth_val, prev_bars))

    # Sounds — directly from accuracy
    acc = data.get("accuracy")
    bars.append(_bar("sounds", acc or 0, prev_bars))

    # Sounding Natural — avg of stress + intonation
    stress = data.get("stress_accuracy")
    intonation = data.get("intonation_accuracy")
    if stress is not None and intonation is not None:
        natural_val = (stress + intonation) / 2
    elif stress is not None:
        natural_val = stress
    elif intonation is not None:
        natural_val = intonation
    else:
        natural_val = data.get("prosody") or 0
    bars.append(_bar("natural", natural_val, prev_bars))

    # Confidence — based on fillers + repetitions (fewer = more confident)
    fillers = data.get("filler_count", 0) or 0
    reps = data.get("repetition_count", 0) or 0
    penalty = min(fillers * 15 + reps * 10, 100)
    conf_val = max(0, 100 - penalty)
    bars.append(_bar("confidence", conf_val, prev_bars))

    # Completeness — directly from score
    comp = data.get("completeness")
    bars.append(_bar("completeness", comp or 0, prev_bars))

    return bars


def _bar(name: str, value: float, prev_bars: dict) -> dict:
    """Build a single skill bar entry with optional delta from previous recording."""
    stars = _val_to_stars(value)
    entry = {"name": name, "value": round(value), "stars": stars}
    prev = prev_bars.get(name)
    if prev:
        entry["prev_stars"] = prev["stars"]
        entry["delta"] = stars - prev["stars"]
    else:
        entry["prev_stars"] = None
        entry["delta"] = 0
    return entry


def _val_to_stars(val: float) -> int:
    """Convert 0-100 value to 1-5 stars."""
    if val >= 90: return 5
    if val >= 70: return 4
    if val >= 50: return 3
    if val >= 30: return 2
    return 1
