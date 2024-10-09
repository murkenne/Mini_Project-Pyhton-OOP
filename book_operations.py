# Import the necessary module for database connection
from connect_mysql import connect_database  # Import the connection function from your module
import mysql.connector
from mysql.connector import Error

# Define the Book class
class Book:
    def __init__(self, title, author, genre, isbn, publication_date, availability_status=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.publication_date = publication_date
        self.availability_status = availability_status

    def check_out(self):
        self.availability_status = False

    def return_book(self):
        self.availability_status = True

    def is_available(self):
        return self.availability_status

    def display_info(self):
        availability = "Available" if self.availability_status else "Checked out"
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, ISBN: {self.isbn}, Published: {self.publication_date}, Status: {availability}"


# Function to add a new book to the database
def add_book():
    connection = connect_database()
    if not connection:
        print("Failed to connect to the database.")
        return

    try:
        title = input("Enter book title: ")
        author = input("Enter the book author: ")
        genre = input("Enter the book genre: ")
        isbn = input("Enter the book ISBN (13 characters): ")
        publication_date = input("Enter the book publication date (YYYY-MM-DD): ")

        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO books (title, author_id, isbn, genre, publication_date, availability) VALUES (%s, %s, %s, %s, %s, %s)",
            (title, author, isbn, genre, publication_date, True)
        )
        connection.commit()
        print(f"Book '{title}' with ISBN '{isbn}' added to the database!")
    except Error as e:
        print(f"An error occurred while adding the book: {e}")
    finally:
        cursor.close()
        connection.close()


# Function to borrow a book from the database
def borrow_book():
    connection = connect_database()
    if not connection:
        print("Failed to connect to the database.")
        return

    try:
        title = input("Enter the title of the book you want to borrow: ")

        cursor = connection.cursor()
        cursor.execute("SELECT id, availability FROM books WHERE title = %s", (title,))
        book = cursor.fetchone()

        if book:
            book_id, availability = book
            if availability:
                # Update the book's availability status to False (Checked out)
                cursor.execute("UPDATE books SET availability = 0 WHERE id = %s", (book_id,))
                connection.commit()
                print(f"You have successfully borrowed '{title}'.")
            else:
                print(f"Sorry, '{title}' is currently checked out.")
        else:
            print(f"Book titled '{title}' not found in the library.")
    except Error as e:
        print(f"An error occurred while borrowing the book: {e}")
    finally:
        cursor.close()
        connection.close()


# Function to return a borrowed book to the database
def return_book():
    connection = connect_database()
    if not connection:
        print("Failed to connect to the database.")
        return

    try:
        title = input("Enter the title of the book you want to return: ")

        cursor = connection.cursor()
        cursor.execute("SELECT id, availability FROM books WHERE title = %s", (title,))
        book = cursor.fetchone()

        if book:
            book_id, availability = book
            if not availability:
                # Update the book's availability status to True (Available)
                cursor.execute("UPDATE books SET availability = 1 WHERE id = %s", (book_id,))
                connection.commit()
                print(f"You have successfully returned '{title}'.")
            else:
                print(f"'{title}' is already available in the library.")
        else:
            print(f"Book titled '{title}' not found in the library.")
    except Error as e:
        print(f"An error occurred while returning the book: {e}")
    finally:
        cursor.close()
        connection.close()


# Function to search for a book in the database
def search_book():
    connection = connect_database()
    if not connection:
        print("Failed to connect to the database.")
        return

    try:
        title = input("Enter the title of the book you want to search for: ")

        cursor = connection.cursor()
        cursor.execute("SELECT title, author_id, genre, isbn, publication_date, availability FROM books WHERE title = %s", (title,))
        book = cursor.fetchone()

        if book:
            title, author_id, genre, isbn, publication_date, availability = book
            status = "Available" if availability else "Checked out"
            print(f"Book found:\nTitle: {title}\nAuthor ID: {author_id}\nGenre: {genre}\nISBN: {isbn}\nPublication Date: {publication_date}\nStatus: {status}")
        else:
            print(f"Book titled '{title}' not found in the library.")
    except Error as e:
        print(f"An error occurred while searching for the book: {e}")
    finally:
        cursor.close()
        connection.close()


# Function to display all books in the database
def display_all_books():
    connection = connect_database()
    if not connection:
        print("Failed to connect to the database.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT title, author_id, genre, isbn, publication_date, availability FROM books")
        books = cursor.fetchall()

        if not books:
            print("No books available in the library.")
            return

        print("\nBooks available in the library:")
        for book in books:
            title, author_id, genre, isbn, publication_date, availability = book
            status = "Available" if availability else "Checked out"
            print(f"Title: {title}, Author ID: {author_id}, Genre: {genre}, ISBN: {isbn}, Published: {publication_date}, Status: {status}")
    except Error as e:
        print(f"An error occurred while displaying books: {e}")
    finally:
        cursor.close()
        connection.close()


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


# Ensure this script only runs the menu when executed directly, not on import
if __name__ == "__main__":
    book_operations_menu()
