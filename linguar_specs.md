# LinguAR — AR-Based Contextual Speech Learning System
## Full System Specification Document

**Version:** 3.0  
**Date:** February 26, 2026  
**Status:** Pre-Development  
**Target Publication:** Computers & Education / Computer Assisted Language Learning (CALL)  
**Revision Note:** Major pipeline overhaul — all analysis components now grounded in 2024–2025 CAPT literature. v3.0: Silero VAD removed from fluency pipeline (CrisperWhisper handles all fluency analysis); cloud GPU deployment architecture added for multi-user classroom use (50 concurrent learners). See changelog at end of document.

---

## 1. Project Vision

LinguAR is an AR-based language learning system where a learner points their camera at real-world objects, the system detects them using YOLO11, serves contextual sentences at appropriate difficulty levels from a pre-generated sentence bank, and the learner reads those sentences aloud. The system then performs multi-level speech analysis — phoneme-level pronunciation scoring, mispronunciation detection and diagnosis, prosodic assessment, reading accuracy, and fluency assessment — providing instant feedback and tracking progress over time through an analytics dashboard.

The system uses a split architecture: the YOLO11s object detection model runs entirely in-browser (ONNX Runtime Web) for instant visual feedback, while the speech analysis pipeline (CrisperWhisper verbatim ASR, HuBERT retrieval-based mispronunciation detection, Montreal Forced Aligner phoneme segmentation, parselmouth prosody extraction, CrisperWhisper disfluency-based fluency analysis) runs on a cloud GPU backend for fast inference. No camera feeds ever leave the device; audio is transmitted only to the user's own backend server for processing. The system supports up to 50 concurrent learners on a single T4 GPU instance.

### 1.1 Core Learning Loop

```
┌──────────────────────────────────────────────────────────────┐
│                    THE CORE LEARNING LOOP                     │
│                                                              │
│   1. SCAN ──→ Camera detects real-world object(s) via YOLO11   │
│                         │                                     │
│   2. GENERATE ──→ Sentence bank serves contextual sentences    │
│                   (adapted to learner's level + weak areas)   │
│                         │                                     │
│   3. READ ──→ Learner reads sentence aloud                   │
│                         │                                     │
│   4. ANALYZE ──→ CrisperWhisper transcribes (verbatim)     │
│                  HuBERT detects mispronunciations (MDD)    │
│                  MFA + parselmouth scores prosody           │
│                  CrisperWhisper assesses fluency              │
│                         │                                     │
│   5. FEEDBACK ──→ Instant pronunciation score + highlights   │
│                   TTS comparison audio available              │
│                         │                                     │
│   6. ADAPT ──→ Problem sounds feed into next generation      │
│                Spaced repetition schedules practice           │
│                Difficulty auto-adjusts                         │
│                         │                                     │
│               └──────── LOOP REPEATS ────────┘               │
└──────────────────────────────────────────────────────────────┘
```

### 1.2 Key Innovation Claims (For Publication)

1. **No published system combines real-time object detection with phoneme-level pronunciation assessment in a single pipeline.** Existing AR language tools (ARbis Pictus, ARTranslate, LingoLens) handle vision-to-vocabulary only. Existing CAPT systems handle speech-to-feedback only. LinguAR bridges this gap.

2. **Contextual sentences triggered by detected objects is novel.** No system generates practice sentences from visually detected real-world objects — whether dynamically or from a curated bank.

3. **Functional load-weighted intelligibility scoring is unprecedented in automated CAPT.** Despite decades of theoretical support (Catford 1987; Munro & Derwing 2006; Kang & Moran 2014), no existing automated pronunciation assessment system implements functional load weighting in its scoring algorithm. This operationalizes the Intelligibility Principle (Levis, 2005) — the field has called for this but no one has delivered it.

4. **Multi-object scene description for grammar/syntax teaching** is unprecedented in AR language learning.

5. **Literature-grounded multi-dimensional scoring.** Unlike commercial systems that output opaque single scores, LinguAR reports accuracy, completeness, fluency, and prosody as independent dimensions with traceable weights derived from applied linguistics research (SpeechOcean762 framework, CEFR 2018 phonological descriptors, Skehan 2009 fluency model, Grabe & Low 2002 rhythm metrics).

6. **Edge/browser-based ML deployment** for CAPT with full privacy preservation (no voice or camera data leaves the device).

---

