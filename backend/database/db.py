"""Database engine and session management."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from backend.config import settings


_is_sqlite = "sqlite" in settings.db_url

_engine_kwargs = {}
if _is_sqlite:
    _engine_kwargs["connect_args"] = {"check_same_thread": False}
else:
    # PostgreSQL connection pooling for production
    _engine_kwargs.update(
        pool_size=20,
        max_overflow=40,
        pool_pre_ping=True,
        pool_recycle=3600,
    )

engine = create_engine(
    settings.db_url,
    echo=settings.debug,
    **_engine_kwargs,
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass


def get_db():
    """FastAPI dependency — yields a DB session, auto-closes."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Run Alembic migrations to create/update tables.

    Falls back to create_all() if Alembic config is not found
    (e.g., during testing or first-time dev setup).
    """
    from backend.database import schema  # noqa: F401 — registers models

    try:
        from alembic.config import Config
        from alembic import command
        import os

        ini_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "alembic.ini",
        )
        if os.path.exists(ini_path):
            alembic_cfg = Config(ini_path)
            alembic_cfg.set_main_option("sqlalchemy.url", settings.db_url)
            command.upgrade(alembic_cfg, "head")
            return
    except Exception:
        pass

    # Fallback: direct table creation (dev / testing)
    Base.metadata.create_all(bind=engine)
