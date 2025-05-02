#!/usr/bin/env python3
# seed.py

import datetime
import os
import sys



PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


from lib.db.models import Base, engine, get_db_session, Author, Genre, Book

# ── Data to seed ────────────────────────────────────────────────────────────

AUTHOR_NAMES = [
    "J. R. R. Tolkien",
    "George Orwell",
    "Harper Lee",
]

GENRE_NAMES = [
    "Fantasy",
    "Dystopian",
    "Classic",
]

BOOKS = [
    {
        "title": "The Hobbit",
        "published_date": datetime.date(1937, 9, 21),
        "author_name": "J. R. R. Tolkien",
        "genres": ["Fantasy", "Classic"],
    },
    {
        "title": "1984",
        "published_date": datetime.date(1949, 6, 8),
        "author_name": "George Orwell",
        "genres": ["Dystopian", "Classic"],
    },
    {
        "title": "To Kill a Mockingbird",
        "published_date": datetime.date(1960, 7, 11),
        "author_name": "Harper Lee",
        "genres": ["Classic"],
    },
]

# ── Seeding helpers ──────────────────────────────────────────────────────────

def create_schema():
    """Create all tables if they don’t exist."""
    Base.metadata.create_all(bind=engine)

def seed_authors(session):
    """Insert authors if missing."""
    for name in AUTHOR_NAMES:
        if not session.query(Author).filter_by(name=name).first():
            session.add(Author(name=name))

def seed_genres(session):
    """Insert genres if missing."""
    for name in GENRE_NAMES:
        if not session.query(Genre).filter_by(name=name).first():
            session.add(Genre(name=name))

def seed_books(session):
    """Insert books, wiring up their author/genre relationships."""
    for data in BOOKS:
        if session.query(Book).filter_by(title=data["title"]).first():
            continue

        author = session.query(Author).filter_by(name=data["author_name"]).one()
        genres = session.query(Genre).filter(Genre.name.in_(data["genres"])).all()
        book = Book(
            title=data["title"],
            published_date=data["published_date"],
            author=author,
            genres=genres,
        )
        session.add(book)

# ── Main ────────────────────────────────────────────────────────────────────

def main():
    create_schema()
    with get_db_session() as session:
        seed_authors(session)
        seed_genres(session)
        session.flush()   # ensure PKs before books
        seed_books(session)
    print("✅ Database seeded successfully!")

if __name__ == "__main__":
    main()