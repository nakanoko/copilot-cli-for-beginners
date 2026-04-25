def print_menu():
    print("\n📚 Book Collection App")
    print("1. Add a book")
    print("2. List books")
    print("3. Mark book as read")
    print("4. Remove a book")
    print("5. Exit")


def get_user_choice() -> str:
    """Prompt until the user provides a valid choice between 1 and 5 (inclusive).

    Returns the validated choice as a string ("1"-"5").
    """
    while True:
        choice = input("Choose an option (1-5): ").strip()
        if not choice:
            print("Please enter a choice (1-5).")
            continue
        if not choice.isdigit():
            print("Invalid input. Please enter a number between 1 and 5.")
            continue
        num = int(choice)
        if 1 <= num <= 5:
            return str(num)
        print("Choice out of range. Please enter a number between 1 and 5.")


def get_book_details():
    """Prompt the user for book details and return a validated tuple.

    Prompts:
    - Title: required. The function will re-prompt until a non-empty title is provided.
    - Author: optional (empty string allowed).
    - Publication year: optional; parsed to int. If parsing fails, defaults to 0.

    Returns:
        tuple[str, str, int]: (title, author, year)

    Notes:
    - Title is stripped of leading/trailing whitespace and must not be empty.
    - Author is stripped and may be empty if the user does not provide one.
    - Year is converted to an integer when possible; on ValueError the function
      prints a message and returns 0 for the year.
    """
    while True:
        title = input("Enter book title: ").strip()
        if title:
            break
        print("Title cannot be empty. Please enter a title.")

    author = input("Enter author: ").strip()

    year_input = input("Enter publication year: ").strip()
    try:
        year = int(year_input)
    except ValueError:
        print("Invalid year. Defaulting to 0.")
        year = 0

    return title, author, year


def print_books(books):
    """Print a formatted list of books to the console.

    Parameters:
        books (Iterable): An iterable of book-like objects. Each object is
            expected to have the attributes: title (str), author (str), year (int),
            and read (bool).

    Behavior:
    - If `books` is empty, prints a message informing the user and returns.
    - Otherwise, prints a numbered list where each line shows the title, author,
      publication year, and a human-friendly read/unread status.

    Example output:
        1. The Hobbit by J.R.R. Tolkien (1937) - ✅ Read
    """
    if not books:
        print("No books in your collection.")
        return

    print("\nYour Books:")
    for index, book in enumerate(books, start=1):
        status = "✅ Read" if getattr(book, "read", False) else "📖 Unread"
        title = getattr(book, "title", "<untitled>")
        author = getattr(book, "author", "<unknown>")
        year = getattr(book, "year", "?")
        print(f"{index}. {title} by {author} ({year}) - {status}")


def get_title_input(prompt: str = "Title: ") -> str:
    """Prompt the user for a book title and return the stripped value."""
    return input(prompt).strip()


def get_author_input(prompt: str = "Author: ") -> str:
    """Prompt the user for an author name and return the stripped value."""
    return input(prompt).strip()
