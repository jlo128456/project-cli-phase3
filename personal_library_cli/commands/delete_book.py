import click
from lib.db.models import Book
from lib.db.session import get_db_session

@click.command("delete-book")
@click.argument("book_id", type=int)
def delete_book(book_id):
    """Delete a book from the library by its ID."""
    with get_db_session() as session:
        book = session.get(Book, book_id)
        if not book:
            click.echo(f"No book found with ID {book_id}.")
            return

        if click.confirm(f"Are you sure you want to delete '{book.title}' (ID #{book_id})?"):
            session.delete(book)
            click.echo(f"Deleted book #{book_id}: {book.title}")
        else:
            click.echo("Deletion cancelled.")
