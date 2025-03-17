
import json
import os
from colorama import init, Fore

# Initialize colorama (for Windows support)
init(autoreset=True)

# Colors
CYAN = Fore.CYAN
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RED = Fore.RED
BLUE = Fore.BLUE

# File name for saving and loading books
FILE_NAME = "library.txt"

# Load existing books from file
def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save books to file
def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)

# Add a book
def add_book(books):
    print(f"{CYAN}\n📖 Add a Book")
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = input("Enter the publication year: ")
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    book = {
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read": read_status
    }
    books.append(book)
    save_books(books)
    print(f"{GREEN}✅ Book added successfully!")

# Remove a book
def remove_book(books):
    print(f"{RED}\n🗑 Remove a Book")
    title = input("Enter the title of the book to remove: ")
    updated_books = [book for book in books if book["title"].lower() != title.lower()]

    if len(updated_books) == len(books):
        print(f"{RED}❌ Book not found!")
    else:
        save_books(updated_books)
        print(f"{GREEN}✅ Book removed successfully!")
    
    return updated_books

# Search for a book
def search_book(books):
    print(f"{YELLOW}\n🔎 Search for a Book")
    choice = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
    query = input("Enter the search term: ").strip().lower()

    results = []
    for book in books:
        if (choice == "1" and query in book["title"].lower()) or (choice == "2" and query in book["author"].lower()):
            results.append(book)

    if results:
        print(f"{BLUE}\n🔎 Matching Books:")
        for i, book in enumerate(results, 1):
            status = f"{GREEN}Read" if book["read"] else f"{RED}Unread"
            print(f"{i}. {CYAN}{book['title']}{Fore.RESET} by {YELLOW}{book['author']}{Fore.RESET} ({book['year']}) - {book['genre']} - {status}")
    else:
        print(f"{RED}❌ No matching books found.")

# Display all books
def display_books(books):
    print(f"{CYAN}\n📚 Your Library:")
    if not books:
        print(f"{RED}📂 Your library is empty!")
        return

    for i, book in enumerate(books, 1):
        status = f"{GREEN}Read" if book["read"] else f"{RED}Unread"
        print(f"{i}. {CYAN}{book['title']}{Fore.RESET} by {YELLOW}{book['author']}{Fore.RESET} ({book['year']}) - {book['genre']} - {status}")

# Display statistics
def display_statistics(books):
    print(f"{BLUE}\n📊 Library Statistics:")
    total_books = len(books)
    read_books = sum(1 for book in books if book["read"])

    if total_books == 0:
        print(f"{RED}📊 No books in library!")
    else:
        percentage_read = (read_books / total_books) * 100
        print(f"📚 Total books: {YELLOW}{total_books}{Fore.RESET}")
        print(f"✅ Books Read: {GREEN}{read_books}{Fore.RESET}")
        print(f"📖 Percentage Read: {CYAN}{percentage_read:.2f}%{Fore.RESET}")

# Main menu loop
def main():
    books = load_books()

    while True:
        print(f"\n{CYAN}📚 Welcome to Personal Library Manager")
        print(f"{YELLOW}1. Add a book")
        print(f"{RED}2. Remove a book")
        print(f"{BLUE}3. Search for a book")
        print(f"{CYAN}4. Display all books")
        print(f"{GREEN}5. Display statistics")
        print(f"{RED}6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            books = remove_book(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            display_books(books)
        elif choice == "5":
            display_statistics(books)
        elif choice == "6":
            save_books(books)
            print(f"{GREEN}📂 Library saved to file. Goodbye!")
            break
        else:
            print(f"{RED}❌ Invalid choice, please try again.")

# Run the program
if __name__ == "__main__":
    main()
