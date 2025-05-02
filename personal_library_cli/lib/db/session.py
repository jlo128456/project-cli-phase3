from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.helpers import get_database_url

# ── Engine & Session Setup ─────────────────────────────

DATABASE_URL = get_database_url()
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
    echo=False
)
SessionLocal = sessionmaker(bind=engine)