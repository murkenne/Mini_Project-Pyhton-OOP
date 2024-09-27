
# Define Book class

class Book:
    def __init__(self, title, author, genre, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.availability_status = True # True means available, False means not available
        
    
    def check_out(self):
         # Mark the book as checked out (unavailable)
         self.availability_status = False
    
    def return_book(self): 
        # Mark the book as returned (available)
        self.availability_status = True 
        
    def is_available(self):
        # Check if the book is available
        return self.availability_status
    
    def display_info(self):
        # Display book details
        availability = "Available" if self.availability_status else "Checked out"
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Published: {self.publication_date}, Status: {availability}"
    
    # Create a list to store all books 
library = []
    
    # Define functions for book operations
def add_book():
    try:
        title = input("Enter book title: ")
        author = input("Enter the book author: ")
        genre = input("Enter the book genre: ")
        publication_date = ("Enter the book publication date: ")
        new_book = Book(title, author, genre, publication_date)
        library.append(new_book)
        print(f"Book {title} added to the library!")
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
            print(f"Book titled '{title}' found in the library.")
            

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
    """Search for a book in the library"""
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
    """Display all books in the library"""
    try:
        if not library:
            print("No books available in the library.")
            return
        print("\nBooks available in the library:")
        for book in library:
            print(book.display_info())
    except Exception as e:
        print(f"An error occurred while displaying books: {e}")
    

while True:
    action = input("Enter action (add, borrow, return, search, display, exit): ").lower()
    if action == "exit":
        print("Exiting the program. Goodbye!")
        break
    elif action == "add":
        add_book()
    elif action == "borrow":
        borrow_book()
    elif action == "return":
        return_book()
    elif action == "add":
        search_book()
    elif action == "display":
        display_all_books()
    else:
        print("Invalid action. Please try again.")