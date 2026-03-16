from __future__ import annotations

"""
JWT authentication for hosted mode.

In local mode (default), auth is bypassed and a default learner is used.
In hosted mode, users must register/login to get a JWT token.
"""

import logging
from datetime import datetime, timedelta
from hashlib import sha256

import jwt
from fastapi import HTTPException, Depends, Header
from sqlalchemy.orm import Session

from backend.config import settings
from backend.database.db import get_db
from backend.database.schema import LearnerProfile

logger = logging.getLogger(__name__)

SECRET_KEY = settings.secret_key
ALGORITHM = "HS256"
TOKEN_EXPIRE_HOURS = 24


def hash_password(password: str) -> str:
    return sha256(password.encode()).hexdigest()


def create_token(learner_id: str) -> str:
    payload = {
        "sub": learner_id,
        "exp": datetime.utcnow() + timedelta(hours=TOKEN_EXPIRE_HOURS),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> str:
    """Decode JWT and return learner_id. Raises HTTPException on failure."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


def get_current_learner(
    authorization: str | None = Header(None),
    db: Session = Depends(get_db),
) -> str:
    """
    FastAPI dependency — returns learner_id.
    In local mode: always returns "default".
    In hosted mode: requires valid JWT Bearer token.
    """
    if settings.deployment_mode == "local":
        return "default"

    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing authorization header")

    token = authorization.split(" ", 1)[1]
    learner_id = decode_token(token)

    learner = db.query(LearnerProfile).filter_by(learner_id=learner_id).first()
    if not learner:
        raise HTTPException(status_code=404, detail="Learner not found")

    return learner_id


def register(display_name: str, password: str, db: Session) -> dict:
    """Register a new learner. Returns token."""
    import uuid
    learner_id = str(uuid.uuid4())

    learner = LearnerProfile(
        learner_id=learner_id,
        display_name=display_name,
    )
    db.add(learner)
    db.commit()

    token = create_token(learner_id)
    return {"token": token, "learner_id": learner_id}


def login(learner_id: str, db: Session) -> dict:
    """Login an existing learner. Returns token."""
    learner = db.query(LearnerProfile).filter_by(learner_id=learner_id).first()
    if not learner:
        raise HTTPException(status_code=404, detail="Learner not found")

    token = create_token(learner_id)
    return {"token": token, "learner_id": learner_id}
