"""LinguAR — FastAPI application entry point."""

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response as StarletteResponse

from pathlib import Path

from backend.config import TEMPLATES_DIR, STATIC_DIR, settings
from backend.database.db import init_db
from backend.routers import analysis, classroom, auth

app = FastAPI(title="LinguAR", version="0.1.0")


@app.on_event("startup")
def on_startup():
    init_db()

    # Preload ML models in background thread so first request isn't slow
    if not settings.lazy_models:
        import threading

        def _preload():
            import logging
            log = logging.getLogger("preload")
            try:
                log.info("Preloading ASR model...")
                from backend.models.crisperwhisper_model import get_asr_pipeline
                get_asr_pipeline()
                log.info("Preloading HuBERT model...")
                from backend.models.hubert_model import get_hubert_ctc
                get_hubert_ctc()
                log.info("Preloading FAISS phoneme pool...")
                from backend.services.mdd_engine import load_phoneme_pool
                load_phoneme_pool()
                log.info("All models preloaded.")
            except Exception as e:
                log.warning("Model preload failed (will load on first request): %s", e)

        threading.Thread(target=_preload, daemon=True).start()
    else:
        import logging
        logging.getLogger("startup").info("Lazy model loading enabled — models load on first request")


# CORS — controlled via CORS_ORIGINS env var (comma-separated or "*" for dev)
_cors_origins = (
    ["*"] if settings.cors_origins == "*"
    else [o.strip() for o in settings.cors_origins.split(",")]
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=_cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# COOP/COEP headers — required for SharedArrayBuffer (WASM threads in VAD)
class COOPCOEPMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response: StarletteResponse = await call_next(request)
        response.headers["Cross-Origin-Opener-Policy"] = "same-origin"
        response.headers["Cross-Origin-Embedder-Policy"] = "credentialless"
        return response


app.add_middleware(COOPCOEPMiddleware)

# Static files and templates
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

# Register API routers
app.include_router(analysis.router)
app.include_router(classroom.router)
app.include_router(auth.router)


# ── VAD/WASM files at root (bundle.min.js resolves these relative to page) ──

VAD_DIR = STATIC_DIR / "vad"


@app.get("/silero_vad_legacy.onnx")
async def vad_model():
    from fastapi.responses import FileResponse
    return FileResponse(VAD_DIR / "silero_vad_legacy.onnx", media_type="application/octet-stream")


@app.get("/ort-wasm-simd-threaded.wasm")
async def ort_wasm():
    from fastapi.responses import FileResponse
    return FileResponse(VAD_DIR / "ort-wasm-simd-threaded.wasm", media_type="application/wasm")


@app.get("/ort-wasm-simd-threaded.mjs")
async def ort_mjs():
    from fastapi.responses import FileResponse
    return FileResponse(VAD_DIR / "ort-wasm-simd-threaded.mjs", media_type="application/javascript")


@app.get("/vad.worklet.bundle.min.js")
async def vad_worklet():
    from fastapi.responses import FileResponse
    return FileResponse(VAD_DIR / "vad.worklet.bundle.min.js", media_type="application/javascript")


# ── Page routes ──────────────────────────────────────────────────────────────

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")


@app.get("/scan")
async def scan(request: Request):
    return templates.TemplateResponse(request=request, name="scan.html")


@app.get("/practice")
async def practice(request: Request):
    return templates.TemplateResponse(request=request, name="practice.html")


@app.get("/dashboard")
async def dashboard(request: Request):
    return templates.TemplateResponse(request=request, name="dashboard.html")


@app.get("/teacher")
async def teacher(request: Request):
    return templates.TemplateResponse(request=request, name="teacher.html")


@app.get("/teacher/student/{learner_id}")
async def teacher_student_detail(request: Request, learner_id: str):
    return templates.TemplateResponse(
        request=request,
        name="student_detail.html",
        context={"learner_id": learner_id},
    )


@app.get("/exercise/{recording_id}")
async def exercise_detail(request: Request, recording_id: int):
    return templates.TemplateResponse(
        request=request,
        name="exercise.html",
        context={"recording_id": recording_id},
    )


# ── Health check ─────────────────────────────────────────────────────────────

@app.get("/health")
async def health_check():
    """Health check for load balancers and container orchestration."""
    checks = {"status": "ok", "database": "ok", "redis": "ok"}
    try:
        from backend.database.db import SessionLocal
        db = SessionLocal()
        db.execute(__import__("sqlalchemy").text("SELECT 1"))
        db.close()
    except Exception:
        checks["database"] = "unavailable"
        checks["status"] = "degraded"
    try:
        import redis as _redis
        r = _redis.from_url(settings.redis_url, socket_connect_timeout=2)
        r.ping()
    except Exception:
        checks["redis"] = "unavailable"
        checks["status"] = "degraded"
    return checks
