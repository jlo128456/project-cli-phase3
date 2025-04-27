# db/models.py

from contextlib import contextmanager
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# import your helpers
from lib.helpers import get_database_url, create_db_engine

# ── Engine & Session ────────────────────────────────────────────────────────
DATABASE_URL = get_database_url()
engine       = create_db_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

@contextmanager
def get_db_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

Base = declarative_base()

# ── Association Table ───────────────────────────────────────────────────────
book_genre = Table(
    "book_genre",
    Base.metadata,
    Column("book_id",  ForeignKey("books.id"),  primary_key=True),
    Column("genre_id", ForeignKey("genres.id"), primary_key=True),
)

# ── Models ───────────────────────────────────────────────────────────────────

class Author(Base):
    __tablename__ = "authors"
    id    = Column(Integer, primary_key=True)
    name  = Column(String, unique=True, nullable=False)
    books = relationship(
        "Book",
        back_populates="author",
        cascade="all, delete-orphan"
    )

class Genre(Base):
    __tablename__ = "genres"
    id    = Column(Integer, primary_key=True)
    name  = Column(String, unique=True, nullable=False)
    books = relationship(
        "Book",
        secondary=book_genre,
        back_populates="genres"
    )

class Book(Base):
    __tablename__ = "books"
    id             = Column(Integer, primary_key=True)
    title          = Column(String, nullable=False)
    published_date = Column(Date)
    author_id      = Column(Integer, ForeignKey("authors.id"), nullable=False)

    author = relationship("Author", back_populates="books")
    genres = relationship(
        "Genre",
        secondary=book_genre,
        back_populates="books"
    )