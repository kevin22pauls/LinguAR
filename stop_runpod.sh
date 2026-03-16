#!/bin/bash
# Stop all LinguAR services
echo "Stopping LinguAR..."
pkill -f "gunicorn backend.main" 2>/dev/null && echo "  Gunicorn stopped." || echo "  Gunicorn not running."
pkill -f "celery -A backend" 2>/dev/null && echo "  Celery stopped." || echo "  Celery not running."
echo "Done. (PostgreSQL and Redis containers still running)"
