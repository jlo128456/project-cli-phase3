# lib/db/models.py

from contextlib import contextmanager
from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from lib.db.session import get_db_session

from lib.db.session import SessionLocal, engine  # en FIXED: No helper import

# """ # Context manager for DB session
# @contextmanager
# def get_db_session():
#     session = SessionLocal()
#     try:
#         yield session
#         session.commit()
#     except:
#         session.rollback()
#         raise
#     finally:
#         session.close() """

Base = declarative_base()

book_genre = Table(
    "book_genre", Base.metadata,
    Column("book_id",  Integer, ForeignKey("books.id"),  primary_key=True),
    Column("genre_id", Integer, ForeignKey("genres.id"), primary_key=True),
)

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    books = relationship("Book", back_populates="author", cascade="all, delete-orphan")

class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    books = relationship("Book", secondary=book_genre, back_populates="genres")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    published_date = Column(Date)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    author = relationship("Author", back_populates="books")
    genres = relationship("Genre", secondary=book_genre, back_populates="books")
