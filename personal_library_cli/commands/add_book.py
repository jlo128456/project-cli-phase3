import click
from lib.db.models import Book, Author, Genre
from lib.db.session import get_db_session

def add_book():
    title = click.prompt("Title")
    author = click.prompt("Author")
    date = click.prompt("Published Date (YYYY-MM-DD)")
    genres = click.prompt("Genres (comma separated)")

    with get_db_session() as session:
        auth = session.query(Author).filter_by(name=author).first()
        if not auth:
            auth = Author(name=author)
            session.add(auth)
            session.flush()

        genre_objs = []
        for name in (n.strip() for n in genres.split(",") if n.strip()):
            g = session.query(Genre).filter_by(name=name).first()
            if not g:
                g = Genre(name=name)
                session.add(g)
                session.flush()
            genre_objs.append(g)

        book = Book(title=title, published_date=date, author=auth, genres=genre_objs)
        session.add(book)
        click.echo(f"Added book #{book.id}: {book.title}")
    
    click.prompt("\nPress Enter to return to the Book Menu", prompt_suffix='', default='', show_default=False)
