import datetime

from models import Base, engine, SessionLocal, Author, Genre, Book

# Create all tables
Base.metadata.create_all(bind=engine)

# Open a session
session = SessionLocal()

# --- Seed data ---
# Authors
authors = [
    Author(name="J. R. R. Tolkien"),
    Author(name="George Orwell"),
    Author(name="Harper Lee")
]

# Genres
genres = [
    Genre(name="Fantasy"),
    Genre(name="Dystopian"),
    Genre(name="Classic")
]

# Add authors and genres
session.add_all(authors + genres)
session.commit()

# Fetch saved authors/genres
tolkien = session.query(Author).filter_by(name="J. R. R. Tolkien").one()
orwell = session.query(Author).filter_by(name="George Orwell").one()
lee = session.query(Author).filter_by(name="Harper Lee").one()

fantasy = session.query(Genre).filter_by(name="Fantasy").one()
dystopian = session.query(Genre).filter_by(name="Dystopian").one()
classic = session.query(Genre).filter_by(name="Classic").one()

# Books with relationships
books = [
    Book(
        title="The Hobbit",
        published_date=datetime.date(1937, 9, 21),
        author=tolkien,
        genres=[fantasy, classic]
    ),
    Book(
        title="1984",
        published_date=datetime.date(1949, 6, 8),
        author=orwell,
        genres=[dystopian, classic]
    ),
    Book(
        title="To Kill a Mockingbird",
        published_date=datetime.date(1960, 7, 11),
        author=lee,
        genres=[classic]
    )
]

# Add books and commit
session.add_all(books)
session.commit()
session.close()

print("Database seeded successfully!")