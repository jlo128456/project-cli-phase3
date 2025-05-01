# lib/db/models.py

from contextlib import contextmanager                           # for session context manager
from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base         # base class for ORM models
from sqlalchemy.orm import sessionmaker, relationship           # session factory & relationships

from lib.helpers import get_database_url, create_db_engine      # helpers for engine setup



# Read DATABASE_URL (from env or default) and create SQLAlchemy Engine
DATABASE_URL = get_database_url()
engine       = create_db_engine(DATABASE_URL, echo=False)

# sessionmaker factory to generate new Session objects bound to our engine
SessionLocal = sessionmaker(bind=engine)

@contextmanager # only activate when it called in the click command and wraps your generator function into a context‐manager factory, but it doesn’t open any sessions yet.
def get_db_session():
    """
    Provide a transactional scope around a series of operations.
    Commits on success, rolls back on exception, and always closes.
    """
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()



# All ORM models will inherit from this Base
Base = declarative_base()



# Many-to-many link table between books and genres
book_genre = Table(
    "book_genre",
    Base.metadata,
    Column("book_id",  Integer, ForeignKey("books.id"),  primary_key=True),
    Column("genre_id", Integer, ForeignKey("genres.id"), primary_key=True),
)

#  ORM Models 

class Author(Base):
    __tablename__ = "authors"       # table name in the database

    id   = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    # one-to-many: an author can have multiple books
    books = relationship(
        "Book",
        back_populates="author",
        cascade="all, delete-orphan"
    )

class Genre(Base):
    __tablename__ = "genres"

    id   = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    # many-to-many: a genre can be applied to many books
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

    # many-to-one: each book has a single author
    author = relationship("Author", back_populates="books")

    # many-to-many: each book may have multiple genres
    genres = relationship(
        "Genre",
        secondary=book_genre,
        back_populates="books"
    )
