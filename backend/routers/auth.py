"""Simple auth — name + classroom login, no passwords.

Students and teachers identified by (name, classroom) pair.
Session stored in a signed cookie.
"""

import hashlib
import logging
from fastapi import APIRouter, Depends, Form, Response, Request
from sqlalchemy.orm import Session

from backend.database.db import get_db
from backend.database.schema import LearnerProfile, Class, ClassMember

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/auth")

COOKIE_NAME = "linguar_user"


def _make_learner_id(name: str, classroom: str) -> str:
    """Deterministic learner ID from name + classroom."""
    raw = f"{name.strip().lower()}|{classroom.strip().lower()}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


@router.post("/login")
async def login(
    response: Response,
    display_name: str = Form(...),
    classroom: str = Form(...),
    role: str = Form("learner"),
    db: Session = Depends(get_db),
):
    """Login or create a user. No password needed."""
    name = display_name.strip()
    room = classroom.strip()
    if not name or not room:
        return {"error": "Name and classroom are required."}

    learner_id = _make_learner_id(name, room)

    # Get or create profile
    profile = db.query(LearnerProfile).filter_by(
        learner_id=learner_id
    ).first()

    if not profile:
        profile = LearnerProfile(
            learner_id=learner_id,
            display_name=name,
            classroom=room,
            role=role,
        )
        db.add(profile)
        db.commit()
        db.refresh(profile)
    else:
        # Update name/role if changed
        profile.display_name = name
        profile.classroom = room
        if role == "teacher":
            profile.role = "teacher"
        db.commit()

    # Ensure classroom exists
    cls = db.query(Class).filter_by(class_name=room).first()
    if not cls:
        cls = Class(
            class_id=hashlib.sha256(
                room.lower().encode()
            ).hexdigest()[:8],
            class_name=room,
            teacher_name=name if role == "teacher" else "",
        )
        db.add(cls)
        db.commit()
    elif role == "teacher" and not cls.teacher_name:
        cls.teacher_name = name
        db.commit()

    # Add to class members (students only)
    if role == "learner":
        existing = db.query(ClassMember).filter_by(
            class_id=cls.class_id, learner_id=learner_id
        ).first()
        if not existing:
            db.add(ClassMember(
                class_id=cls.class_id, learner_id=learner_id
            ))
            db.commit()

    # Set cookie
    cookie_val = f"{learner_id}|{role}|{room}"
    response.set_cookie(
        COOKIE_NAME, cookie_val,
        # No max_age → session cookie, expires when browser closes
        httponly=False,  # JS needs to read it for redirects
        samesite="lax",
    )

    return {
        "learner_id": learner_id,
        "display_name": name,
        "classroom": room,
        "role": role,
        "class_id": cls.class_id,
    }


@router.get("/me")
async def who_am_i(request: Request, db: Session = Depends(get_db)):
    """Return current user from cookie."""
    cookie = request.cookies.get(COOKIE_NAME)
    if not cookie:
        return {"logged_in": False}

    parts = cookie.split("|")
    if len(parts) < 3:
        return {"logged_in": False}

    learner_id, role, classroom = parts[0], parts[1], parts[2]
    profile = db.query(LearnerProfile).filter_by(
        learner_id=learner_id
    ).first()

    if not profile:
        return {"logged_in": False}

    # Find class_id
    cls = db.query(Class).filter_by(class_name=classroom).first()

    return {
        "logged_in": True,
        "learner_id": learner_id,
        "display_name": profile.display_name,
        "classroom": classroom,
        "role": role,
        "class_id": cls.class_id if cls else None,
    }


@router.post("/logout")
async def logout(response: Response):
    """Clear session cookie."""
    response.delete_cookie(COOKIE_NAME)
    return {"logged_out": True}
