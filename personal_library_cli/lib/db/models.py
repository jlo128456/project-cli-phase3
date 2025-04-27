import os
from sqlalchemy import (
    create_engine, Column, Integer, String, Date, ForeignKey, Table
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Database URL (defaults to local SQLite file)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///library.db")
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

# Base class and session
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

# Association table for books ↔ genres
book_genre = Table(
    "book_genre", Base.metadata,
    Column("book_id", ForeignKey("books.id"), primary_key=True),
    Column("genre_id", ForeignKey("genres.id"), primary_key=True)
)

class Author(Base):
    __tablename__ = "authors"
    id   = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    books = relationship("Book", back_populates="author")

class Genre(Base):
    __tablename__ = "genres"
    id   = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    books = relationship(
        "Book", secondary=book_genre, back_populates="genres"
    )

class Book(Base):
    __tablename__ = "books"
    id             = Column(Integer, primary_key=True)
    title          = Column(String)
    published_date = Column(Date)
    author_id      = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")
    genres = relationship(
        "Genre", secondary=book_genre, back_populates="books"
    )