import click
from lib.db.models import (
    engine,          # SQLAlchemy engine for database connection
    Base,            # Declarative base holding metadata for all models
    get_db_session,  # Context manager yielding a database session
    Book,            # ORM model for books
    Author,          # ORM model for authors
    Genre            # ORM model for genres
)

from lib.db.seed import run_seed

@click.group()
def library():
    """Manage your personal book library."""
    pass

@library.command("create-tables", help="Create tables, optionally resetting and seeding the DB.")
@click.option("--reset/--no-reset", default=True, help="Drop existing tables before creating new ones.")
@click.option("--seed", is_flag=True, help="Also populate the tables with sample data.")
def create_tables(reset, seed):
    if reset:
        click.echo("Dropping all existing tables...", fg="red")
        Base.metadata.drop_all(engine)
    else:
        click.echo("Skipping drop (keeping existing tables)...", fg="yellow")

    click.echo("Creating tables...", fg="green")
    Base.metadata.create_all(engine)

    if seed:
        click.echo("Seeding initial data...", fg="yellow")
        run_seed()
        click.echo("Database seeded successfully.", fg="cyan")
    else:
        click.echo("Tables created (no seed).", fg="cyan")


@library.command("list-books")
def list_books():
    """List all books in your library."""
    with get_db_session() as session:
        books = session.query(Book).all()      # fetch all Book records
        if not books:
            click.echo("No books found")
            return

        click.echo("Your library:")
        for b in books:
            # prepare comma-separated genre names
            genres = ", ".join(g.name for g in b.genres) or "No genres"
            click.echo(
                f"- [{b.id}] {b.title} by {b.author.name} "
                f"({b.published_date}) – {genres}"
            )

@library.command("add-book")
@click.option("--title", prompt="Title", help="The book's title")
@click.option("--author", prompt="Author", help="The author's name")
@click.option(
    "--date",
    prompt="Published Date (YYYY-MM-DD)",
    help="Publication date"
)
@click.option(
    "--genres",
    prompt="Genres (comma separated)",
    help="Comma-separated genres"
)
def add_book(title, author, date, genres):
    """Add a new book to the library."""
    with get_db_session() as session:
        # get or create the author
        auth = session.query(Author).filter_by(name=author).first()
        if not auth:
            auth = Author(name=author)
            session.add(auth)
            session.flush()                    # get auth.id assigned

        # get or create each genre
        genre_objs = []
        for name in (n.strip() for n in genres.split(",") if n.strip()):
            g = session.query(Genre).filter_by(name=name).first()
            if not g:
                g = Genre(name=name)
                session.add(g)
                session.flush()
            genre_objs.append(g)

        # create and persist the Book
        book = Book(
            title=title,
            published_date=date,
            author=auth,
            genres=genre_objs
        )
        session.add(book)
        click.echo(f"Added book #{book.id}: {book.title}")

@library.command("delete-book")
@click.argument("book_id", type=int)
def delete_book(book_id):
    """Delete a book from the library by its ID."""
    with get_db_session() as session:
        book = session.get(Book, book_id)      # look up by primary key
        if not book:
            click.echo(f"No book found with ID {book_id}.")
            return

        # ask for confirmation before deleting
        if click.confirm(f"Are you sure you want to delete '{book.title}' (ID #{book_id})?"):
            session.delete(book)
            click.echo(f"Deleted book #{book_id}: {book.title}")
        else:
            click.echo("Deletion cancelled.")

if __name__ == "__main__":
    library()  # invoke the CLI group