import click
from lib.db.models import Book, Author, Genre
from lib.db.session import get_db_session

def add_book():
    try:
        title = click.prompt("Title", type=str)
        author_name = click.prompt("Author", type=str)
        published_date = click.prompt("Published Date (YYYY-MM-DD)", type=str)
        genre_input = click.prompt("Genres (comma-separated)", type=str)

        with get_db_session() as session:
            # Get or create author
            author = session.query(Author).filter_by(name=author_name).first()
            if not author:
                author = Author(name=author_name)
                session.add(author)
                session.flush()  # Get ID

            # Get or create genres
            genre_objs = []
            for name in (g.strip() for g in genre_input.split(",") if g.strip()):
                genre = session.query(Genre).filter_by(name=name).first()
                if not genre:
                    genre = Genre(name=name)
                    session.add(genre)
                    session.flush()
                genre_objs.append(genre)

            # Add book
            book = Book(title=title, published_date=published_date, author=author, genres=genre_objs)
            session.add(book)

            click.echo(f"\n Added Book #{book.id}: {book.title} by {author.name}")

    except Exception as e:
        click.echo(f"\n Error adding book: {e}")

    click.prompt("\nPress Enter to return to the Book Menu", prompt_suffix='', default='', show_default=False)
