import click
from lib.db.models import (
    engine, 
    Base,
    get_db_session,
    Book,
    Author,
    Genre
)

#entry point for cli group of related commands
@click.group()
def library():
    """Manage your personal book library"""
    pass

#command to create library table
@library.command("create-tables")
@click.option(
    "--reset/--no-reset",
    default=False,
    help="If set, drop all existing tables before creating them"
)
def create_tables(reset):
    """Create all tables from ORM models."""
    if reset:
        Base.metadata.drop_all(engine)
        click.echo("Dropped all existing tables")
    Base.metadata.create_all(engine)
    if reset:
        click.echo("Tables recreated from models.")
    else:
        click.echo("Tables created (if not present).") 

@library.command("list-books")
def list_books():
    """List all books in your library"""
    with get_db_session() as session:
        books = session.query(book).all()
        if not books:
            click.echo("No books found")
            return
        click.echo("Your library:")
        for b in books:
            genres = ",".join(g.name for g in b.genres) or "No genres"
            click.echo(f"-[{b.id}] {b.title} by {b.author.name} ({b.published_date}) - {genres} ")    
