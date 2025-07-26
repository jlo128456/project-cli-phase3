import click
from commands.create_tables import create_tables
from commands.list_books import list_books
from commands.add_book import add_book
from commands.delete_book import delete_book
from commands.search_books import search_books

def book_menu():
    while True:
        click.clear()
        click.echo("📚 Book Menu")
        click.echo("1. List Books")
        click.echo("2. Add Book")
        click.echo("3. Delete Book")
        click.echo("4. Search Book")
        click.echo("5. Return to Main Menu")

        choice = click.prompt("Select an option", type=str).strip()
        if choice == "1":
            list_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            search_books()
        elif choice == "5":
            break
        else:
            click.echo("Invalid selection. Try again.")
            click.prompt("Press Enter to continue", default="", show_default=False)

def db_menu():
    while True:
        click.clear()
        click.echo("🗃️  Database Menu")
        click.echo("1. Create or Reset Tables")
        click.echo("2. Return to Main Menu")

        choice = click.prompt("Select an option", type=str).strip()
        if choice == "1":
            create_tables()
        elif choice == "2":
            break
        else:
            click.echo("Invalid selection. Try again.")
            click.prompt("Press Enter to continue", default="", show_default=False)

def main_menu():
    while True:
        click.clear()
        click.echo("==== Personal Library CLI ====")
        click.echo("1. Book Management")
        click.echo("2. Database Management")
        click.echo("3. Exit")

        choice = click.prompt("Select an option", type=str).strip()
        if choice == "1":
            book_menu()
        elif choice == "2":
            db_menu()
        elif choice == "3":
            click.echo("Goodbye!")
            break
        else:
            click.echo("Invalid selection. Try again.")
            click.prompt("Press Enter to continue", default="", show_default=False)

if __name__ == "__main__":
    main_menu()
