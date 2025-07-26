import click
from lib.db.models import Book
from lib.db.session import get_db_session

def list_books():
    with get_db_session() as session:
        books = session.query(Book).all()
        if not books:
            click.echo("No books found")
        else:
            click.echo("\nYour library:")
            for b in books:
                genres = ", ".join(g.name for g in b.genres) or "No genres"
                click.echo(f"- [{b.id}] {b.title} by {b.author.name} ({b.published_date}) – {genres}")
    
    click.prompt("\nPress Enter to return to the Book Menu", prompt_suffix='', default='', show_default=False)
