# lib/db/session.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Inline helper (formerly from helpers.py)
def get_database_url(env_var: str = "DATABASE_URL", default: str = "sqlite:///library.db") -> str:
    return os.getenv(env_var, default)

# Engine and Session setup
DATABASE_URL = get_database_url()
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
    echo=False
)
SessionLocal = sessionmaker(bind=engine)