## 2. System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         FRONTEND LAYER                               │
│                                                                      │
│  ┌─────────────────┐  ┌──────────────────┐  ┌───────────────────┐  │
│  │  AR Scanner      │  │  Practice Mode   │  │  Learner          │  │
│  │  (scan.html)     │  │  (practice.html) │  │  Dashboard        │  │
│  │                  │  │                  │  │  (dashboard.html) │  │
│  │  - YOLO11s ONNX  │  │  - Manual word   │  │  - Progress       │  │
│  │  - Camera feed   │  │    selection     │  │  - Problem sounds │  │
│  │  - Multi-object  │  │  - Conversation  │  │  - Vocab mastery  │  │
│  │  - Bounding box  │  │    scaffolding   │  │  - Streaks/XP     │  │
│  │  - Audio record  │  │  - Minimal pairs │  │  - Level (CEFR)   │  │
│  └─────────────────┘  └──────────────────┘  └───────────────────┘  │
│                                                                      │
│  ┌─────────────────┐  ┌──────────────────┐  ┌───────────────────┐  │
│  │  Review Page     │  │  Teacher         │  │  Home / Onboard   │  │
│  │  (review.html)   │  │  Dashboard       │  │  (index.html)     │  │
│  │                  │  │  (teacher.html)  │  │                   │  │
│  │  - Session stats │  │  - Class overview│  │  - L1 selection   │  │
│  │  - Replay audio  │  │  - Assignments   │  │  - Level test     │  │
│  │  - TTS compare   │  │  - Student list  │  │  - Daily goals    │  │
│  │  - Per-word GOP  │  │  - Problem areas │  │  - Feature cards  │  │
│  └─────────────────┘  └──────────────────┘  └───────────────────┘  │
└──────────────────────────────┬──────────────────────────────────────┘
                               │ HTTP API
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      BACKEND API (FastAPI)                            │
│                                                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────────────────┐    │
│  │ Session Mgmt │  │ Prompt Gen   │  │ Analysis Router        │    │
│  │              │  │              │  │                        │    │
│  │ /session/*   │  │ /generate-*  │  │ /record (main pipe)   │    │
│  │ /learner/*   │  │ /scene-desc  │  │ /recording/{id}       │    │
│  │ /class/*     │  │ /dialogue    │  │ /learner/progress     │    │
│  │              │  │ /minimal-pair│  │ /learner/vocabulary    │    │
│  └──────────────┘  └──────────────┘  └────────────────────────┘    │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    ML ANALYSIS PIPELINE                               │
│                                                                      │
│  ┌──────────────┐ ┌─────────────┐ ┌────────────┐ ┌──────────────┐  │
│  │ CrisperWhis- │ │ HuBERT      │ │ MFA +      │ │ CrisperWhis- │  │
│  │ per ASR      │ │ MDD Engine  │ │ parselmouth│ │ per Fluency  │  │
│  │              │ │             │ │            │ │              │  │
│  │ Verbatim     │ │ Retrieval-  │ │ Phoneme    │ │ Disfluency   │  │
│  │ transcript + │ │ based MDD   │ │ alignment  │ │ detection    │  │
│  │ word timing  │ │ GOP Scores  │ │ F0/pitch   │ │ Pause timing │  │
│  │ + disfluency │ │ FL-weighted │ │ Stress det.│ │ Speech rate  │  │
│  │ detection    │ │ intelli-    │ │ nPVI rhythm│ │ Repair       │  │
│  │              │ │ gibility wt │ │            │ │ fluency      │  │
│  └──────────────┘ └─────────────┘ └────────────┘ └──────────────┘  │
│                                                                      │
│  ┌──────────────┐ ┌──────────────────┐ ┌──────────────────────────┐│
│  │ Word-Level   │ │ Hierarchical     │ │ Adaptive Engine          ││
│  │ Alignment    │ │ Scorer           │ │                          ││
│  │              │ │ (phone→word→utt) │ │ - Spaced repetition      ││
│  │ jiwer edit   │ │                  │ │ - L1 transfer predictor  ││
│  │ distance:    │ │ 4 dimensions:    │ │ - Difficulty auto-adjust ││
│  │ C/S/D/I/R    │ │ Accuracy, Fluency│ │ - Minimal pair generator ││
│  │ per word     │ │ Prosody, Total   │ │ - Problem sound tracker  ││
│  └──────────────┘ └──────────────────┘ └──────────────────────────┘│
│                                                                      │
│  ┌──────────────────┐                                               │
│  │ TTS Engine       │                                               │
│  │ (Reference Audio)│                                               │
│  │                  │                                               │
│  │ - Generate model │                                               │
│  │   pronunciation  │                                               │
│  │ - Serve for      │                                               │
│  │   comparison     │                                               │
│  └──────────────────┘                                               │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      DATA PERSISTENCE                                │
│                 (SQLite local / PostgreSQL hosted)                    │
│                                                                      │
│  recordings ─── learner_vocabulary ─── spaced_repetition_queue      │
│  learner_profiles ─── class_assignments ─── daily_progress          │
│  generated_prompts ─── session_progress ─── l1_transfer_patterns    │
│                                                                      │
│  + Redis (task queue, result cache, rate limiting) [hosted mode]     │
│  + S3/MinIO (audio files, TTS cache, MFA TextGrids) [hosted mode]   │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.1 Tech Stack

| Layer | Technology | Purpose | Literature Basis |
|---|---|---|---|
| Backend Framework | FastAPI + Uvicorn | REST API, serves frontend, orchestrates ML pipeline | — |
| ASR | CrisperWhisper (nyrahealth/CrisperWhisper, transformers pipeline) | Verbatim speech-to-text with accurate word-level timestamps, disfluency detection | Wagner et al. (Interspeech 2024) — standard Whisper normalizes L2 errors; CrisperWhisper preserves fillers, stutters, false starts |
| Mispronunciation Detection | HuBERT (facebook/hubert-large-ls960-ft) retrieval-based MDD | Training-free mispronunciation detection and diagnosis, GOP scoring | Tu et al. (arXiv 2025) — F1 69.60% on L2-ARCTIC without task-specific training; HuBERT outperforms Wav2Vec2 and WavLM for MDD |
| Forced Alignment | Montreal Forced Aligner (MFA 3.x) | Phoneme-level time boundaries for prosody analysis, vowel/consonant segmentation | McAuliffe et al. (2017); Rousso et al. (2024) — median boundary deviation 12.5ms on TIMIT; Wu et al. (2023) validated MFA for prosody research |
| Prosody Analysis | parselmouth (Praat wrapper) + CREPE pitch tracker | F0 extraction, intensity, formants, lexical stress, intonation contour | Boersma & Weenink (2001) for Praat; Kim et al. (2018) for CREPE — sub-cent pitch accuracy; Tavakoli et al. (2020) for fluency-prosody constructs |
| Voice Activity Detection | Silero VAD (browser-side only, ONNX) | Browser-side recording utility: auto-detect speech onset/offset to trim recordings before server upload; quick phonation-time ratio check. NOT used in server-side fluency analysis pipeline. | — |
| Reading Accuracy | jiwer word-level edit distance alignment | Word-level classification: correct/substitution/deletion/insertion/repetition | Standard in all competitive CAPT systems (Azure PA, SpeechAce, Duolingo); Zhang et al. (2021) SpeechOcean762 completeness metric |
| Object Detection | YOLO11s ONNX (browser via ONNX Runtime Web) | Client-side real-time object detection (80 COCO classes) | YOLO11 (Ultralytics, Sep 2024): 47.0 mAP on COCO (+10 over YOLOv8n), 9.4M params, ~38MB ONNX, ~20 FPS in-browser via WASM; same export + ONNX Runtime Web pipeline as v8 |
| Sentence Generation | Pre-generated sentence bank (JSON) + optional Ollama (gemma2:2b) for local dev/authoring | Batch-generated graded sentences per object per difficulty level; curated for phoneme coverage and pedagogical control. Ollama used only offline during sentence authoring, NOT at runtime. | — |
| TTS Engine | Piper TTS (primary) / espeak-ng (fallback) | Reference pronunciation audio generation | — |
| Database | SQLite (local) / PostgreSQL (hosted) + SQLAlchemy ORM | Learner data, analytics, prompt caching; PostgreSQL for concurrent multi-user writes | — |
| Frontend | Vanilla HTML5 + JS + Chart.js | No framework dependency, lightweight, offline-capable | — |
| Audio Processing | PyAV (bundled FFmpeg), noisereduce, Web Audio API | Format conversion, noise reduction, silence detection | — |
| Phoneme Dictionary | CMU Pronouncing Dictionary (134,000+ words) + g2p-en seq2seq G2P (for OOV words) | Word-to-phoneme lookup with unified ARPAbet output | Weide (1998) for CMUdict; g2p-en trained on CMUdict avoids phoneset inconsistency introduced by espeak-ng IPA fallback |

### 2.2 Deployment Architecture (Cloud GPU, 50 Concurrent Learners)

The system uses a split architecture: lightweight browser-side components (YOLO11s, audio recording, Silero VAD for recording auto-trim) run on the learner's device, while compute-heavy ML inference runs on a single cloud GPU server. This is sized for a pilot study with up to 50 primary school children in a classroom setting.

```
┌─────────────────────────────────────────────────────────────────┐
│                    LEARNER DEVICES (browser)                       │
│                                                                    │
│  YOLO11s ONNX (in-browser, ~38MB loaded once)                    │
│  Silero VAD ONNX (in-browser, ~1MB) — auto-trim recordings       │
│  Audio recording (MediaRecorder API → WebM → server)              │
│  UI: scan page, practice page, dashboard                          │
│                                                                    │
│  Up to 50 concurrent browser sessions                             │
└───────────────────────────┬─────────────────────────────────────┘
                            │ HTTPS (audio upload ~50-200KB per recording)
┌───────────────────────────▼─────────────────────────────────────┐
│           CLOUD GPU SERVER (single T4/A10G instance)               │
│                                                                    │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │  FastAPI (Uvicorn, 4 workers)                              │    │
│  │  - User auth (simple session/JWT per learner)              │    │
│  │  - Audio upload, validation, format conversion             │    │
│  │  - Enqueues analysis jobs to Redis                         │    │
│  │  - Serves frontend static files                            │    │
│  │  - Sentence lookup (pre-generated bank, no LLM at runtime)   │    │
│  │  - Returns job_id → client polls for results               │    │
│  └────────────────────────────┬─────────────────────────────┘    │
│                               │ Redis (task broker)               │
│  ┌────────────────────────────▼─────────────────────────────┐    │
│  │  Celery Worker (1 worker, 1 GPU)                           │    │
│  │                                                             │    │
│  │  Models loaded ONCE at startup:                             │    │
│  │    CrisperWhisper  (~3.0 GB VRAM)                          │    │
│  │    HuBERT-large    (~1.5 GB VRAM)                          │    │
│  │    MFA engine      (~0.5 GB RAM)                           │    │
│  │    parselmouth     (~0.1 GB RAM)                           │    │
│  │                                                             │    │
│  │  Total: ~5.0 GB VRAM (fits T4 16GB with headroom)          │    │
│  │  Throughput: ~8-12 utterances/minute                        │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                    │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │  PostgreSQL + Redis                                         │    │
│  │  - Learner profiles, session data, all scores               │    │
│  │  - Audio files stored on local disk (lifecycle cleanup)     │    │
│  └──────────────────────────────────────────────────────────┘    │
└────────────────────────────────────────────────────────────────┘
```

**Concurrency analysis for 50 learners:**

```
Learning cycle per child: ~45-60 seconds
  Scan object:     15-20s (browser-only, no server load)
  Read/record:      5-10s (browser-only until submission)
  Wait for results:  8-15s (GPU processing)
  Review feedback:  10-20s (browser-only)

Peak concurrent submissions: 50 × ~15% = ~6-8 simultaneous
GPU processing per utterance: ~6-8s on T4
Queue clearance for burst of 8: ~50-65s
Average wait time at peak: ~15-25s ← acceptable for children
```

**Cloud GPU cost estimate:**

| Provider | GPU | Cost/hr | 3-hour classroom session |
|---|---|---|---|
| Google Cloud (g2-standard-4 + T4) | T4 16GB | ~$0.35/hr | ~$1.05 |
| AWS (g4dn.xlarge) | T4 16GB | ~$0.53/hr | ~$1.59 |
| Vast.ai (community) | T4 16GB | ~$0.15-0.30/hr | ~$0.45-0.90 |
| Lambda Labs | A10G 24GB | ~$0.60/hr | ~$1.80 |

**Scaling note:** If wait times exceed 25s consistently (e.g., children are faster than expected), upgrading from T4 to A10G (~2× throughput) or adding a second Celery worker (requires A10G 24GB to fit two model copies) resolves this. For studies with 80-100+ children, use 2 T4 instances behind a load balancer.

**Key design decisions:**

| Decision | Rationale |
|---|---|
| **Async job queue (Celery + Redis)** | Analysis takes 6-8s; blocking the API would starve other users. Client submits audio, gets job_id, polls for result |
| **PostgreSQL over SQLite** | SQLite allows only one concurrent writer; 50 children writing simultaneously requires PostgreSQL row-level locking |
| **Models loaded once at worker startup** | Loading ~5GB of models per-request would add 30-60s latency; singleton pattern keeps them in VRAM |
| **Single worker, single GPU** | 50 kids is well within one T4's capacity; no need for orchestration complexity |
| **Silero VAD browser-only** | Speech onset detection for auto-trim needs real-time local processing; server-side fluency uses CrisperWhisper timestamps instead |

**Single-user local mode (development/research):** The system supports single-user local mode by running all components in one process (FastAPI + models loaded in-process + SQLite), controlled by a `DEPLOYMENT_MODE=local|hosted` environment variable. The Celery queue is bypassed in local mode — analysis runs synchronously in the request handler. This mode requires a local NVIDIA GPU for acceptable inference speed.

**Docker Compose (hosted mode):**

```yaml
services:
  api:         # FastAPI gateway (CPU, lightweight)
  worker:      # Celery ML worker (GPU, single instance)
  redis:       # Task broker + result cache
  postgres:    # Primary database (concurrent user writes)
  nginx:       # Reverse proxy + SSL termination
```

---

## 3. Component Specifications

### 3.1 AR OBJECT DETECTION (scan.html)

The AR interface is the system's primary interaction point. The learner opens the camera, points at real-world objects, and the system identifies them for contextual language practice.

#### 3.1.1 Object Detection Pipeline

```
Camera feed (getUserMedia API, rear camera on mobile)
        │
        ▼
YOLO11s ONNX model (~38 MB, loaded once)
Running in-browser via ONNX Runtime Web (WASM backend, WebGPU where available)
        │
        ▼
Detection output:
  - Object class (80 COCO classes: bottle, cup, phone, book, laptop, etc.)
  - Bounding box coordinates (x, y, width, height)
  - Confidence score (0-1)
        │
        ▼
Bounding box overlay drawn on canvas
Confidence score displayed
        │
        ▼
"Generate Sentences" button triggers prompt generation
```

**Why YOLO11s over YOLOv8n:** YOLO11 (Ultralytics, September 2024) achieves 47.0 mAP on COCO vs YOLOv8n's 37.3 — a +10 mAP improvement that translates to substantially better detection of smaller objects, partially occluded items, and objects at odd angles. The "s" (small) variant is chosen over "n" (nano) because the ~38MB model size is acceptable for a one-time download in a web app, and the mAP difference (47.0 vs 39.5) meaningfully impacts user experience. YOLO11s uses 22% fewer parameters than YOLOv8m while achieving higher accuracy. Export to ONNX is identical (`model.export(format="onnx")`) and the ONNX Runtime Web inference pipeline requires zero code changes beyond swapping the model file.

**Supported object classes include:** person, bicycle, car, motorcycle, bus, bottle, cup, fork, knife, spoon, bowl, banana, apple, orange, sandwich, pizza, chair, couch, bed, dining table, toilet, TV, laptop, mouse, remote, keyboard, cell phone, book, clock, vase, scissors, teddy bear, toothbrush, and 47 more COCO categories.

#### 3.1.2 Multi-Object Detection

When 2+ objects are detected simultaneously, the system computes spatial relationships from bounding box positions for scene description generation (see Section 3.2.2).

```
Spatial relationship computation:
  - Compare bounding box center coordinates pairwise
  - X-axis: left-of / right-of / next-to (if <15% frame width apart)
  - Y-axis: above / below / same-level (if <10% frame height apart)
  - Overlap: in-front-of / behind (if boxes overlap >20%)
```

#### 3.1.3 Audio Recording Integration

Recording is integrated directly into the AR interface:

- Browser captures audio using MediaRecorder API (WebM format)
- Client-side VAD detects 900ms of silence → auto-stops recording
- Maximum recording duration: 8 seconds timeout
- Audio blob is sent to backend via `POST /record`
- Backend converts WebM → WAV (16kHz mono) using PyAV for ML model compatibility

---

### 3.2 SENTENCE GENERATION (Pre-Generated Bank)

The prompt generation system serves contextual, graded sentences for detected objects from a **pre-generated sentence bank** (`data/sentence_bank.json`). All sentences are batch-authored offline (using any LLM or manually) and curated for vocabulary control, phoneme coverage, and age-appropriateness. **No LLM runs at runtime** — this eliminates a deployment dependency and ensures consistent, reproducible content across all learners (critical for controlled research studies).

**How the AR interaction works (unchanged):**
```
Kid points camera at bottle  →  YOLO11s detects "bottle" in real-time (in-browser)
                              →  System looks up "bottle" in sentence_bank.json
                              →  Selects sentence at learner's difficulty level
                              →  Displays: "Could you pass me the bottle, please?"
                              →  Kid reads aloud → speech analysis → feedback
```
The AR experience is the **real-time object detection triggering contextual content** — the child sees the sentence appear moments after pointing at the object. Whether that sentence was authored by an LLM last week or selected from a curated bank is invisible to the learner.

**Why a pre-generated bank (not a runtime LLM):**
- YOLO11s detects from a fixed 80 COCO classes → sentence space is fully pre-computable (~80 objects × 5 levels × 10 variants = 4,000 sentences)
- No Ollama/gemma2 dependency on server → simpler deployment, lower RAM, no GPU contention with speech models
- Pre-generated sentences can be pedagogically reviewed before deployment
- Research studies require controlled stimuli — dynamic LLM output introduces an uncontrolled variable
- Zero latency: JSON lookup vs. ~2-5s LLM generation per request

**Sentence bank structure:**

```json
// data/sentence_bank.json — ~80 objects × 5 levels × 10 sentences = 4,000 entries
{
  "bottle": {
    "beginner": [
      {"sentence": "This is a bottle.", "grammar": "simple present, articles", "target_phonemes": ["b", "aa", "t", "l"]},
      {"sentence": "The bottle is blue.", "grammar": "adjectives", "target_phonemes": ["b", "l", "uw"]},
      ...
    ],
    "elementary": [...],
    "intermediate": [...],
    "upper_intermediate": [...],
    "advanced": [...]
  },
  "cup": { ... },
  ...
}
```

**Authoring workflow (one-time, offline):**
1. Run `scripts/generate_sentence_bank.py` — calls Ollama/gemma2 (or any LLM, or ChatGPT API) locally to batch-generate 10 sentences per object per level
2. Teacher/researcher reviews and edits generated sentences for quality, age-appropriateness, phoneme coverage, and vocabulary level
3. Output: `data/sentence_bank.json` deployed with the application
4. To add sentences for new objects or scenarios: re-run the script for those objects only, or manually add entries to the JSON

#### 3.2.1 Single-Object Contextual Sentence Escalation

When YOLO11 detects an object (e.g., "bottle"), the system selects a sentence from the bank at the learner's current level:

| Level | CEFR | Example for "bottle" | Grammar Focus |
|---|---|---|---|
| Beginner | A1–A2 | "This is a bottle." | Simple present, articles |
| Elementary | A2–B1 | "The water bottle is on the table." | Prepositions, adjectives |
| Intermediate | B1–B2 | "Could you pass me the bottle, please?" | Modals, politeness forms |
| Upper-Int. | B2–C1 | "She forgot her reusable bottle at the restaurant yesterday." | Past tense, compound sentences |
| Advanced | C1–C2 | "Had I remembered to bring my bottle, I wouldn't have had to buy a plastic one." | Conditionals, subjunctive |

**Sentence selection logic (runtime, ~1ms):**

```
1. Look up object_name in sentence_bank.json
2. Filter by learner's current difficulty level
3. If learner has known problem phonemes → prefer sentences tagged with those phonemes
4. Exclude sentences already practiced in this session (track by sentence hash)
5. Random selection from remaining candidates
6. Return: {sentence, grammar_focus, target_phonemes}
```

**Authoring prompt template (used OFFLINE to generate the bank, NOT at runtime):**

```
You are a language learning content generator for primary school children (ages 8-12).
Generate 10 English sentences about the object "{object_name}" at {difficulty_level} level.

Requirements:
- Sentences must naturally include the word "{object_name}"
- Each sentence should introduce different grammar patterns
- Include diverse phoneme combinations for pronunciation practice
- Sentences should be natural and conversational, not textbook-like
- Age-appropriate for primary school children
- Return as JSON array with fields: sentence, grammar_focus, target_phonemes
```

**Key design decisions:**
- Problem phonemes from the learner's history are used to SELECT sentences from the bank (not generate them dynamically)
- Each sentence is tagged with its target phonemes during authoring, enabling phoneme-targeted selection at runtime
- Teachers can add custom sentences to the bank via a simple JSON edit or admin interface
- The bank is extensible: objects not in the pre-generated set fall back to generic templates ("I can see a {object}. The {object} is {color}.")

#### 3.2.2 Multi-Object Scene Description Mode

When 2+ objects are detected simultaneously, the system generates relational sentences using **template composition with spatial slot-filling** from pre-authored scene templates:

```
Camera detects: [bottle (x:120, y:200), laptop (x:400, y:180), book (x:600, y:220)]
                                    │
           Bounding box positions converted to spatial relationships:
           bottle = LEFT, laptop = CENTER, book = RIGHT
           bottle ≈ same height as laptop (NEXT TO)
           book ≈ same height as laptop (NEXT TO / BESIDE)
                                    │
        Template slot-filling from data/scene_templates.json:
                                    │
           ▼                        ▼                        ▼
    Beginner:                Intermediate:              Advanced:
    "I see a bottle,        "The bottle is next to     "Between the laptop and
    a laptop, and           the laptop, and the        the book sits a water
    a book."                book is on the right."     bottle that she always
                                                        carries to the library."
```

**Implementation details:**
- Extract bounding box center coordinates from YOLO11 output
- Compute pairwise spatial relationships (left-of, right-of, above, below, next-to)
- Select from pre-authored scene templates in `data/scene_templates.json` with relationship slots: `"The {obj1} is {relation} the {obj2}."`
- Templates graded by difficulty level, covering prepositions (on, next to, between, behind, above, under, near)
- **Research value:** No existing AR language learning system generates relational grammar from multi-object detection

#### 3.2.3 Conversation Scaffolding Mode

After individual sentence practice, the system can generate short dialogues involving the detected object:

```
[Object detected: cup]

System displays Dialogue:
─────────────────────────────────
Speaker A (Learner reads):    "Would you like a cup of tea?"
Speaker B (System displays):  "Yes, please. With milk and sugar."
Speaker A (Learner reads):    "Here you go. Be careful, the cup is hot."
Speaker B (System displays):  "Thank you! This is just what I needed."
─────────────────────────────────

Flow: Learner records line → System analyzes → Displays next line → Learner records → ...
```

**Design:**
- Pre-authored 2-4 turn dialogue exchanges per object per level, stored in `data/dialogue_bank.json`
- Frontend alternates between display-only turns (the other speaker) and record-and-analyze turns (the learner)
- Backend tracks which lines are learner-produced vs system-displayed
- Moves learning from isolated reading practice to conversational rehearsal, aligned with Communicative Language Teaching (CLT) principles

#### 3.2.4 Minimal Pair Targeting from Error Data

When the phoneme analysis detects a specific confusion (e.g., /b/ → /p/), the system selects sentences containing minimal pairs for that contrast from the sentence bank.

```
Detected error: learner confuses /ɪ/ and /iː/
                        │
         Minimal pair database lookup:
         ship/sheep, sit/seat, bit/beat, fill/feel, lid/lead
                        │
         Sentence bank filtered by phoneme tags:
         Select sentences containing /ɪ/ and /iː/ minimal pair words
                        │
         Selected sentence (from pre-authored bank):
         "The sheep on the ship needed a seat to sit on."
```

**Design:**
- Curated minimal pair database (`data/minimal_pairs.json`) indexed by phoneme contrast
- After each session, the system queries the learner's top 3 problem phoneme pairs
- Minimal pair words used as filter criteria when selecting sentences from the bank
- Pre-authored minimal pair sentences in `data/sentence_bank.json` tagged with their contrasting phonemes
- Minimal pair mastery is tracked separately in the vocabulary database
- Minimal pair practice is a gold-standard technique in pronunciation teaching with strong empirical support in SLA literature

---

### 3.3 SPEECH ANALYSIS PIPELINE

When the learner records a sentence, the audio passes through a multi-stage analysis pipeline.

#### 3.3.1 Audio Preprocessing

```
Input: WebM blob from browser
            │
            ▼
   PyAV (bundled FFmpeg) converts to WAV
   Resamples to 16kHz mono (required by all ML models)
            │
            ▼
   Optional noise reduction (noisereduce library, spectral gating)
            │
            ▼
   Saved to storage/audio/{session_id}_{timestamp}.wav
```

#### 3.3.2 Automatic Speech Recognition (CrisperWhisper)

CrisperWhisper transcribes the learner's speech verbatim — preserving fillers, stutters, false starts, and hesitations that standard Whisper suppresses. This is critical for L2 assessment because standard Whisper acts as a normalizing transcriber, actively removing disfluencies and correcting mispronunciations (Cai, 2025, *Language Learning*; Ballier et al., ICNLSP 2023). CrisperWhisper was specifically developed to address this limitation and was accepted at Interspeech 2024.

- **Model:** nyrahealth/CrisperWhisper (transformers pipeline, not faster-whisper — the CTranslate2 conversion loses timestamp accuracy)
- **Output:** Verbatim transcript + accurate word-level timestamps + detected disfluencies (fillers: "um"/"uh", stutters, false starts)
- **Language:** Forced English (prevents false language detection for L2 speakers)

```
Example output:
{
  "text": "Could you um pass me the the battle please",
  "word_timings": [
    {"word": "Could", "start": 0.0, "end": 0.28, "type": "word"},
    {"word": "you", "start": 0.28, "end": 0.45, "type": "word"},
    {"word": "um", "start": 0.52, "end": 0.71, "type": "filler"},
    {"word": "pass", "start": 0.80, "end": 1.05, "type": "word"},
    {"word": "me", "start": 1.05, "end": 1.20, "type": "word"},
    {"word": "the", "start": 1.25, "end": 1.35, "type": "word"},
    {"word": "the", "start": 1.38, "end": 1.48, "type": "repetition"},
    {"word": "battle", "start": 1.50, "end": 1.85, "type": "word"},
    {"word": "please", "start": 1.90, "end": 2.20, "type": "word"}
  ]
}
```

**Why CrisperWhisper over standard Whisper:** A 2025 proficiency-aware study found standard Whisper-small produces ~17% WER on A2-level speech but under 8% on C1 — not because it detects errors better at lower levels, but because its language model more aggressively "corrects" what learners actually say. CrisperWhisper's verbatim output directly enables the word-level alignment approach (Section 3.3.5), since it will not silently correct substitutions like "battle" for "bottle."

**Role boundary:** CrisperWhisper is used exclusively for transcription, word timing, and disfluency detection. It is NOT used for mispronunciation detection or phonetic error diagnosis — that role belongs to HuBERT (Section 3.3.3).

#### 3.3.3 Mispronunciation Detection and Diagnosis (HuBERT Retrieval-Based MDD)

The core pronunciation assessment uses a training-free retrieval-based approach with HuBERT, following Tu et al. (arXiv 2025) which achieved F1 of 69.60% on L2-ARCTIC — the best current result without any task-specific training. Among HuBERT, WavLM, and Wav2Vec2, HuBERT achieves the best MDD performance (Tu et al., 2025), and self-supervised speech models display human-like cross-linguistic perceptual abilities that make them well-suited to L2 assessment (Millet et al., 2024).

**Model:** facebook/hubert-large-ls960-ft (HuggingFace, pre-trained on 60K hours, fine-tuned on LibriSpeech 960h for ASR)

**Retrieval-Based MDD Process:**

```
ONE-TIME SETUP (Phoneme Embedding Pool Construction):
  1. Sample ~500 native speech utterances from L2-ARCTIC training split
  2. For each utterance, extract HuBERT embeddings (frame-level, layer 21)
  3. Align with canonical phoneme sequences using forced alignment
  4. Store (embedding, phoneme_label) pairs as the retrieval pool
  → Pool contains ~200K frame-embedding-to-phoneme mappings

PER-UTTERANCE INFERENCE:
  1. Load learner audio waveform (16kHz)
  2. Extract HuBERT frame-level embeddings
  3. For each frame t:
     a. Retrieve k=10 nearest neighbors from the pool (cosine similarity)
     b. Filter by similarity threshold τ=0.7
     c. Majority vote among retrieved phoneme labels → predicted phoneme
  4. Collapse consecutive duplicates + remove blanks → predicted phoneme sequence
  5. Align predicted sequence with canonical phoneme sequence (Needleman-Wunsch)
  6. Classify each position: CORRECT / SUBSTITUTION(p→q) / DELETION / INSERTION
```

**Goodness of Pronunciation (GOP) Scoring:**

GOP is computed from HuBERT's CTC logits (the GOP calculation is model-agnostic — Witt & Young, 2000):

```
GOP(p) = (1/T) × Σ_t log P(p | audio_features_t)

Where:
  p = expected phoneme
  T = number of frames assigned to this phoneme (from MFA alignment)
  P = posterior probability from HuBERT's CTC output layer

Interpretation (following Hu et al., 2015 calibration):
  GOP ≈ 0:   Excellent pronunciation (high model confidence)
  GOP ≈ -1:  Good pronunciation
  GOP ≈ -2:  Fair pronunciation
  GOP < -3:  Poor pronunciation

Advantage: Works directly on audio, not dependent on ASR transcription accuracy.
```

**IPA to ARPAbet Conversion:**
- HuBERT with the ASR head outputs token sequences; phoneme labels come from the retrieval pool
- A mapping layer converts between IPA (from the pool's MFA-derived labels) and ARPAbet (for CMU dictionary comparison)

**ML-Based Phoneme Error Rate (PER):**

```
1. Get expected phonemes from CMU dictionary for each word
   - Primary lookup: CMU Pronouncing Dictionary (134K+ words, ARPAbet)
   - OOV fallback: g2p-en seq2seq model (trained on CMUdict, outputs ARPAbet)
   - NOTE: espeak-ng is NOT used as G2P fallback (avoids IPA/ARPAbet phoneset mixing)
2. Get detected phonemes from HuBERT retrieval-based MDD
3. Align sequences using Needleman-Wunsch dynamic programming
4. Count substitutions, insertions, deletions

PER = (S + D + I) / N

Example:
  Expected: [DH, AH, B, AE, G]  ("the bag")
  Detected: [DH, AH, B, AE, K]  (from HuBERT MDD)
  Alignment: [(DH,DH), (AH,AH), (B,B), (AE,AE), (G,K)]
  PER = 1/5 = 0.20 (one substitution: G→K, voiced→voiceless velar stop)
```

**CMU Dictionary Acknowledged Limitations (for publication):**
- No allophonic variation (aspirated vs. unaspirated stops, flapping, dark-L)
- North American English pronunciations only
- No connected speech phenomena (linking, elision, assimilation)
- Coarse 39-phone granularity that cannot capture sub-phonemic errors
- Mitigated by: g2p-en for OOV (instead of phoneset-inconsistent espeak-ng), and by the fact that the intelligibility-focused scoring explicitly tolerates allophonic variation

**Phonetic Distance Calculation:**

Each phoneme error is further analyzed by articulatory distance, following established phonological feature geometry (Chomsky & Halle, 1968; Clements, 1985):

```
Consonant features:
  - Voicing: voiced vs voiceless (weight: 0.15)
  - Place: bilabial, labiodental, dental, alveolar, palatal, velar, glottal (weight: 0.25)
  - Manner: stop, fricative, affricate, nasal, lateral, approximant (weight: 0.30)

Vowel features:
  - Height: high, mid, low (weight: 0.15)
  - Backness: front, central, back (weight: 0.15)

Feature weights based on perceptual salience: manner > place > voicing
(Steriade, 2001, "The phonology of perceptibility effects";
 Flemming, 2004, "Contrast and perceptual distinctiveness")

Example: [G] vs [K]
  - Same place (velar): 0
  - Same manner (stop): 0
  - Different voicing: 0.15
  - Distance = 0.15 (very similar sounds — low intelligibility impact)
```

#### 3.3.4 Intelligibility-Focused Scoring (Functional Load Weighting)

Instead of penalizing all phoneme deviations equally (standard GOP approach), errors are weighted by their impact on **intelligibility** — whether the error changes meaning or just sounds accented. This aligns with the Intelligibility Principle (Levis, 2005, *TESOL Quarterly*) which argues that pronunciation instruction should target intelligibility rather than native-likeness.

**No existing automated CAPT system implements functional load weighting in its scoring algorithm** (verified across 2022–2025 literature). This is the primary novel contribution of LinguAR's analysis pipeline.

**Theoretical chain:**

1. Munro & Derwing (1995, *Language Learning*) established that accent, comprehensibility, and intelligibility are partially independent — heavy accent does not necessarily reduce intelligibility
2. Levis (2005, *TESOL Quarterly*) formalized the Nativeness Principle vs. the Intelligibility Principle
3. Catford (1987) first applied functional load rankings to L2 pronunciation teaching priorities
4. Munro & Derwing (2006, *System*) empirically validated that high-FL errors significantly impact comprehensibility while low-FL errors have minimal impact
5. Brown (1988, 1991) computed FL values for English consonant and vowel contrasts
6. Kang & Moran (2014, *Frontiers in Communication*) empirically validated FL in L2 pronunciation instruction

**Functional Load Values:**

FL weights are derived from Brown (1988, 1991) and Catford (1987), normalized to 0-1 scale. The values below represent the relative information load carried by each phonemic contrast — higher FL means the contrast distinguishes more minimal pairs in English.

| Phoneme Pair | FL Source | FL Weight | Example | Intelligibility Impact |
|---|---|---|---|---|
| /ɪ/ vs /iː/ | Brown (1988): FL rank 1 | 0.90 | ship ↔ sheep | Meaning changes — HIGH |
| /l/ vs /r/ | Brown (1991): high FL in English | 0.85 | light ↔ right | Meaning changes — HIGH |
| /æ/ vs /ɛ/ | Brown (1988): FL rank 3 | 0.80 | bat ↔ bet | Meaning changes — HIGH |
| /p/ vs /b/ | Brown (1988): FL rank 5-6 | 0.60 | pat ↔ bat | Often distinguishable by context — MEDIUM |
| /s/ vs /z/ | Brown (1988): mid FL | 0.55 | sip ↔ zip | Moderate impact — MEDIUM |
| /θ/ vs /t/ | Brown (1988): low FL | 0.30 | think ↔ tink | Rarely causes misunderstanding — LOW |
| /θ/ vs /ð/ | Brown (1988): very low FL | 0.20 | — | Almost never causes misunderstanding — LOW |
| /v/ vs /w/ | Brown (1991): low FL | 0.25 | vine ↔ wine | Usually clear from context — LOW |

**Pronunciation Score Formula:**

The scoring formula follows the SpeechOcean762 multi-aspect framework (Zhang et al., 2021) which is the standard in pronunciation assessment research, while incorporating our novel FL weighting:

```
Pronunciation Score = 100 × (1 - FL_Weighted_Error_Sum / Total_Phonemes)

Where:
  FL_Weighted_Error_Sum = Σ (functional_load_weight × error_type_modifier × (1 - phonetic_distance_discount))

  Error type modifiers (based on error severity in L2 assessment literature):
    - Substitution: ×1.0  (Munro & Derwing, 2006: substitutions most impact intelligibility)
    - Deletion: ×0.8      (Deletions moderately impact — context often recovers meaning)
    - Insertion: ×0.5     (Insertions rarely cause misunderstanding — Zampini, 2008)

  Phonetic distance discount: errors to articulatorily similar phonemes are penalized less
    - e.g., /d/→/t/ (voicing only) gets 0.15 discount vs /d/→/z/ (manner change) gets 0

Score ranges (aligned with CEFR phonological control descriptors, Council of Europe, 2018):
  90-100: Excellent — highly intelligible, prosodic features used effectively (C1-C2)
  75-89:  Good — intelligible with minor accent markers (B2)
  60-74:  Fair — mostly intelligible, some listener effort needed (B1)
  40-59:  Developing — intelligible with significant effort (A2)
  0-39:   Needs work — frequently unintelligible (A1)
```

**Data source:** Functional load values for English phoneme pairs are compiled from Brown (1988, 1991) and Catford (1987), stored in `data/functional_load.json`. The JSON includes source citations per value for reproducibility.

#### 3.3.5 Reading Accuracy (Word-Level Sequence Alignment)

Reading accuracy is assessed by word-level edit distance alignment between CrisperWhisper's verbatim transcript and the displayed reference sentence. This approach is standard across all competitive CAPT systems (Microsoft Azure PA, SpeechAce, Duolingo) and matches the SpeechOcean762 "completeness" metric (Zhang et al., 2021) which is defined as the percentage of correctly pronounced words.

**Method:** `jiwer` library computes word-level alignment using the standard Levenshtein distance algorithm, classifying each word as:

```
Reference: "Could you pass me the bottle please"
Transcript: "Could you um pass me the the battle please"
                      ^^                 ^^  ^^^^^^
Alignment output:
  Could    → Could    [CORRECT]
  you      → you      [CORRECT]
           → um       [INSERTION — filler, flagged by CrisperWhisper]
  pass     → pass     [CORRECT]
  me       → me       [CORRECT]
  the      → the      [CORRECT]
           → the      [INSERTION — repetition, flagged by CrisperWhisper]
  bottle   → battle   [SUBSTITUTION]
  please   → please   [CORRECT]

Reading Accuracy = Correct / Reference_Words = 6/7 = 85.7%
```

**Classification enrichment from CrisperWhisper:** Insertions are sub-classified into:
- **Filler** ("um", "uh") — flagged by CrisperWhisper's disfluency detection
- **Repetition** (consecutive duplicate words) — detected from CrisperWhisper output
- **Content insertion** (extra content words) — standard insertion error

**Classification tiers (replacing the old semantic similarity approach):**

| Accuracy Range | Classification | Meaning |
|---|---|---|
| > 90% | CORRECT | Sentence read accurately |
| 70% – 90% | PARTIAL | Minor errors (word substitutions, small omissions) |
| < 70% | NEEDS_RETRY | Significant deviation — suggest re-reading |

**Why word-level alignment replaces semantic similarity:** Sentence Transformers cosine similarity is fundamentally unsuitable for reading accuracy assessment. BERTScore research shows contextual embeddings give F1 of 0.97 even for antonyms — a student saying "rug" instead of "mat" receives a high similarity score despite being a substitution error. Word-level alignment detects the exact error, which is what pronunciation feedback requires.

#### 3.3.6 Prosody Analysis (MFA + parselmouth)

Prosody scoring is absent from most open-source CAPT systems but is expected in modern pronunciation assessment research. SpeechOcean762 includes prosody as one of four sentence-level dimensions (accuracy, fluency, completeness, prosody). The CEFR (Council of Europe, 2018) describes phonological control across A1–C2 in terms of intelligibility, individual sounds, AND prosodic features.

**Step 1: Forced Alignment via Montreal Forced Aligner**

MFA provides phoneme-level time boundaries (median deviation 12.5ms from ground truth on TIMIT — Rousso et al., 2024), which are required for all prosodic measurements:

```
Input: CrisperWhisper transcript + audio WAV
MFA Process:
  1. Dictionary lookup: transcript words → ARPAbet phoneme sequences (using CMUdict + g2p-en)
  2. Acoustic model: GMM-HMM with SAT (Speaker Adaptive Training)
  3. Viterbi decoding: optimal phoneme-frame alignment
Output: TextGrid with phone and word boundaries at 10ms resolution

Example for "Could you pass me the bottle please":
  Word: "bottle"  [1.50 - 1.85s]
  Phone: B [1.50-1.57], AA [1.57-1.66], T [1.66-1.71], AH [1.71-1.78], L [1.78-1.85]
```

**Step 2: F0 (Pitch) Extraction via parselmouth/CREPE**

```
Primary: parselmouth (Python Praat wrapper) — Boersma & Weenink (2001)
  - F0 extraction: autocorrelation method, 75-500 Hz range
  - Intensity contour: for stress detection
  - Formants: F1/F2 for vowel quality (optional enrichment)

Fallback: CREPE (Kim et al., 2018) — neural pitch tracker
  - Sub-cent accuracy on clean speech
  - More robust to noise than autocorrelation
  - Heavier compute (~20MB model)
```

**Step 3: Prosodic Feature Computation**

| Feature | Tool | Calculation | Literature |
|---|---|---|---|
| **Lexical Stress** | MFA alignment + parselmouth F0 + duration + intensity | For each polysyllabic word: compare F0 peak, vowel duration, and intensity at stressed vs. unstressed syllables against reference. Stress error = mismatch with CMUdict stress markers (0/1/2) | Hahn (2004); Zielinski (2008): lexical stress strongly associated with intelligibility |
| **Intonation Pattern** | parselmouth F0 at phrase boundaries (from MFA word alignment) | Extract F0 slope over final 200ms of each phrase. Classify as rising/falling/flat. Compare against expected pattern for sentence type (statement=falling, question=rising) | Brazil (1997); Gilbert (2008): intonation conveys discourse-level information critical for comprehensibility |
| **Rhythm (nPVI-V)** | MFA phone alignment + vowel duration extraction | Normalized Pairwise Variability Index for vocalic intervals: nPVI-V = 100 × (Σ|d_k - d_{k+1}| / ((d_k + d_{k+1})/2)) / (m-1). Higher nPVI-V = more stress-timed (English-like) | Grabe & Low (2002): nPVI-V distinguishes stress-timed (English ~57) from syllable-timed languages; Ordin & Polyanskaya (2015): validated for L2 rhythm assessment |
| **Pitch Range** | parselmouth F0 | Standard deviation of F0 in semitones across utterance. Narrow range suggests monotone delivery | Kang (2010): pitch range accounts for significant variance in comprehensibility ratings |

**Prosody Composite Score:**

Weights are derived from the relative contribution of each prosodic feature to human intelligibility/comprehensibility ratings, as established in the literature:

```
Prosody Score = (0.35 × Stress_Accuracy) + (0.30 × Intonation_Accuracy) +
                (0.20 × Rhythm_nPVI_Normalized) + (0.15 × Pitch_Range_Normalized)

Weight justification:
  - Stress 0.35: Hahn (2004), Zielinski (2008) — lexical stress is the single strongest
    prosodic predictor of intelligibility; Field (2005) showed misplaced stress causes
    more comprehension failure than segmental errors
  - Intonation 0.30: Munro & Derwing (2001), Kang et al. (2010) — intonation is the
    second most impactful prosodic feature for comprehensibility ratings
  - Rhythm 0.20: Ordin & Polyanskaya (2015) — rhythm contributes to perceived
    fluency but is less directly tied to intelligibility than stress/intonation
  - Pitch Range 0.15: Kang (2010) — contributes to naturalness and engagement
    but has smallest independent effect on comprehensibility

Score ranges:
  90-100: Native-like prosody
  70-89:  Good prosody with minor deviations
  50-69:  Developing — noticeable prosodic issues
  30-49:  Flat or inappropriate prosody
  0-29:   Severe prosodic difficulties
```

#### 3.3.7 Fluency Analysis (CrisperWhisper disfluency + MFA timing)

Evaluates the learner's speech flow, pace, and rhythm. Fluency is decomposed into three sub-constructs following Skehan (2009) and Tavakoli & Skehan (2005): speed fluency, breakdown fluency, and repair fluency.

**Component roles (explicit division of labor):**

| Component | Role | What it provides |
|---|---|---|
| **CrisperWhisper** | Primary fluency source: filled pause detection ("um"/"uh"), repetitions, false starts, word-level timing for MLR/articulation rate, pause detection from word timestamp gaps | Word-level timestamps (~20ms accuracy), disfluency labels, inter-word silence durations |
| **MFA** | Sub-word temporal precision: phone-level boundaries for phonation-time ratio, vowel/consonant durations for nPVI-V rhythm | Phone boundaries at 10ms resolution — better than frame-level VAD for sub-word analysis |

**Why Silero VAD is NOT used server-side:** CrisperWhisper word timestamps provide pause boundaries (gaps between consecutive words), and MFA provides phone-level timing at 10ms resolution. Together they cover everything Silero VAD offered for fluency analysis, while CrisperWhisper additionally distinguishes filled pauses from silence — something Silero VAD cannot do. Silero VAD remains browser-side only for recording auto-trim (see Section 2.2). This aligns with Vaidya et al. (arXiv 2024), who showed that end-to-end SSL representations (wav2vec2.0) are more informative than hand-crafted features for oral reading fluency prediction.

**Pause Detection (from CrisperWhisper word timestamps):**

```
Process:
  1. CrisperWhisper returns: [{word: "the", start: 0.12, end: 0.28},
                              {word: "cat", start: 0.85, end: 1.10}, ...]
  2. Inter-word gaps computed: gap = next_word.start - prev_word.end
  3. Gaps > 250ms classified as pauses (de Jong & Bosker, 2013)
  4. Phonation-time ratio: sum(word_durations) / total_audio_duration
     (MFA phone boundaries used for precise vowel/consonant split)
```

**Pause Classification (informed by Tavakoli et al., 2020):**

```
By duration:
  - Brief hesitation: 250ms - 500ms (within normal processing)
  - Extended hesitation: 500ms - 1000ms (word-finding delay)
  - Long pause: > 1000ms (significant difficulty)
  (Thresholds following de Jong & Bosker, 2013: 250ms is minimum
   perceptible pause in fluency research)

By context (using CrisperWhisper word timing):
  - Phrase-boundary pause: Before punctuation or natural break — EXPECTED
  - Mid-phrase pause: Within a syntactic unit — DIFFICULTY MARKER
  (de Jong & Perfetti, 2011: mid-clause pauses most strongly predict
   perceived disfluency)
```

**Disfluency Detection (CrisperWhisper):**

CrisperWhisper's verbatim transcription provides all disfluency features directly:
- Filled pauses ("um", "uh") with timestamps — enables repair fluency metrics
- Repetitions (consecutive duplicate words) — counted separately from pauses
- False starts / self-corrections — indicates monitoring behavior

**Fluency Metrics (three sub-constructs):**

| Sub-construct | Metric | Calculation | Literature Basis |
|---|---|---|---|
| **Speed Fluency** | Words Per Minute (WPM) | word_count / total_duration × 60 | Standard oral fluency measure (CEFR, IELTS) |
| | Articulation Rate | syllables / speaking_time (excluding pauses) | Tavakoli et al. (2020): distinguishes proficiency levels A2-C1 |
| | Mean Length of Run (MLR) | mean words between pauses >250ms | Kang & Johnson (2018): associated with intelligible speech |
| **Breakdown Fluency** | Hesitation Ratio | pause_time / total_time | de Jong (2016): most reliable temporal fluency predictor |
| | Mid-Phrase Pause Rate | mid_phrase_pauses / total_words | de Jong & Perfetti (2011): strongest marker of processing difficulty |
| | Longest Fluent Phrase | max consecutive words without extended pause | Tavakoli & Skehan (2005): indicates sustained processing capacity |
| **Repair Fluency** | Filled Pause Rate | fillers_per_minute (from CrisperWhisper) | Skehan (2009): repair behaviors indicate self-monitoring |
| | Repetition Rate | repetitions_per_minute (from CrisperWhisper) | Freed et al. (2004): decreases with proficiency |
| | Phrase Boundary Accuracy | pauses_at_boundaries / total_pauses | de Jong & Bosker (2013): skilled speakers pause at natural boundaries |

**Fluency Composite Score:**

```
Fluency Score = (0.30 × Speed_Normalized) + (0.35 × Breakdown_Normalized) +
                (0.20 × Repair_Normalized) + (0.15 × Rhythm_nPVI_Normalized)

Weight justification:
  - Breakdown 0.35: de Jong (2016), Tavakoli et al. (2020) — pause patterns are
    the most reliable predictor of perceived fluency across proficiency levels
  - Speed 0.30: Tavakoli et al. (2020) — articulation rate and MLR consistently
    distinguish CEFR levels; but speed alone is insufficient (fast+choppy ≠ fluent)
  - Repair 0.20: Skehan (2009) — repair behaviors (fillers, repetitions) indicate
    self-monitoring ability; decreases with proficiency
  - Rhythm 0.15: shared with prosody score; contributes to perceived naturalness

Score ranges:
  90-100: Native-like fluency
  70-89:  Fluent with minor hesitations
  50-69:  Developing fluency — noticeable pauses
  30-49:  Choppy — frequent mid-phrase pauses
  0-29:   Word-by-word reading
```

#### 3.3.8 Hierarchical Scoring (Phone → Word → Utterance)

Since GOPT (Gong et al., ICASSP 2022), multi-granularity scoring across phoneme, word, and utterance levels is the expected standard in pronunciation assessment publications. SpeechOcean762 provides annotations at all three levels, and reviewers at Interspeech, ICASSP, and SLaTE expect results reported at each granularity.

**Scoring Hierarchy:**

```
PHONE LEVEL:
  Per-phoneme: GOP score, MDD label (correct/substitution/deletion/insertion),
               FL weight, phonetic distance to canonical

WORD LEVEL (aggregated from phones):
  Per-word accuracy = mean phone GOP within word boundaries (from MFA)
  Per-word stress = binary correct/incorrect (from prosody module)
  Per-word total = 0.7 × accuracy + 0.3 × stress
  (Following SpeechOcean762 word-level annotation schema: accuracy + stress → total)

UTTERANCE LEVEL (four dimensions, following SpeechOcean762 + CEFR):
  Accuracy:     FL-weighted pronunciation score (Section 3.3.4)
  Completeness: Reading accuracy percentage (Section 3.3.5)
  Fluency:      Fluency composite score (Section 3.3.7)
  Prosody:      Prosody composite score (Section 3.3.6)

  Total = (0.35 × Accuracy) + (0.15 × Completeness) +
          (0.25 × Fluency) + (0.25 × Prosody)

  Utterance-level weight justification:
    - Accuracy 0.35: Segmental accuracy is the primary focus of pronunciation
      assessment in CAPT (El Kheir et al., EMNLP Findings 2023); SpeechOcean762
      annotation guidelines give accuracy the highest weight in total score
    - Fluency 0.25: CEFR speaking assessment gives equal weight to fluency
      and phonological control (Council of Europe, 2018)
    - Prosody 0.25: CEFR 2018 expanded phonological descriptors explicitly
      include prosodic features at every level; Kang et al. (2010) showed prosody
      accounts for substantial variance in comprehensibility ratings
    - Completeness 0.15: Important for read-aloud tasks but less diagnostic
      than other dimensions; aligns with SpeechOcean762 where completeness
      has lower variance than other aspects
```

**Dashboard Reporting:**

All four dimensions are displayed independently on the learner dashboard, in addition to the composite total. This enables learners and teachers to identify whether difficulties are primarily segmental (accuracy), suprasegmental (prosody), temporal (fluency), or task-related (completeness).

---

### 3.4 TTS REFERENCE AUDIO & PRONUNCIATION REPLAY

After a learner records a sentence, they can compare their audio against a model pronunciation generated by a local TTS engine.

#### 3.4.1 TTS Engine

| Option | Model Size | Quality | Latency | Offline? |
|---|---|---|---|---|
| Piper TTS (primary) | ~30-60 MB | Good, natural | <1s per sentence | Yes |
| Coqui TTS / XTTS v2 (optional) | ~1.5 GB | Excellent, very natural | 2-5s per sentence | Yes |
| espeak-ng (fallback) | ~2 MB | Robotic but functional | <0.1s | Yes |

Piper TTS is the default — lightweight, fast, good quality, and fully offline. Generated reference audio is cached by sentence hash to avoid re-generation.

#### 3.4.2 Comparison Interface

```
┌─────────────────────────────────────────────────────────┐
│  "Could you pass me the bottle, please?"                 │
│                                                          │
│  Your Recording:      [▶ Play] ──── [waveform visual]   │
│  Model Pronunciation: [▶ Play] ──── [waveform visual]   │
│                                                          │
│  Pronunciation Score: 78/100                             │
│  Fluency: 72/100  │  Prosody: 65/100  │  Complete: 86%   │
│                                                          │
│  Problem areas highlighted:                              │
│  "Could you pass me the [bɒtl̩], please?"                │
│                           ^^^^                           │
│           /ɒ/ detected — expected /ɑː/                   │
│           GOP: -2.1 (below threshold)                    │
│                                                          │
│  [Try Again]   [Next Sentence]   [Hear Difference]       │
└─────────────────────────────────────────────────────────┘
```

- Side-by-side waveform visualization using Web Audio API
- Per-word pronunciation highlighting (words with low GOP scores are marked)
- "Hear Difference" button plays the specific problem word from both recordings
- Audio storage: `storage/tts_cache/{sentence_hash}.wav`

---

### 3.5 L1 TRANSFER ERROR PREDICTION

When a learner specifies their native language (L1) during onboarding, the system pre-loads predicted difficulty patterns based on contrastive analysis research.

#### 3.5.1 Supported L1 Profiles (Initial Set)

| L1 | Predicted Difficult Phonemes | Common Substitution Patterns |
|---|---|---|
| Mandarin Chinese | /r/, /l/, /θ/, /ð/, /v/, /ɪ/ | /r/→/l/, /θ/→/s/, /v/→/w/ |
| Hindi/Urdu | /θ/, /ð/, /æ/, /ɔː/ | /θ/→/t̪/, /ð/→/d̪/, /æ/→/ɛ/ |
| Tamil | /θ/, /ð/, /f/, /z/, /æ/ | /θ/→/t/, /f/→/p/, /z/→/s/ |
| Arabic | /p/, /v/, /ŋ/, /ɪ/, /e/ | /p/→/b/, /v/→/f/, /ŋ/→/n/ |
| Japanese | /r/, /l/, /θ/, /v/, /ʊ/ | /r/↔/l/, /θ/→/s/, /v/→/b/ |
| Korean | /r/, /l/, /f/, /v/, /z/ | /r/↔/l/, /f/→/p/, /z/→/ʤ/ |
| Spanish | /ʤ/, /ʃ/, /z/, /v/, /ɪ/ | /ʤ/→/j/, /z/→/s/, /v/→/b/ |
| French | /θ/, /ð/, /h/, /ɪ/, /æ/ | /θ/→/s/, /h/→∅, /æ/→/ɛ/ |

#### 3.5.2 Prediction-Validation Loop

```
Learner sets L1 = "Tamil" during onboarding
        │
        ├──→ System loads Tamil L1 profile
        │    Predicted difficulties: /θ/, /ð/, /f/, /z/, /æ/
        │
        ├──→ From Session 1: Prompt generator includes words with these sounds
        │    "Can you *feel* the *fresh* breeze *through* the window?"
        │
        ├──→ Dashboard shows "Predicted vs Actual" comparison
        │    Predicted: /θ/ difficult    Actual after 5 sessions: /θ/ 42% accuracy ✓ confirmed
        │    Predicted: /f/ difficult    Actual after 5 sessions: /f/ 88% accuracy ✗ not an issue
        │
        └──→ Spaced repetition prioritizes CONFIRMED difficult sounds
             (drops predictions that aren't validated by actual performance)
```

Data source: `data/l1_transfer_profiles.json`, compiled from contrastive analysis literature. Profiles are extensible — adding a new L1 requires only a JSON entry.

---

### 3.6 ADAPTIVE ENGINE — Spaced Repetition & Difficulty

The adaptive engine creates a closed feedback loop: performance data drives what content is generated next.

#### 3.6.1 Spaced Repetition for Problem Sounds

Each phoneme the learner has been assessed on gets a spaced repetition score using a modified SM-2 (SuperMemo 2) algorithm:

```
Phoneme Mastery Tracking:
─────────────────────────
/θ/  ████░░░░░░  42%  — Due for practice NOW (overdue 2 days)
/r/  ██████░░░░  63%  — Due for practice tomorrow
/æ/  ████████░░  81%  — Due in 4 days
/ɪ/  █████████░  92%  — Due in 12 days
/l/  ██████████  97%  — Mastered — due in 30 days
```

**SM-2 Algorithm:**

```
After each assessment of phoneme P:
  quality = pronunciation_score for P (0-5 scale, mapped from GOP)

  if quality >= 3 (passing):
    if repetition == 0: interval = 1 day
    if repetition == 1: interval = 3 days
    if repetition >= 2: interval = previous_interval × easiness_factor
    repetition += 1
  else:
    repetition = 0
    interval = 1 day  (reset — needs immediate re-practice)

  easiness_factor = max(1.3, EF + 0.1 - (5-quality) × (0.08 + (5-quality) × 0.02))
```

**Integration with sentence selection:**

```
Before selecting a sentence for any detected object:
  1. Query spaced_repetition_queue for phonemes DUE for this learner
  2. Get top 3 due phonemes (e.g., /θ/, /r/, /v/)
  3. Use as filter in sentence_selector: prefer sentences tagged with these phonemes
  4. Selected sentence: "Through the vivid rain, three birds returned to the river."
                        ^^         ^^     ^      ^^              ^      ^^
                        /θ/        /v/    /r/    /θ/             /r/    /r/
```

#### 3.6.2 Adaptive Difficulty

The system automatically adjusts sentence difficulty based on sustained performance:

```
IF pronunciation_score > 85% AND fluency_score > 80% for 3 consecutive sessions:
    → LEVEL UP (e.g., A2 → B1)

IF pronunciation_score < 50% OR fluency_score < 40% for 2 consecutive sessions:
    → LEVEL DOWN (e.g., B1 → A2)

IF pronunciation_score 50-85% (stable):
    → STAY at current level, increase phoneme targeting intensity
```

Level changes are logged and visible on the dashboard as a progression chart.

---

### 3.7 LEARNER DASHBOARD

The dashboard provides a gamified view of learning progress.

#### 3.7.1 Metric Cards (Top Row)

| Card | Data Source | Display |
|---|---|---|
| Pronunciation Score | Avg FL-weighted accuracy score (last 7 days) | "78/100" with trend arrow |
| Fluency Score | Avg fluency composite (last 7 days) | "72/100" with trend arrow |
| Prosody Score | Avg prosody composite (last 7 days) | "65/100" with trend arrow |
| Reading Speed | Avg WPM (last 7 days) | "112 WPM" with trend arrow |
| Words Practiced | Count of unique words attempted | "342 words" |
| Current Level | CEFR level from adaptive engine | "B1 — Intermediate" |
| Streak | Consecutive days with ≥1 session | "12 days 🔥" |

#### 3.7.2 Charts (Chart.js)

1. **Four-Dimension Radar Chart** — Accuracy, Fluency, Prosody, Completeness (most recent session vs average)
2. **Pronunciation Score Trend** — Line chart, 0-100 accuracy score over time
3. **Sounds to Practice** — Bar chart, bottom 10 phonemes by accuracy (with FL weight shown)
4. **Fluency & Prosody Trend** — Dual-line chart, fluency + prosody over time
5. **Reading Speed Trend** — Line chart, WPM over time
6. **Vocabulary Mastery Heatmap** — Grid of objects/words scanned, colored by mastery level (green = mastered, yellow = learning, red = struggling)
7. **Difficulty Progression** — Line chart showing CEFR level changes over time
8. **L1 Predictions vs Actuals** — Grouped bar chart comparing predicted and actual difficulty per phoneme

#### 3.7.3 Sessions Table

| Date | Object(s) | Mode | Pron. Score | Fluency | Sentences | Actions |
|---|---|---|---|---|---|---|
| Feb 24 | bottle, laptop | Scene | 82 | 74 | 5 | [Review] |
| Feb 23 | cup | Single | 71 | 68 | 8 | [Review] |

Each row expands to show individual sentence results. "Review" links to the detailed review page with TTS comparison.

#### 3.7.4 Gamification Elements

| Element | Implementation | Theoretical Basis (SDT) |
|---|---|---|
| XP per sentence | Base 10 XP + bonus for score >85 | Competence |
| Daily streak | Consecutive days with ≥1 session | Autonomy (habit formation) |
| Object Collection | Badge for scanning N unique objects | Competence + Autonomy |
| Sound Mastery | "Mastered /θ/!" badge when accuracy >90% 3× | Competence |
| Level progression | A1 → A2 → B1 → B2 → C1 → C2 | Competence (growth visibility) |
| Class leaderboard | Optional, teacher-enabled | Relatedness |
| Vocabulary count | Total unique words practiced | Competence |

---

### 3.8 TEACHER DASHBOARD & CLASSROOM INTEGRATION

A separate dashboard for teachers to monitor class-wide progress and assign targeted practice.

```
┌──────────────────────────────────────────────────────────┐
│  Class: English B1 — Mrs. Sharma                          │
│  Students: 28 │ Active this week: 24                      │
│                                                           │
│  Class-wide Problem Sounds:                               │
│  /θ/  ████████░░  78% of students struggling              │
│  /r/  ██████░░░░  62% of students struggling              │
│  /v/  █████░░░░░  54% of students struggling              │
│  → Suggestion: Plan a lesson on dental fricatives (/θ/)   │
│                                                           │
│  ┌──────────┬──────┬───────┬────────┬────────┐           │
│  │ Student  │ Level│ Score │ Streak │ Status │           │
│  ├──────────┼──────┼───────┼────────┼────────┤           │
│  │ Priya S. │ B1   │ 82    │ 14d    │ ● On   │           │
│  │ Ravi K.  │ A2   │ 61    │ 3d     │ ● On   │           │
│  │ Arun M.  │ B1   │ 75    │ 0d     │ ○ Off  │           │
│  └──────────┴──────┴───────┴────────┴────────┘           │
│                                                           │
│  [Assign Vocabulary Set]  [Export Class Report]            │
└──────────────────────────────────────────────────────────┘
```

**Teacher features:**
- View all students' progress in one place
- See class-wide problem areas (aggregated phoneme error data across all students)
- Assign specific objects or topics for students to scan
- Set difficulty level overrides per student
- Export progress reports (CSV/PDF)

---

### 3.9 OFFLINE-FIRST / LOW-RESOURCE MODE

The system is designed with progressive degradation — the core scan → read → score loop works even without internet, with full analysis syncing when connectivity returns.

**Client-side capabilities (no server needed):**
- YOLO11s ONNX (~38 MB) — object detection in browser
- Silero VAD ONNX (~1 MB) — recording auto-trim in browser (speech onset/offset detection)
- Web Audio API — audio capture
- Web Speech API — browser-built-in ASR as fallback
- Pre-cached sentence sets per object (downloaded once)

**Online vs Offline comparison:**

| Capability | Online Mode (Full) | Offline Mode (Degraded) |
|---|---|---|
| Object Detection | YOLO11s (browser) | YOLO11s (browser) — identical |
| Sentence Generation | Pre-generated sentence bank (JSON lookup) | Same — sentence bank is a local JSON file, works offline |
| ASR | CrisperWhisper (server) | Web Speech API (browser) |
| Pronunciation Scoring | HuBERT MDD + FL scoring (server) | Rule-based scoring (browser) |
| Prosody Analysis | MFA + parselmouth (server) | Not available offline |
| Fluency Analysis | CrisperWhisper + MFA (server) | Silero VAD (browser ONNX, basic WPM only) |
| Analytics | Full dashboard (4 dimensions) | Basic accuracy + WPM only |
| Data Sync | Real-time | Queued, syncs when online |

**Offline implementation:**
- Service Worker caches sentence sets, frontend assets, and ONNX models
- IndexedDB stores offline session results locally
- Sync endpoint (`POST /sync`) uploads cached results when connectivity returns
- **Equity argument:** Works in rural schools, developing regions, areas with poor connectivity — no student data leaves the device

---

## 4. Frontend Pages

| Page | URL | Purpose |
|---|---|---|
| index.html | `/` | Home — onboarding flow, daily goals, streak display, navigation to all features |
| scan.html | `/scan` | **Hero feature** — AR camera with object detection, contextual sentence practice |
| practice.html | `/practice` | Manual practice mode — select word/topic, conversation scaffolding, minimal pairs |
| dashboard.html | `/dashboard` | Learner progress — charts, streaks, XP, vocabulary mastery, level progression |
| review.html | `/review?recording_id=X` | Session review — detailed per-sentence analysis, TTS comparison, replay |
| teacher.html | `/teacher` | Teacher dashboard — class overview, assignments, aggregated analytics |

### 4.1 Onboarding Flow (index.html)

```
Step 1: "What's your native language?"
        → [Tamil] [Hindi] [Mandarin] [Arabic] [Japanese] [Spanish] [Other...]
        → Loads L1 transfer profile

Step 2: "What's your English level?"
        → [Beginner] [Elementary] [Intermediate] [Advanced] [Not sure — test me]
        → If "test me": Quick 5-sentence pronunciation test to estimate CEFR level

Step 3: "Set your daily goal"
        → [5 minutes] [10 minutes] [15 minutes] [20 minutes]

Step 4: "You're all set! Start scanning objects around you."
        → Redirect to Scan & Learn
```

---

## 5. Database Schema

All tables use SQLAlchemy ORM for database-agnostic access. In local mode (`DEPLOYMENT_MODE=local`), the database is SQLite at `storage/linguar.db`. In hosted mode (`DEPLOYMENT_MODE=hosted`), the database is PostgreSQL configured via `DATABASE_URL` environment variable. Schema is identical in both modes; SQLAlchemy handles dialect differences.

Audio files are stored locally in `storage/audio/` (local mode) or in S3/MinIO object storage (hosted mode), with only the file path/key stored in the database.

### 5.0 users (Hosted Mode Only)

```sql
users:
  id                          INTEGER PRIMARY KEY
  email                       TEXT UNIQUE NOT NULL
  hashed_password             TEXT NOT NULL
  display_name                TEXT
  created_at                  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  last_login                  TIMESTAMP
  is_active                   BOOLEAN DEFAULT TRUE
  role                        TEXT DEFAULT 'learner'  -- learner / teacher / admin
  rate_limit_tier             TEXT DEFAULT 'free'     -- free / premium / teacher
```

In local mode, this table is not used; a default learner profile is created automatically. In hosted mode, `learner_profiles.learner_id` references `users.id`.

### 5.1 recordings

```sql
recordings:
  -- Identity
  id                          INTEGER PRIMARY KEY
  session_id                  TEXT
  learner_id                  TEXT

  -- Content
  object_name                 TEXT        -- detected object
  scene_objects_json          TEXT        -- all detected objects if multi-object mode
  sentence_text               TEXT        -- displayed sentence
  difficulty_level            TEXT        -- A1/A2/B1/B2/C1/C2
  sentence_type               TEXT        -- single/scene/dialogue/minimal_pair
  grammar_focus               TEXT        -- grammar pattern in the sentence

  -- Audio
  audio_path                  TEXT
  transcript                  TEXT

  -- Reading Accuracy (word-level alignment)
  reading_accuracy            REAL        -- % correct words (from jiwer alignment)
  reading_classification      TEXT        -- CORRECT / PARTIAL / NEEDS_RETRY
  wer                         REAL        -- word error rate
  word_alignment_json         TEXT        -- per-word: {word, ref_word, label: C/S/D/I/R}
  missed_words_json           TEXT        -- specific words missed (substitutions + deletions)
  filler_count                INTEGER     -- filled pauses detected by CrisperWhisper
  repetition_count            INTEGER     -- word repetitions detected

  -- Pronunciation (HuBERT MDD + FL-weighted)
  pronunciation_score         REAL        -- 0-100 FL-weighted intelligibility score
  per_ml                      REAL        -- ML phoneme error rate (from HuBERT MDD)
  ml_gop                      REAL        -- overall GOP score (from HuBERT CTC logits)
  ml_confidence               REAL        -- model confidence
  ml_detected_phonemes_json   TEXT        -- detected ARPAbet sequence
  ml_detected_ipa_json        TEXT        -- detected IPA sequence
  ml_alignment_json           TEXT        -- (expected, detected) phoneme pairs with MDD labels
  ml_phoneme_scores_json      TEXT        -- per-phoneme: {phone, gop, fl_weight, mdd_label}
  problematic_phonemes_json   TEXT        -- phonemes below threshold
  speech_rate                 REAL        -- syllables per second (overall)

  -- Prosody (MFA + parselmouth)
  prosody_score               REAL        -- composite 0-100
  stress_accuracy             REAL        -- % correctly stressed words
  intonation_accuracy         REAL        -- % correct phrase-final patterns
  rhythm_npvi_v               REAL        -- normalized PVI for vocalic intervals
  pitch_range_st              REAL        -- F0 standard deviation in semitones
  mfa_textgrid_path           TEXT        -- path to MFA output TextGrid
  prosody_details_json        TEXT        -- per-word stress + intonation details

  -- Fluency (CrisperWhisper disfluency + MFA timing)
  words_per_minute            REAL
  articulation_rate           REAL        -- syllables/sec excluding pauses
  mean_length_of_run          REAL        -- mean words between pauses >250ms
  longest_fluent_phrase       INTEGER
  hesitation_ratio            REAL
  mid_phrase_pause_rate       REAL        -- mid-phrase pauses / total words
  filled_pause_rate           REAL        -- fillers per minute (from CrisperWhisper)
  repetition_rate             REAL        -- repetitions per minute
  total_pauses                INTEGER
  hesitation_count            INTEGER
  speaking_rate               REAL        -- syllables/sec including pauses
  fluency_score               REAL        -- composite 0-100
  pauses_json                 TEXT        -- detailed pause data with context labels

  -- Hierarchical Scores (phone→word→utterance)
  word_scores_json            TEXT        -- per-word: {word, accuracy, stress, total}
  utterance_accuracy          REAL        -- utterance-level accuracy (0-100)
  utterance_completeness      REAL        -- utterance-level completeness (0-100)
  utterance_fluency           REAL        -- utterance-level fluency (0-100)
  utterance_prosody           REAL        -- utterance-level prosody (0-100)
  utterance_total             REAL        -- weighted composite (0-100)

  -- Metadata
  analysis_mode               TEXT
  tts_audio_path              TEXT        -- path to reference TTS audio
  created_at                  DATETIME
```

### 5.2 learner_profiles

```sql
learner_profiles:
  learner_id          TEXT PRIMARY KEY
  display_name        TEXT
  native_language     TEXT           -- for L1 transfer prediction
  current_level       TEXT           -- CEFR level (A1-C2)
  xp_total            INTEGER DEFAULT 0
  streak_current      INTEGER DEFAULT 0
  streak_longest      INTEGER DEFAULT 0
  last_active_date    DATE
  daily_goal_minutes  INTEGER DEFAULT 10
  created_at          DATETIME
```

### 5.3 learner_vocabulary

```sql
learner_vocabulary:
  id                  INTEGER PRIMARY KEY
  learner_id          TEXT
  word                TEXT
  phonemes_arpabet    TEXT           -- expected pronunciation
  times_practiced     INTEGER DEFAULT 0
  avg_pronunciation   REAL           -- average GOP for this word
  mastery_level       TEXT           -- new/learning/practiced/mastered
  last_practiced      DATETIME
  context_sentence    TEXT           -- sentence where first encountered
  detected_object     TEXT           -- object it was associated with
  UNIQUE(learner_id, word)
```

### 5.4 spaced_repetition_queue

```sql
spaced_repetition_queue:
  id                  INTEGER PRIMARY KEY
  learner_id          TEXT
  phoneme             TEXT           -- ARPAbet symbol
  interval_days       REAL
  due_date            DATE
  easiness_factor     REAL DEFAULT 2.5
  repetitions         INTEGER DEFAULT 0
  last_score          REAL
  last_reviewed       DATETIME
  UNIQUE(learner_id, phoneme)
```

### 5.5 l1_transfer_predictions

```sql
l1_transfer_predictions:
  learner_id          TEXT
  phoneme             TEXT
  predicted_difficult BOOLEAN
  actual_accuracy     REAL           -- updated as data comes in
  confirmed           BOOLEAN        -- prediction validated by performance?
  PRIMARY KEY(learner_id, phoneme)
```

### 5.6 classes & class_members

```sql
classes:
  class_id            TEXT PRIMARY KEY
  teacher_name        TEXT
  class_name          TEXT
  created_at          DATETIME

class_members:
  class_id            TEXT
  learner_id          TEXT
  PRIMARY KEY(class_id, learner_id)

class_assignments:
  id                  INTEGER PRIMARY KEY
  class_id            TEXT
  target_objects_json  TEXT           -- objects to practice
  target_level        TEXT           -- difficulty level
  due_date            DATE
  created_at          DATETIME
```

### 5.7 daily_progress

```sql
daily_progress:
  id                  INTEGER PRIMARY KEY
  learner_id          TEXT
  date                DATE
  sessions_completed  INTEGER
  sentences_practiced INTEGER
  minutes_practiced   REAL
  avg_pronunciation   REAL
  avg_fluency         REAL
  xp_earned           INTEGER
  new_words_learned   INTEGER
  UNIQUE(learner_id, date)
```

### 5.8 Supporting Tables

```sql
generated_prompts:
  id                  INTEGER PRIMARY KEY
  object_name         TEXT
  difficulty_level    TEXT
  prompt_json         TEXT           -- selected sentence from bank (JSON)
  created_at          DATETIME

session_progress:
  id                  INTEGER PRIMARY KEY
  session_id          TEXT
  learner_id          TEXT
  avg_pronunciation   REAL
  avg_fluency         REAL
  sentences_completed INTEGER
  created_at          DATETIME
```

---

## 6. API Endpoints

### 6.0 Authentication (Hosted Mode)

| Endpoint | Method | Purpose | Parameters |
|---|---|---|---|
| `/auth/register` | POST | Create new user account | email, password, display_name |
| `/auth/login` | POST | Authenticate and receive JWT token | email, password |
| `/auth/refresh` | POST | Refresh expired JWT access token | refresh_token |
| `/auth/me` | GET | Get current authenticated user info | — (JWT in header) |

All endpoints below require `Authorization: Bearer <token>` header in hosted mode. In local mode (`DEPLOYMENT_MODE=local`), auth is bypassed and a default learner profile is used.

### 6.1 Session & Learner Management

| Endpoint | Method | Purpose | Parameters |
|---|---|---|---|
| `/learner/onboard` | POST | Create learner profile | display_name, native_language, current_level, daily_goal_minutes |
| `/session/start` | POST | Initialize new practice session | learner_id, difficulty_level, object_name (optional) |
| `/session/next-prompt` | POST | Get next sentence in session | session_id |
| `/session/{session_id}/summary` | GET | Session-level aggregated metrics | — |
| `/learner/{learner_id}/history` | GET | All recording history | — |
| `/learner/{learner_id}/progress` | GET | Aggregated progress metrics and trends | — |
| `/learner/{learner_id}/vocabulary` | GET | Vocabulary list with mastery levels | — |
| `/learner/{learner_id}/due-phonemes` | GET | Phonemes due for spaced repetition | — |
| `/learner/{learner_id}/l1-predictions` | GET | L1 transfer predictions vs actuals | — |

### 6.2 Content Generation

| Endpoint | Method | Purpose | Parameters |
|---|---|---|---|
| `/generate-prompts` | POST | Generate graded sentences for an object | object_name, difficulty_level, problem_phonemes (optional) |
| `/generate-scene` | POST | Generate multi-object relational sentences | objects_json (with positions), difficulty_level |
| `/generate-dialogue` | POST | Generate conversation scaffolding | object_name, difficulty_level, num_turns |
| `/generate-minimal-pairs` | POST | Generate sentences with minimal pairs | phoneme_contrast (e.g., "ɪ-iː"), difficulty_level |

### 6.3 Analysis

| Endpoint | Method | Purpose | Parameters |
|---|---|---|---|
| `/record` | POST | Submit audio for analysis — **returns job_id immediately** (async in hosted mode, sync in local mode). Audio is enqueued for ML processing. | session_id, object_name, sentence_text, difficulty_level, audio (file) |
| `/recording/{recording_id}` | GET | Full analysis details for one recording | — |
| `/recording/{job_id}/status` | GET | Poll analysis job status: `queued` / `processing` / `completed` / `failed`. Returns full results when completed. (Hosted mode only; local mode returns results directly from `/record`.) | — |
| `/tts/generate` | POST | Generate reference pronunciation audio | sentence_text |

### 6.4 Classroom

| Endpoint | Method | Purpose | Parameters |
|---|---|---|---|
| `/class/{class_id}/overview` | GET | Teacher class overview | — |
| `/class/{class_id}/problem-sounds` | GET | Aggregated class phoneme difficulties | — |
| `/class/{class_id}/assign` | POST | Create assignment for class | target_objects_json, target_level, due_date |

### 6.5 Offline Sync

| Endpoint | Method | Purpose | Parameters |
|---|---|---|---|
| `/sync` | POST | Upload cached offline session results | learner_id, recordings_json |

### 6.6 Status

| Endpoint | Method | Purpose |
|---|---|---|
| `/api/generate` | POST | Select sentence from bank for detected object at learner's level |
| `/generated-objects` | GET | List all objects with cached prompts |

---

## 7. File Structure

```
LinguAR/
├── backend/
│   ├── main.py                           # FastAPI application entry point
│   ├── config.py                         # Configuration (DB_URL, model paths, TTS config)
│   ├── requirements.txt                  # Python dependencies
│   │
│   ├── routers/
│   │   ├── analysis.py                   # Core API endpoints (session, record, learner)
│   │   ├── classroom.py                  # Teacher/class endpoints
│   │   └── sync.py                       # Offline sync endpoint
│   │
│   ├── services/
│   │   ├── speech_processing.py          # Main analysis pipeline orchestrator
│   │   ├── reading_accuracy.py           # Word-level edit distance alignment (jiwer)
│   │   ├── mdd_engine.py                 # HuBERT retrieval-based MDD (phoneme pool + kNN)
│   │   ├── phoneme_analysis.py           # Phoneme comparison, Needleman-Wunsch alignment
│   │   ├── intelligibility_scoring.py    # Functional load weighted pronunciation score
│   │   ├── prosody_analysis.py           # MFA + parselmouth: stress, intonation, nPVI, pitch
│   │   ├── hierarchical_scorer.py        # Phone→word→utterance aggregation (4 dimensions)
│   │   ├── phoneme_features.py           # Articulatory phonetic distance calculations
│   │   ├── phoneme_mapping.py            # IPA ↔ ARPAbet bidirectional conversion
│   │   ├── phoneme_lookup.py             # CMU Pronouncing Dictionary + g2p-en OOV fallback
│   │   ├── ml_hubert.py                  # HuBERT model loader, embedding extraction, GOP
│   │   ├── ml_models.py                  # ML model registry and lazy loader
│   │   ├── ml_vad.py                     # Silero VAD wrapper (browser-side recording utility only; NOT in server fluency pipeline)
│   │   ├── fluency_analysis.py           # Speed/breakdown/repair fluency (CrisperWhisper + VAD)
│   │   ├── sentence_selector.py          # Sentence bank lookup + phoneme-targeted selection (no LLM at runtime)
│   │   ├── tts_engine.py                 # Piper TTS wrapper for reference audio
│   │   ├── adaptive_engine.py            # Difficulty adjustment logic
│   │   ├── spaced_repetition.py          # SM-2 algorithm for phoneme scheduling
│   │   ├── l1_predictor.py               # L1 transfer error prediction
│   │   ├── minimal_pairs.py              # Minimal pair sentence generation
│   │   ├── scene_generator.py             # Multi-object template slot-filling with spatial relationships
│   │   ├── metrics.py                    # WER, speech rate, pause ratio calculations
│   │   ├── audio.py                      # Audio preprocessing utilities
│   │   ├── tasks.py                      # Celery task definitions (analysis job dispatch)
│   │   ├── auth.py                       # JWT authentication, user session management
│   │   └── storage.py                    # Storage abstraction (local filesystem / S3-MinIO)
│   │
│   ├── models/
│   │   ├── crisperwhisper_model.py       # CrisperWhisper ASR singleton loader (transformers pipeline)
│   │   ├── hubert_model.py               # HuBERT singleton loader + phoneme embedding pool
│   │   └── cache/                        # HuggingFace model cache directory
│   │
│   ├── database/
│   │   ├── db.py                         # SQLAlchemy engine and session management
│   │   ├── schema.py                     # Table initialization
│   │   ├── schema.sql                    # Full SQL schema
│   │   └── persistence.py                # Save/query functions for all tables
│   │
│   ├── data/
│   │   ├── objects.py                    # Object definitions with frequency and difficulty data
│   │   ├── cmudict-0.7b.txt             # CMU Pronouncing Dictionary (134,000+ words)
│   │   ├── functional_load.json          # Phoneme pair FL weights (Brown 1988/1991, Catford 1987)
│   │   ├── l1_transfer_profiles.json     # L1-specific difficulty predictions (8 languages)
│   │   ├── minimal_pairs.json            # Minimal pair database indexed by phoneme contrast
│   │   ├── cefr_vocabulary.json          # Word frequency lists organized by CEFR level
│   │   ├── phoneme_pool/                 # HuBERT phoneme embedding pool (built from L2-ARCTIC native samples)
│   │   │   ├── embeddings.npy            # ~200K frame embeddings (HuBERT layer 21)
│   │   │   ├── labels.npy               # Corresponding phoneme labels (ARPAbet)
│   │   │   └── build_pool.py            # Script to regenerate pool from L2-ARCTIC training data
│   │   └── mfa_models/                   # Montreal Forced Aligner pretrained models
│   │       ├── english_mfa.zip           # English acoustic model
│   │       └── english_mfa_dict.txt      # English pronunciation dictionary
│   │
│   ├── utils/
│   │   ├── file_utils.py                 # File and directory management
│   │   └── audio_converter.py            # PyAV audio format conversion (WebM→WAV, resampling)
│   │
│   ├── frontend/
│   │   ├── index.html                    # Home — onboarding, daily goals, navigation
│   │   ├── scan.html                     # AR Scan & Learn (hero feature)
│   │   ├── practice.html                 # Manual practice, conversation scaffolding, minimal pairs
│   │   ├── dashboard.html                # Learner progress dashboard (gamified)
│   │   ├── review.html                   # Session review with TTS pronunciation comparison
│   │   ├── teacher.html                  # Teacher dashboard — class management
│   │   └── assets/
│   │       ├── style.css                 # Shared styles, gamification UI
│   │       └── sounds/                   # UI sound effects (level up, streak, achievement)
│   │
│   ├── storage/
│   │   ├── audio/                        # Learner recordings
│   │   └── tts_cache/                    # Generated TTS reference audio (cached by hash)
│   │
│   └── tests/
│       ├── test_intelligibility.py       # FL-weighted scoring tests
│       ├── test_mdd_engine.py            # HuBERT retrieval MDD tests
│       ├── test_reading_accuracy.py      # Word-level alignment tests
│       ├── test_prosody.py               # MFA + parselmouth prosody tests
│       ├── test_hierarchical_scorer.py   # Phone→word→utterance aggregation tests
│       ├── test_spaced_repetition.py     # SM-2 algorithm tests
│       ├── test_l1_predictor.py          # L1 transfer prediction tests
│       ├── test_fluency_analysis.py      # Fluency metrics tests
│       └── test_persistence.py           # Database operations tests
│
├── launcher.py                           # One-click server startup + browser launch (local mode)
├── docker-compose.yml                    # Multi-service configuration (hosted mode)
├── docker-compose.local.yml              # Single-process override (local/dev mode)
├── Dockerfile.api                        # FastAPI gateway image
├── Dockerfile.worker                     # Celery ML worker image (includes all ML models)
├── .env.example                          # Environment variables template (DEPLOYMENT_MODE, DB_URL, REDIS_URL, etc.)
├── nginx.conf                            # Reverse proxy + SSL termination config
└── README.md                             # Setup and usage documentation
```

---

## 8. Key Dependencies

```
# Backend framework
fastapi, uvicorn, python-multipart

# Database
sqlalchemy, psycopg2-binary             # PostgreSQL driver (hosted mode)
# SQLite used in local mode (no extra driver needed)

# Task queue (hosted mode)
celery[redis], redis                     # Async ML job processing

# Authentication
python-jose[cryptography], passlib       # JWT tokens, password hashing

# Object storage (hosted mode)
boto3                                    # S3/MinIO client for audio file storage

# ASR
transformers (CrisperWhisper — must use nyrahealth/transformers fork for best timestamps)
# NOTE: Do NOT use faster-whisper for CrisperWhisper — CTranslate2 loses timestamp accuracy

# ML / Deep Learning
torch, torchaudio, transformers (HuBERT: facebook/hubert-large-ls960-ft)

# Forced Alignment & Prosody
montreal-forced-aligner (conda install -c conda-forge montreal-forced-aligner)
praat-parselmouth                    # Python Praat wrapper for F0, intensity, formants
crepe                                # Neural pitch tracker (fallback for noisy audio)

# Voice Activity Detection (browser-side only — NOT in server fluency pipeline)
# silero-vad ONNX loaded via ONNX Runtime Web in browser for recording auto-trim

# Phoneme tools
g2p-en                               # Seq2seq G2P trained on CMUdict (replaces espeak-ng fallback)
nltk (WordNet, CMUdict)

# TTS
piper-tts (or coqui-tts)

# Audio processing
av (PyAV), noisereduce, numpy, scipy

# Text comparison & alignment
jiwer                                # Word-level edit distance alignment (replaces sentence-transformers)

# Multi-user deployment
celery[redis]                        # Async task queue for ML inference jobs
redis                                # Task broker + result cache
psycopg2-binary                      # PostgreSQL adapter (concurrent multi-user writes)
pyjwt                                # JWT authentication for learner sessions

# Frontend (CDN / browser)
Chart.js, ONNX Runtime Web, YOLO11s ONNX model, Silero VAD ONNX model
```

**Removed dependencies:**
- `faster-whisper` → replaced by CrisperWhisper (transformers pipeline)
- `sentence-transformers` → replaced by jiwer word-level alignment
- `phonemizer` → replaced by g2p-en for G2P (avoids IPA/ARPAbet phoneset mixing)
- `silero-vad` (server-side) → removed from fluency pipeline; CrisperWhisper timestamps + MFA phone boundaries replace all VAD-based fluency features. Silero VAD ONNX retained browser-side only for recording auto-trim.

---

## 9. Implementation Roadmap

### Phase 1 — Core System (MVP)

| Task | Effort | Description |
|---|---|---|
| AR object detection interface | Medium | Camera feed, YOLO11s ONNX detection, bounding box overlay |
| Audio recording pipeline | Medium | MediaRecorder API, silence detection, WebM→WAV conversion |
| CrisperWhisper ASR integration | Medium | Verbatim transcription with word timestamps and disfluency detection |
| HuBERT MDD engine | High | Phoneme embedding pool construction (L2-ARCTIC), retrieval-based MDD, GOP scoring |
| MFA forced alignment integration | Medium | Phone/word boundary extraction, TextGrid output |
| Prosody analysis (parselmouth) | Medium-High | F0 extraction, stress detection, intonation classification, nPVI-V rhythm |
| Hierarchical scorer | Medium | Phone→word→utterance aggregation, 4-dimension output |
| Intelligibility-focused scoring | Medium | Functional load weighting (Brown 1988/1991 values), pronunciation score 0-100 |
| Word-level reading accuracy | Low | jiwer edit distance alignment, C/S/D/I/R per word |
| CrisperWhisper + MFA fluency analysis | Medium | Speed/breakdown/repair fluency metrics from CrisperWhisper timestamps + MFA phone boundaries |
| Sentence bank + selection logic | Low | JSON lookup from pre-generated bank, phoneme-targeted selection, fallback templates |
| Sentence bank authoring script | Low | Offline script to batch-generate sentences via any LLM (Ollama/ChatGPT/Claude) |
| Fallback template sentences | Low | Pre-built sentences per object per level |
| Database schema and persistence | Medium | All tables including new prosody/hierarchical fields |
| Basic learner dashboard | Medium | Metric cards (4 dimensions), score trends, sessions table |
| FastAPI endpoints | Medium | All core routes (/record, /session, /learner, /generate) |
| Launcher and navigation | Low | One-click startup, home page |

### Phase 2 — Key Enhancements (Publication Novelty)

| Task | Effort | Description |
|---|---|---|
| Multi-object scene description | Medium | Spatial relationship computation, relational sentence generation |
| L1 transfer error prediction | Medium | L1 profiles, prediction-validation loop |
| Spaced repetition engine | Medium-High | SM-2 algorithm, integration with prompt generation |
| FL weight data compilation with citations | Low-Medium | Functional load JSON from Brown (1988/1991), Catford (1987) with per-value source |
| Learner onboarding flow | Low | L1 selection, level assessment, goal setting |
| Benchmark validation (SpeechOcean762) | High | Run pipeline on SpeechOcean762 test set, report PCC for 4 dimensions at 3 granularities |
| Benchmark validation (L2-ARCTIC) | Medium | Run HuBERT MDD on L2-ARCTIC 6-speaker test set, report F1, FRR, precision |
| FL weighting ablation study | Medium | Compare FL-weighted vs unweighted scores in correlation with human intelligibility ratings |

### Phase 3 — Advanced Features

| Task | Effort | Description |
|---|---|---|
| TTS reference audio generation | Medium | Piper TTS integration, caching, comparison endpoint |
| Pronunciation replay & comparison UI | Medium | Side-by-side waveforms, per-word highlighting |
| Conversation scaffolding mode | Medium | Dialogue generation, turn-taking interface |
| Minimal pair targeting | Medium | Minimal pair database, error-driven sentence generation |
| Adaptive difficulty adjustment | Low-Medium | Level up/down logic, progression tracking |

### Phase 4 — Multi-User Deployment & Scale

| Task | Effort | Description |
|---|---|---|
| Docker Compose configuration | Medium | api, worker, redis, postgres, minio, nginx services with health checks |
| Celery task queue integration | Medium | Analysis job dispatch, result polling endpoint, dead letter queue |
| PostgreSQL migration | Low-Medium | SQLAlchemy dialect switch, Alembic migrations, connection pooling |
| JWT authentication system | Medium | Register, login, refresh token, role-based access (learner/teacher/admin) |
| S3/MinIO object storage | Medium | Audio upload, TTS cache, MFA TextGrid storage with lifecycle policies |
| Per-user rate limiting | Low | Redis-based sliding window rate limiter per tier |
| Teacher dashboard | High | Class overview, student list, assignments, aggregated analytics |
| Gamification layer | Medium | XP, streaks, badges, achievements, level progression UI |
| Offline-first mode | High | Service Worker, IndexedDB, Web Speech API fallback, sync |
| Class assignment system | Medium | Teacher creates assignments, students see assigned objects |
| CSV/PDF report export | Low-Medium | Teacher export of class and individual progress |
| Horizontal scaling validation | Medium | Load test with k6/Locust, verify async pipeline under 50+ concurrent users |

---

## 10. User Study Design Requirements (For Publication)

### 10.1 Minimum Viable Study (for CALL / ReCALL journals)

- **Design:** Pre-test → 6-week intervention → Post-test → Delayed post-test (2 weeks)
- **Participants:** 60-80 L2 English learners (30-40 per group)
- **Groups:** (a) LinguAR system, (b) Traditional pronunciation app (same content, no AR)
- **Measures:** Pronunciation accuracy (human rated + automated), reading fluency (WPM), vocabulary retention, motivation (Intrinsic Motivation Inventory), usability (SUS), cognitive load (Paas scale)
- **Analysis:** Mixed ANOVA (time × group), Cohen's d effect sizes

### 10.2 Ideal Study (for Computers & Education)

- **Design:** Pre-test → 8-12 week intervention → Post-test → Delayed post-test (3 weeks)
- **Participants:** 120-150 learners (40-50 per group)
- **Groups:** (a) Full LinguAR, (b) Non-AR app with same speech features, (c) Traditional classroom instruction
- **Additional measures:** Semi-structured interviews (n=15-20), think-aloud protocols (n=10-12), learning analytics log analysis
- **Theoretical framework:** Situated Learning Theory + Cognitive Theory of Multimedia Learning + Task-Based Language Teaching

### 10.3 Validation Study (Recommended Before Main Study)

- **Purpose:** Validate automated scoring against human expert ratings AND benchmark on standard datasets
- **Design A — Human validation:** 2-3 trained phoneticians rate 80-100 learner utterances on 1-9 scale for intelligibility and comprehensibility
- **Target:** Pearson/Spearman correlation ρ > 0.75 between human ratings and system's pronunciation score
- **Benchmark:** Duolingo's pronunciation scorer achieved ρ = 0.82 (Cai, 2025); Microsoft PA prosody PCC = 0.77 (Cai, 2025)
- **Report:** Inter-rater reliability (ICC or Cronbach's alpha) alongside human-machine correlations
- **Design B — Benchmark validation (deferred to post-implementation):**
  - **SpeechOcean762:** Report PCC for all 4 utterance-level dimensions (accuracy, fluency, prosody, completeness) + word-level accuracy + phoneme-level accuracy. Competitive thresholds: phone accuracy PCC > 0.61, sentence total PCC > 0.74
  - **L2-ARCTIC:** Report MDD F1, precision, recall, and False Rejection Rate. Competitive: F1 > 63%, FRR < 5%
  - **Required baselines:** Kaldi GOP (traditional), wav2vec2-CTC (SSL baseline), GOPT (multi-granularity), Microsoft Azure PA (commercial)
- **Design C — FL weighting ablation:**
  - Compare FL-weighted vs unweighted pronunciation scores in correlation with human intelligibility/comprehensibility ratings
  - Demonstrate differential effects for learners from ≥3 L1 backgrounds
  - This is the novel contribution validation — essential for publication

---

## 11. Research Applications

This system enables research on:

1. AR-based contextual pronunciation training effectiveness vs traditional CAPT
2. Multi-object scene description as a grammar teaching intervention
3. **Functional load-weighted vs equal-weighted scoring** — impact on learner motivation, self-efficacy, and learning outcomes (novel)
4. **Intelligibility-focused vs native-likeness scoring** — comparative study using the same pipeline with FL weights on vs off
5. L1 transfer error prediction accuracy across language backgrounds (Hindi, Tamil, Mandarin, Arabic, Japanese, Korean, Spanish, French)
6. Spaced repetition applied to phoneme-level pronunciation training
7. **Multi-dimensional feedback (accuracy, fluency, prosody, completeness) vs single-score feedback** — which drives better learning outcomes?
8. Edge ML deployment feasibility and privacy implications for educational AI
9. Longitudinal pronunciation development tracking with automated metrics at three granularities
10. Teacher-facing analytics for data-driven pronunciation instruction
11. Offline-capable language learning for resource-constrained environments
12. Comparative effectiveness of contextual (AR-situated) vs decontextualized pronunciation practice
13. **HuBERT retrieval-based MDD validation** — testing training-free approach in a deployed educational system (ecological validity study)
14. **Prosodic development trajectories** — tracking nPVI-V, stress accuracy, and intonation over weeks/months of practice

---

## 12. Version History

### v3.0 Changelog (from v2.0)

| Component | v2.0 | v3.0 | Rationale |
|---|---|---|---|
| **Object Detection** | YOLOv8n ONNX (~13 MB, 37.3 mAP) | YOLO11s ONNX (~38 MB, 47.0 mAP) | +10 mAP improvement — substantially better detection of smaller/occluded objects; 22% fewer params than YOLOv8m; same ONNX Runtime Web pipeline, zero code changes |
| **Silero VAD** | Server-side fluency analysis tool | Browser-side only (recording auto-trim); removed from server-side fluency pipeline entirely | Silero VAD cannot distinguish filled pauses from speech; CrisperWhisper word timestamps + MFA phone boundaries provide superior pause detection with disfluency classification; aligns with Vaidya et al. (arXiv 2024) finding that SSL representations outperform hand-crafted features for fluency |
| **Fluency Pipeline** | Silero VAD + CrisperWhisper | CrisperWhisper timestamps + MFA phone boundaries (no VAD) | CrisperWhisper provides pause detection (inter-word gaps), filled pause/repetition labels, and word timing; MFA provides sub-word phone boundaries for phonation ratio and nPVI-V; together they fully replace and exceed Silero VAD |
| **Database** | SQLite only | SQLite (local) / PostgreSQL (hosted) | SQLite does not support concurrent writers; PostgreSQL needed for 50-user classroom deployment |
| **Deployment** | Single-process local only | Cloud GPU (T4) + browser split architecture | Laptop has no NVIDIA GPU; cloud T4 handles 50 concurrent learners at ~$0.35/hr; browser-side YOLO11s + Silero VAD remain on-device |
| **Architecture** | Single-user, single-process | FastAPI gateway → Redis → Celery worker (single T4 GPU) | Async job queue prevents request starvation with 50 users; single worker sufficient for pilot study throughput |
| **Auth** | None | JWT/session-based per learner | Multi-user classroom requires user isolation for progress tracking |

### v2.0 Changelog (from v1.0)

| Component | v1.0 | v2.0 | Rationale |
|---|---|---|---|
| **ASR** | faster-whisper (small/medium) | CrisperWhisper (nyrahealth/CrisperWhisper, transformers) | Whisper normalizes L2 mispronunciations (Cai, 2025; Ballier et al., 2023); CrisperWhisper preserves verbatim speech including disfluencies (Wagner et al., Interspeech 2024) |
| **MDD/Pronunciation** | Wav2Vec2 (wav2vec2-lv-60-espeak-cv-ft) CTC-based | HuBERT (hubert-large-ls960-ft) retrieval-based MDD | HuBERT outperforms Wav2Vec2 and WavLM for MDD (Tu et al., 2025); training-free retrieval achieves F1 69.60% on L2-ARCTIC |
| **Reading Accuracy** | Sentence Transformers cosine similarity (all-MiniLM-L6-v2) | jiwer word-level edit distance alignment | Semantic similarity is fundamentally wrong for reading accuracy (BERTScore gives F1 0.97 for antonyms); word-level alignment is standard across all competitive CAPT systems |
| **Prosody** | None | MFA + parselmouth: F0, stress, intonation, nPVI-V rhythm | SpeechOcean762 and CEFR 2018 expect prosody as an independent scoring dimension; absent from v1.0 |
| **Scoring** | Single composite score | Hierarchical phone→word→utterance with 4 dimensions (accuracy, completeness, fluency, prosody) | Standard since GOPT (Gong et al., ICASSP 2022); SpeechOcean762 annotates all 4 dimensions |
| **G2P Fallback** | espeak-ng (IPA output) | g2p-en seq2seq (ARPAbet output) | espeak-ng introduces IPA/ARPAbet phoneset inconsistency; g2p-en trained on CMUdict outputs consistent ARPAbet |
| **Fluency** | Silero VAD only (basic pause detection) | CrisperWhisper disfluency-based (speed/breakdown/repair sub-constructs) + MFA timing | CrisperWhisper enables filled pause and repetition detection; MFA provides sub-word phone boundaries; fluency decomposed per Skehan (2009) framework |
| **Rhythm** | PVI mentioned but not implementable (no forced alignment) | nPVI-V from MFA phone boundaries | Grabe & Low (2002); MFA provides the vowel/consonant segmentation needed for rhythm metrics |
| **FL Weighting** | Functional load values cited (Catford 1987, Munro & Derwing 2006) | FL values explicitly from Brown (1988, 1991) with per-value source citations | Publication requires traceable, reproducible values |

### Weights and Formulas — Literature Sources

| Formula | Weights | Primary Sources |
|---|---|---|
| Phonetic distance features | manner 0.30, place 0.25, voicing 0.15, height 0.15, backness 0.15 | Steriade (2001) perceptual salience hierarchy; Flemming (2004) contrast and perceptual distinctiveness |
| FL-weighted error modifiers | substitution ×1.0, deletion ×0.8, insertion ×0.5 | Munro & Derwing (2006) error type impact; Zampini (2008) L2 phonological processes |
| Prosody composite | stress 0.35, intonation 0.30, rhythm 0.20, pitch range 0.15 | Hahn (2004), Zielinski (2008) for stress; Munro & Derwing (2001), Kang et al. (2010) for intonation; Ordin & Polyanskaya (2015) for rhythm; Kang (2010) for pitch range |
| Fluency composite | breakdown 0.35, speed 0.30, repair 0.20, rhythm 0.15 | de Jong (2016) breakdown primacy; Tavakoli et al. (2020) speed metrics; Skehan (2009) repair construct |
| Utterance total | accuracy 0.35, fluency 0.25, prosody 0.25, completeness 0.15 | SpeechOcean762 (Zhang et al., 2021) annotation weighting; CEFR 2018 phonological descriptors; El Kheir et al. (EMNLP Findings 2023) review of APA methods |

---

## 13. Key References

### Speech Analysis Pipeline
- **Witt & Young (2000)** — Original GOP scoring method. *Speech Communication*.
- **Tu, H.T. et al. (2025)** — Training-free retrieval-based MDD with HuBERT, F1 69.60%. *arXiv:2511.20107*.
- **Wagner, L. et al. (2024)** — CrisperWhisper: verbatim ASR with accurate timestamps. *Interspeech 2024*.
- **Gong, Y. et al. (2022)** — GOPT: multi-granularity pronunciation assessment. *ICASSP 2022*.
- **Zhang, J. et al. (2021)** — SpeechOcean762 corpus and annotation schema. *Interspeech 2021*.
- **Zhao, G. et al. (2018)** — L2-ARCTIC corpus. *Interspeech 2018*.

### Intelligibility & Functional Load
- **Levis, J.M. (2005)** — Changing contexts and shifting paradigms in pronunciation teaching. *TESOL Quarterly*.
- **Munro, M.J. & Derwing, T.M. (1995)** — Foreign accent, comprehensibility, and intelligibility. *Language Learning*.
- **Munro, M.J. & Derwing, T.M. (2006)** — The functional load principle in ESL pronunciation instruction. *System*.
- **Catford, J.C. (1987)** — Phonetics and the teaching of pronunciation. *Current Perspectives on Pronunciation*.
- **Brown, A. (1988, 1991)** — Functional load and the teaching of pronunciation. *TESOL Quarterly*; *World Englishes*.
- **Kang, O. & Moran, M. (2014)** — Functional load-based intelligibility in pronunciation teaching. *Frontiers in Communication*.

### Prosody & Fluency
- **Grabe, E. & Low, E.L. (2002)** — Durational variability in speech and the nPVI rhythm metric. *Laboratory Phonology 7*.
- **Ordin, M. & Polyanskaya, L. (2015)** — nPVI-V for L2 rhythm assessment. *Speech Communication*.
- **Hahn, L.D. (2004)** — Primary stress and intelligibility. *TESOL Quarterly*.
- **Kang, O., Rubin, D. & Pickering, L. (2010)** — Suprasegmental measures of accentedness. *Applied Linguistics*.
- **Skehan, P. (2009)** — Modelling second language performance: fluency framework. *Applied Linguistics*.
- **Tavakoli, P. & Skehan, P. (2005)** — Strategic planning, task structure and performance testing. *Planning and Task Performance*.
- **de Jong, N.H. (2016)** — Predicting pauses in L1 and L2 speech. *Studies in Second Language Acquisition*.
- **Tavakoli, P. et al. (2020)** — Fluency across CEFR levels. *Applied Linguistics*.

### Scoring & Assessment
- **Cai, W. et al. (2025)** — Duolingo pronunciation scorer aligned with applied linguistics constructs. *Language Learning*.
- **El Kheir, Y. et al. (2023)** — Comprehensive APA technical review. *EMNLP Findings*.
- **Council of Europe (2018)** — CEFR Companion Volume with New Descriptors (expanded phonological control scales).
- **Boersma, P. & Weenink, D. (2001)** — Praat: doing phonetics by computer.
- **McAuliffe, M. et al. (2017)** — Montreal Forced Aligner. *Interspeech 2017*.

---

*End of Specification Document*
