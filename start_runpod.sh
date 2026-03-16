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

# ── 3. PostgreSQL container ───────────────────────────────────────────────
echo "[3/8] Starting PostgreSQL..."
if docker ps -a --format '{{.Names}}' | grep -q '^linguar-pg$'; then
    docker start linguar-pg 2>/dev/null || true
else
    docker run -d \
        --name linguar-pg \
        --restart unless-stopped \
        -e POSTGRES_USER=linguar \
        -e POSTGRES_PASSWORD=linguar \
        -e POSTGRES_DB=linguar \
        -p 5432:5432 \
        -v /workspace/pgdata:/var/lib/postgresql/data \
        postgres:16
fi

# Wait for PG to be ready
echo "  -> Waiting for PostgreSQL..."
for i in $(seq 1 30); do
    if docker exec linguar-pg pg_isready -U linguar -q 2>/dev/null; then
        echo "  -> PostgreSQL ready."
        break
    fi
    sleep 1
done

# ── 4. Redis container ───────────────────────────────────────────────────
echo "[4/8] Starting Redis..."
if docker ps -a --format '{{.Names}}' | grep -q '^linguar-redis$'; then
    docker start linguar-redis 2>/dev/null || true
else
    docker run -d \
        --name linguar-redis \
        --restart unless-stopped \
        -p 6379:6379 \
        redis:7-alpine
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

# ── 8. Start services ────────────────────────────────────────────────────
echo "[8/8] Starting LinguAR services..."

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
    --workers 4 \
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
