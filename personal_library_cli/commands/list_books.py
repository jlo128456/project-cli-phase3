import click
from lib.db.models import Book
from lib.db.session import get_db_session

@click.command("list-books")
def list_books():
    """List all books in your library."""
    with get_db_session() as session:
        books = session.query(Book).all()
        if not books:
            click.echo("No books found")
            return

        click.echo("Your library:")
        for b in books:
            genres = ", ".join(g.name for g in b.genres) or "No genres"
            click.echo(f"- [{b.id}] {b.title} by {b.author.name} ({b.published_date}) – {genres}")
