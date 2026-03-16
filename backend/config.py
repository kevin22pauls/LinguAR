"""Application configuration via pydantic-settings."""

import os
from pathlib import Path
from pydantic_settings import BaseSettings

# Fix OpenMP conflict between torch and faiss on Windows
os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")


BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent
DATA_DIR = BASE_DIR / "data"
MODEL_CACHE_DIR = BASE_DIR / "models" / "cache"
FRONTEND_DIR = PROJECT_DIR / "frontend"
TEMPLATES_DIR = FRONTEND_DIR / "templates"
STATIC_DIR = FRONTEND_DIR / "static"


class Settings(BaseSettings):
    # Deployment
    deployment_mode: str = "local"  # "local" or "server"
    debug: bool = True

    # Database (PostgreSQL for production; override via DB_URL env var)
    db_url: str = "postgresql://linguar:linguar@localhost:5432/linguar"

    # Server
    host: str = "0.0.0.0"
    port: int = 8000

    # Security
    secret_key: str = "linguar-dev-secret-change-in-production"
    cors_origins: str = "*"  # comma-separated origins, or "*" for dev

    # Models — production defaults (CrisperWhisper + HuBERT-large)
    # Override via .env for local dev (e.g. WHISPER_MODEL=openai/whisper-tiny)
    whisper_model: str = "nyrahealth/CrisperWhisper"  # REQUIRES: HF access token + nyrahealth transformers fork
    hubert_model: str = "facebook/hubert-large-ls960-ft"
    lazy_models: bool = False  # False = preload at startup (production); True = load on first request (dev)

    # Celery / Redis
    redis_url: str = "redis://localhost:6379/0"

    # Audio
    sample_rate: int = 16000

    # MDD hyperparameters (Tu et al. 2025)
    mdd_top_k: int = 10
    mdd_threshold: float = 0.7

    # L1 transfer — all users are Tamil speakers
    default_l1: str = "tamil"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
