import click
from lib.db.models import Book
from lib.db.session import get_db_session

def delete_book():
    book_id = click.prompt("Enter the book ID to delete", type=int)

    with get_db_session() as session:
        book = session.get(Book, book_id)
        if not book:
            click.echo(f"No book found with ID {book_id}.")
        else:
            if click.confirm(f"Are you sure you want to delete '{book.title}' (ID #{book_id})?"):
                session.delete(book)
                click.echo(f"Deleted book #{book_id}: {book.title}")
            else:
                click.echo("Deletion cancelled.")

    click.prompt("\nPress Enter to return to the Book Menu", prompt_suffix='', default='', show_default=False)
