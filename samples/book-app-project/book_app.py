import sys
from books import BookCollection
from utils import print_books, get_book_details, get_title_input, get_author_input


# Global collection instance
collection = BookCollection()


def handle_list():
    books = collection.list_books()
    print_books(books)


def handle_add():
    print("\nAdd a New Book\n")

    title, author, year = get_book_details()

    try:
        collection.add_book(title, author, year)
        print("\nBook added successfully.\n")
    except ValueError as e:
        print(f"\nError: {e}\n")


def handle_remove():
    print("\nRemove a Book\n")

    title = get_title_input("Enter the title of the book to remove: ")
    collection.remove_book(title)

    print("\nBook removed if it existed.\n")


def handle_find():
    print("\nFind Books by Author\n")

    author = get_author_input("Author name: ")
    books = collection.find_by_author(author)

    print_books(books)


def handle_mark_read():
    """Mark a book as read by title."""
    print("\nMark Book as Read\n")
    title = get_title_input("Enter the title of the book to mark as read: ")
    if collection.mark_as_read(title):
        print("\nBook marked as read.\n")
    else:
        print("\nBook not found.\n")


def show_help():
    print("""
Book Collection Helper

Commands:
  list       - Show all books
  add        - Add a new book
  remove     - Remove a book by title
  find       - Find books by author
  mark-read  - Mark a book as read
  help       - Show this help message
""")


def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1].lower()

    if command == "list":
        handle_list()
    elif command == "add":
        handle_add()
    elif command == "remove":
        handle_remove()
    elif command == "find":
        handle_find()
    elif command in ("mark-read", "mark"):
        handle_mark_read()
    elif command == "help":
        show_help()
    else:
        print("Unknown command.\n")
        show_help()


if __name__ == "__main__":
    main()
