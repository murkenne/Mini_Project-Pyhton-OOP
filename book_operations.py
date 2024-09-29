# book_operations.py

# Define the Book class
class Book:
    def __init__(self, title, author, genre, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.availability_status = True  # True means available, False means not available

    def check_out(self):
        self.availability_status = False

    def return_book(self):
        self.availability_status = True

    def is_available(self):
        return self.availability_status

    def display_info(self):
        availability = "Available" if self.availability_status else "Checked out"
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Published: {self.publication_date}, Status: {availability}"


# List to store all books
library = []


# Functions for book operations
def add_book():
    try:
        title = input("Enter book title: ")
        author = input("Enter the book author: ")
        genre = input("Enter the book genre: ")
        publication_date = input("Enter the book publication date: ")
        new_book = Book(title, author, genre, publication_date)
        library.append(new_book)
        print(f"Book '{title}' added to the library!")
    except Exception as e:
        print(f"An error occurred while adding the book: {e}")


def borrow_book():
    title = input("Enter the title of the book you want to borrow: ")
    for book in library:
        if book.title.lower() == title.lower():
            if book.is_available():
                book.check_out()
                print(f"You have successfully borrowed '{book.title}'.")
            else:
                print(f"Sorry, '{book.title}' is currently checked out.")
            return
    print(f"Book titled '{title}' not found in the library.")


def return_book():
    try:
        title = input("Enter the title of the book you want to return: ")
        for book in library:
            if book.title.lower() == title.lower():
                if not book.is_available():
                    book.return_book()
                    print(f"You have successfully returned '{book.title}'.")
                else:
                    print(f"'{book.title}' is already available in the library.")
                return
        print(f"Book titled '{title}' not found in the library.")
    except Exception as e:
        print(f"An error occurred while returning the book: {e}")


def search_book():
    try:
        title = input("Enter the title of the book you want to search for: ")
        for book in library:
            if book.title.lower() == title.lower():
                print(f"Book found: {book.display_info()}")
                return
        print(f"Book titled '{title}' not found in the library.")
    except Exception as e:
        print(f"An error occurred while searching for the book: {e}")


def display_all_books():
    try:
        if not library:
            print("No books available in the library.")
            return
        print("\nBooks available in the library:")
        for book in library:
            print(book.display_info())
    except Exception as e:
        print(f"An error occurred while displaying books: {e}")


# Book operations menu function (with its own loop)
def book_operations_menu():
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to Main Menu")

        book_action = input("Enter your choice (1, 2, 3, 4, 5, or 6): ").strip().lower()

        if book_action == "1":
            add_book()
        elif book_action == "2":
            borrow_book()
        elif book_action == "3":
            return_book()
        elif book_action == "4":
            search_book()
        elif book_action == "5":
            display_all_books()
        elif book_action == "6" or book_action == "back":
            print("Returning to the Main Menu.")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    book_operations_menu()