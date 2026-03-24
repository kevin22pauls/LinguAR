#!/bin/bash
# ============================================================================
# LinguAR — RunPod GPU Pod Startup Script
# Run this ONCE after creating your pod. It sets up everything.
# Usage: bash start_runpod.sh
# ============================================================================
set -e

APP_DIR="/workspace/LinguAR"
VENV_DIR="$APP_DIR/.venv"
LOG_DIR="$APP_DIR/logs"

echo "============================================"
echo "  LinguAR — RunPod Deployment"
echo "============================================"

# ── 0. Check we're on RunPod ──────────────────────────────────────────────
if [ ! -d "/workspace" ]; then
    echo "ERROR: /workspace not found. Are you on a RunPod GPU Pod?"
    exit 1
fi

cd /workspace

# ── 1. Clone repo (skip if already cloned) ────────────────────────────────
if [ ! -d "$APP_DIR" ]; then
    echo "[1/8] Cloning repository..."
    echo "  -> You need to clone your repo first:"
    echo "     git clone <your-repo-url> LinguAR"
    echo "  Then re-run this script."
    exit 1
else
    echo "[1/8] Repository found at $APP_DIR"
fi

cd "$APP_DIR"
mkdir -p "$LOG_DIR" uploads backend/data/phoneme_pool backend/models/cache

# ── 2. Python venv + dependencies ─────────────────────────────────────────
if [ ! -d "$VENV_DIR" ]; then
    echo "[2/8] Creating Python virtual environment..."
    python3.11 -m venv "$VENV_DIR" 2>/dev/null || python3 -m venv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"

echo "[2/8] Installing Python dependencies..."
pip install --upgrade pip setuptools wheel -q

# Preserve CUDA-enabled PyTorch from the RunPod base image.
# Only install torch if it's missing (e.g. fresh venv without system packages).
python -c "import torch; assert torch.cuda.is_available(); print(f'  -> PyTorch {torch.__version__} (CUDA) already available, skipping torch install')" 2>/dev/null || {
    echo "  -> Installing PyTorch with CUDA 12.4 support..."
    pip install torch==2.4.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu124 -q
}

# crepe uses legacy setup.py that imports pkg_resources at build time.
# Force pip to use the venv's setuptools instead of an isolated build env.
SETUPTOOLS_USE_DISTUTILS=stdlib pip install --no-build-isolation crepe -q 2>/dev/null || \
    echo "  WARNING: crepe install failed — parselmouth still handles F0 extraction"
pip install -r requirements.txt -q

# Install nyrahealth's CrisperWhisper fork for accurate timestamps
pip install git+https://github.com/nyrahealth/transformers.git@crisper_whisper -q 2>/dev/null || \
    echo "  WARNING: CrisperWhisper fork install failed. Using standard transformers."

# NLTK data
python -c "import nltk; nltk.download('cmudict', quiet=True); nltk.download('averaged_perceptron_tagger', quiet=True)" 2>/dev/null

echo "  -> Dependencies installed."

# ── 3. PostgreSQL (install + run natively) ──────────────────────────────
echo "[3/8] Starting PostgreSQL..."
if ! command -v pg_isready &>/dev/null; then
    echo "  -> Installing PostgreSQL..."
    apt-get update -qq && apt-get install -y -qq postgresql postgresql-client >/dev/null 2>&1
fi

# Find PostgreSQL version directory
PG_BIN=$(dirname $(find /usr/lib/postgresql -name "pg_ctl" 2>/dev/null | head -1) 2>/dev/null)
PG_DATA="/var/lib/postgresql/data"

# Fix permissions — let postgres user own its data dir
mkdir -p "$PG_DATA"
chown -R postgres:postgres /var/lib/postgresql
chown -R postgres:postgres /var/run/postgresql 2>/dev/null || mkdir -p /var/run/postgresql && chown postgres:postgres /var/run/postgresql

# Initialize DB cluster if needed
if [ ! -f "$PG_DATA/PG_VERSION" ]; then
    su - postgres -c "$PG_BIN/initdb -D $PG_DATA"
fi

# Start PostgreSQL
su - postgres -c "$PG_BIN/pg_ctl -D $PG_DATA -l $LOG_DIR/postgresql.log start" 2>/dev/null || true
sleep 2

# Create user and database if they don't exist
su - postgres -c "psql -tc \"SELECT 1 FROM pg_roles WHERE rolname='linguar'\" | grep -q 1" 2>/dev/null || \
    su - postgres -c "psql -c \"CREATE USER linguar WITH PASSWORD 'linguar';\"" 2>/dev/null
su - postgres -c "psql -tc \"SELECT 1 FROM pg_database WHERE datname='linguar'\" | grep -q 1" 2>/dev/null || \
    su - postgres -c "psql -c \"CREATE DATABASE linguar OWNER linguar;\"" 2>/dev/null

echo "  -> Waiting for PostgreSQL..."
for i in $(seq 1 15); do
    if pg_isready -q 2>/dev/null; then
        echo "  -> PostgreSQL ready."
        break
    fi
    sleep 1
done

