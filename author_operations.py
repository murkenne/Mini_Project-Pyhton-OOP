# author_operations.py

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def display_info(self):
        """Return a formatted string with author details."""
        return f"Name: {self.name}\nBiography: {self.biography}\n"


# List to store author objects
authors = []


# Function to add a new author
def add_author():
    try:
        name = input("Enter author name: ")
        biography = input("Enter a brief history of the author: ")
        new_author = Author(name, biography)
        authors.append(new_author)
        print(f"Author '{name}' added to the list.")
    except Exception as e:
        print(f"Something went wrong: {e}")


# Function to view a specific author's details
def view_author_info():
    try:
        name = input("Enter the author's name you want to view: ")
        for author in authors:
            if author.name.lower() == name.lower():
                print(f"\nAuthor details:\n{author.display_info()}")
                return
        print(f"No author named '{name}' found.")
    except Exception as e:
        print(f"Something went wrong: {e}")


# Function to display all authors in the list
def display_all():
    try:
        if not authors:
            print("No authors available.")
        else:
            print("\nList of all authors:")
            for index, author in enumerate(authors, start=1):
                print(f"\nAuthor {index}:\n{author.display_info()}")
    except Exception as e:
        print(f"Something went wrong: {e}")


# Function to handle author operations menu
def author_operations_menu():
    while True:
        action = input(
            "\nEnter an action: \n1. Add a new author \n2. View author details \n3. Display all authors \n4. Back to Main Menu: "
        ).strip().lower()

        if action == "4" or action == "back":
            print("Returning to the Main Menu.")
            break
        elif action == "1" or action == "add":
            add_author()
        elif action == "2" or action == "view":
            view_author_info()
        elif action == "3" or action == "display":
            display_all()
        else:
            print("Invalid action. Please try again.")


# Ensure this script only runs the menu when executed directly, not on import
if __name__ == "__main__":
    author_operations_menu()
