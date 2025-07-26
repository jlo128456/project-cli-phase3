import click
from lib.db.models import Book
from lib.db.session import get_db_session

def search_books():
    keyword = click.prompt("Enter part of the title to search").strip().lower()
    with get_db_session() as session:
        results = session.query(Book).filter(Book.title.ilike(f"%{keyword}%")).all()
        if results:
            click.echo("\nSearch Results:")
            click.echo("{:<4} {:<30} {:<12} {:<20}".format("ID", "Title", "Published", "Author"))
            click.echo("-" * 70)
            for b in results:
                click.echo("{:<4} {:<30} {:<12} {:<20}".format(b.id, b.title, str(b.published_date), b.author.name))
        else:
            click.echo("No books found.")
    click.prompt("\nPress Enter to return to the Book Menu", prompt_suffix='', default='', show_default=False)
