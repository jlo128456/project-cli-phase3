import click
from commands.create_tables import create_tables
from commands.list_books import list_books
from commands.add_book import add_book
from commands.delete_book import delete_book

@click.group()
def library():
    """Manage your personal book library."""
    pass

# Register commands
library.add_command(create_tables)
library.add_command(list_books)
library.add_command(add_book)
library.add_command(delete_book)

if __name__ == "__main__":
    library()
