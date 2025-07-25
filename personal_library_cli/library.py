from commands.create_tables import create_tables
from commands.list_books import list_books
from commands.add_book import add_book
from commands.delete_book import delete_book
from lib.db.session import get_db_session
from lib.db.models import Book

def confirm_delete(book_id):
    with get_db_session() as session:
        book = session.query(Book).get(book_id)
        if not book:
            print("Book not found.")
            return
        confirm = input(f"Are you sure you want to delete '{book.title}'? (y/N): ").strip().lower()
        if confirm == "y":
            delete_book(book_id)
        else:
            print("Cancelled.")

def search_books():
    keyword = input("Enter part of the title to search: ").strip().lower()
    with get_db_session() as session:
        results = session.query(Book).filter(Book.title.ilike(f"%{keyword}%")).all()
        if results:
            print("\nSearch Results:")
            print("{:<4} {:<30} {:<12} {:<20}".format("ID", "Title", "Published", "Author"))
            print("-" * 70)
            for b in results:
                print("{:<4} {:<30} {:<12} {:<20}".format(b.id, b.title, str(b.published_date), b.author.name))
        else:
            print("No books found.")

def book_menu():
    while True:
        print("\nBook Menu")
        print("1. List Books\n2. Add Book\n3. Delete Book\n4. Search Book\n5. Return to Main Menu")
        choice = input("Select an option (1–5): ").strip()
        if choice == "1":
            list_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            confirm_delete(input("Enter the book ID to delete: ").strip())
        elif choice == "4":
            search_books()
        elif choice == "5":
            break
        else:
            print("Invalid selection. Please try again.")

def db_menu():
    while True:
        print("\nDatabase Menu")
        print("1. Create or Reset Tables\n2. Return to Main Menu")
        choice = input("Select an option (1–2): ").strip()
        if choice == "1":
            create_tables()
        elif choice == "2":
            break
        else:
            print("Invalid selection. Please try again.")

def main_menu():
    while True:
        print("\n==== Personal Library CLI ====")
        print("1. Book Management\n2. Database Management\n3. Exit")
        choice = input("Select an option (1–3): ").strip()
        if choice == "1":
            book_menu()
        elif choice == "2":
            db_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main_menu()