# ── 4. Redis (install + run natively) ──────────────────────────────────
echo "[4/8] Starting Redis..."
if ! command -v redis-server &>/dev/null; then
    echo "  -> Installing Redis..."
    apt-get install -y -qq redis-server >/dev/null 2>&1
fi

if ! redis-cli ping &>/dev/null 2>&1; then
    redis-server --daemonize yes --logfile "$LOG_DIR/redis.log"
fi
echo "  -> Redis ready."

# ── 5. Create .env for production ─────────────────────────────────────────
echo "[5/8] Configuring environment..."
if [ ! -f "$APP_DIR/.env" ]; then
    # Generate a random secret key
    SECRET=$(python -c "import secrets; print(secrets.token_urlsafe(32))")
    cat > "$APP_DIR/.env" << EOF
DB_URL=postgresql://linguar:linguar@localhost:5432/linguar
SECRET_KEY=$SECRET
CORS_ORIGINS=*
WHISPER_MODEL=nyrahealth/CrisperWhisper
HUBERT_MODEL=facebook/hubert-large-ls960-ft
LAZY_MODELS=false
REDIS_URL=redis://localhost:6379/0
DEPLOYMENT_MODE=server
DEBUG=false
EOF
    echo "  -> .env created with random SECRET_KEY."
else
    echo "  -> .env already exists, skipping."
fi

# ── 6. Run database migrations ────────────────────────────────────────────
echo "[6/8] Running database migrations..."
source "$VENV_DIR/bin/activate"
cd "$APP_DIR"
python -c "
from backend.database.db import init_db
init_db()
print('  -> Database tables created.')
"

# ── 7. Build phoneme pool (if not already built) ─────────────────────────
POOL_DIR="$APP_DIR/backend/data/phoneme_pool"
if [ -f "$POOL_DIR/faiss_index.bin" ] && [ -f "$POOL_DIR/embeddings.npy" ]; then
    echo "[7/8] Phoneme pool already built, skipping."
else
    echo "[7/8] Building phoneme pool (this takes ~30 min on GPU)..."
    echo "  -> Skipping for now. Run manually when L2-ARCTIC dataset is available:"
    echo "     python scripts/build_phoneme_pool.py --dataset-dir /workspace/l2arctic --mode ctc"
fi

# ── 8. YOLO11s ONNX model (export if missing) ────────────────────────────
YOLO_MODEL="$APP_DIR/frontend/static/models/yolo11s.onnx"
if [ -f "$YOLO_MODEL" ]; then
    echo "[8/9] YOLO11s ONNX model already exists, skipping."
else
    echo "[8/9] Exporting YOLO11s ONNX model..."
    pip install ultralytics -q 2>/dev/null
    mkdir -p "$APP_DIR/frontend/static/models"
    python -c "
from ultralytics import YOLO
model = YOLO('yolo11s.pt')
model.export(format='onnx', imgsz=640, simplify=True)
import shutil
shutil.move('yolo11s.onnx', '$APP_DIR/frontend/static/models/yolo11s.onnx')
print('  -> YOLO11s ONNX exported successfully.')
" 2>/dev/null || echo "  WARNING: YOLO export failed. Place yolo11s.onnx in frontend/static/models/ manually."
fi

# ── 9. Start services ────────────────────────────────────────────────────
echo "[9/9] Starting LinguAR services..."

# Kill any existing processes
pkill -f "gunicorn backend.main" 2>/dev/null || true
pkill -f "celery -A backend" 2>/dev/null || true
sleep 2

# Start Celery worker (background)
echo "  -> Starting Celery worker..."
nohup celery -A backend.services.tasks worker \
    --loglevel=info \
    --concurrency=1 \
    > "$LOG_DIR/celery.log" 2>&1 &
echo "  -> Celery PID: $!"

# Start Gunicorn (FastAPI)
echo "  -> Starting Gunicorn (4 workers)..."
nohup gunicorn backend.main:app \
    --worker-class uvicorn.workers.UvicornWorker \
    --workers 1 \
    --bind 0.0.0.0:8000 \
    --timeout 120 \
    --graceful-timeout 30 \
    --access-logfile "$LOG_DIR/access.log" \
    --error-logfile "$LOG_DIR/error.log" \
    > "$LOG_DIR/gunicorn.log" 2>&1 &
echo "  -> Gunicorn PID: $!"

# Wait for app to be ready
echo "  -> Waiting for app to start..."
for i in $(seq 1 60); do
    if curl -sf http://localhost:8000/health > /dev/null 2>&1; then
        HEALTH=$(curl -s http://localhost:8000/health)
        echo ""
        echo "============================================"
        echo "  LinguAR is RUNNING!"
        echo "============================================"
        echo "  Health: $HEALTH"
        echo ""
        echo "  Access your app at:"
        echo "  https://<your-pod-id>-8000.proxy.runpod.net"
        echo ""
        echo "  Logs: $LOG_DIR/"
        echo "    - gunicorn.log (API server)"
        echo "    - celery.log   (ML worker)"
        echo "    - access.log   (HTTP requests)"
        echo "============================================"
        exit 0
    fi
    sleep 3
done

echo "ERROR: App did not start within 3 minutes. Check logs:"
echo "  tail -50 $LOG_DIR/error.log"
echo "  tail -50 $LOG_DIR/celery.log"
exit 1
