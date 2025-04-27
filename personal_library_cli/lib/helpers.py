# helpers.py

import os
from sqlalchemy import create_engine

def get_database_url(env_var: str = "DATABASE_URL", default: str = "sqlite:///library.db") -> str:
    """
    Read the database URL from environment, 
    falling back to `default` if not set.
    """
    return os.getenv(env_var, default)

def create_db_engine(url: str, echo: bool = False):
    """
    Create and return a SQLAlchemy Engine.
    Automatically disables SQLite’s same-thread check when needed.
    """
    connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
    return create_engine(url, connect_args=connect_args, echo=echo)
