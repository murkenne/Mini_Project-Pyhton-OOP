# Import the necessary module for database connection
from connect_mysql import connect_database  # Import the connection function from your module
import mysql.connector
from mysql.connector import Error

# Define the User class
class User:
    def __init__(self, name, library_id, borrowed_books=None):
        """Initialize a new user with private attributes."""
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = borrowed_books if borrowed_books is not None else []

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name (if needed)
    def set_name(self, name):
        self.__name = name

    # Getter for library ID
    def get_library_id(self):
        return self.__library_id

    # Setter for library ID (if needed)
    def set_library_id(self, library_id):
        self.__library_id = library_id

    # Method to borrow a book
    def borrow_book(self, book_title):
        if book_title not in self.__borrowed_books:
            self.__borrowed_books.append(book_title)
            print(f"'{book_title}' has been borrowed by {self.__name}.")
        else:
            print(f"'{book_title}' is already borrowed by {self.__name}.")

    # Method to return a book
    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)
            print(f"'{book_title}' has been returned by {self.__name}.")
        else:
            print(f"'{book_title}' was not borrowed by {self.__name}.")

    # Method to get list of borrowed books
    def get_borrowed_books(self):
        return self.__borrowed_books

    # Display user details
    def display_user_info(self):
        borrowed_books_list = ', '.join(self.__borrowed_books) if self.__borrowed_books else "No books borrowed."
        return f"Name: {self.__name}\nLibrary ID: {self.__library_id}\nBorrowed Books: {borrowed_books_list}"


# Function to add a new user to the database
def add_user():
    connection = connect_database()
    if not connection:
        print("Failed to connect to the database.")
        return

    try:
        name = input("Enter the user's name: ")
        library_id = input("Enter the user's library ID: ")

        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO users (name, library_id) VALUES (%s, %s)", (name, library_id)
        )
        connection.commit()
        print(f"User '{name}' added to the database.")
    except Error as e:
        print(f"Failed to add user: {e}")
    finally:
        cursor.close()
        connection.close()


# Function to view a specific user's details from the database
def view_user_details():
    connection = connect_database()
    if not connection:
        print("Failed to connect to the database.")
        return

    try:
        library_id = input("Enter the library ID of the user you want to view: ")
        cursor = connection.cursor()
        cursor.execute("SELECT name, library_id FROM users WHERE library_id = %s", (library_id,))
        user = cursor.fetchone()

        if user:
            name, library_id = user
            print(f"\nUser Details:\nName: {name}\nLibrary ID: {library_id}\n")
        else:
            print(f"No user with library ID '{library_id}' found.")
    except Error as e:
        print(f"Failed to retrieve user details: {e}")
    finally:
        cursor.close()
        connection.close()


# Function to display all users in the database
def display_all_users():
    connection = connect_database()
    if not connection:
        print("Failed to connect to the database.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT name, library_id FROM users")
        users = cursor.fetchall()

        if not users:
            print("No users available in the system.")
        else:
            print("\nList of all users:")
            for index, user in enumerate(users, start=1):
                name, library_id = user
                print(f"\nUser {index}:\nName: {name}\nLibrary ID: {library_id}")
    except Error as e:
        print(f"Failed to display users: {e}")
    finally:
        cursor.close()
        connection.close()


# Main program loop for user operations
def user_operations_menu():
    while True:
        action = input(
            "\nUser Operations:\n1. Add a new user\n2. View user details\n3. Display all users\n4. Back to Main Menu\nEnter your choice: "
        ).strip().lower()

        if action == "4" or action == "back":
            print("Returning to the Main Menu.")
            break
        elif action == "1":
            add_user()
        elif action == "2":
            view_user_details()
        elif action == "3":
            display_all_users()
        else:
            print("Invalid action. Please try again.")

# Example of how you can call the user_operations_menu function in your main program
if __name__ == "__main__":
    user_operations_menu()
