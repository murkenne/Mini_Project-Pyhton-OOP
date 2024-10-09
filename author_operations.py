from connect_mysql import connect_database

# Author class
class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def display_info(self):
        """Return a formatted string with author details."""
        return f"Name: {self.name}\nBiography: {self.biography}\n"



# Function to add a new author to the database
def add_author():
    connection = connect_database()
    if not connection:
        print("Failed to connect to the database.")
        return

    try:
        name = input("Enter author name: ")
        biography = input("Enter a brief history of the author: ")

        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO authors (name, biography) VALUES (%s, %s)", (name, biography)
        )
        connection.commit()
        print(f"Author '{name}' added to the database.")
    except Error as e:
        print(f"Failed to add author: {e}")
    finally:
        cursor.close()
        connection.close()


# Function to view a specific author's details from the database
def view_author_info():
    connection = connect_database()
    if not connection:
        print("Failed to connect to the database.")
        return

    try:
        name = input("Enter the author's name you want to view: ")
        cursor = connection.cursor()
        cursor.execute("SELECT name, biography FROM authors WHERE name = %s", (name,))
        author = cursor.fetchone()

        if author:
            print(f"\nAuthor details:\nName: {author[0]}\nBiography: {author[1]}\n")
        else:
            print(f"No author named '{name}' found.")
    except Error as e:
        print(f"Failed to retrieve author details: {e}")
    finally:
        cursor.close()
        connection.close()


# Function to display all authors from the database
def display_all():
    connection = connect_database()
    if not connection:
        print("Failed to connect to the database.")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT name, biography FROM authors")
        authors = cursor.fetchall()

        if not authors:
            print("No authors available in the database.")
        else:
            print("\nList of all authors:")
            for index, author in enumerate(authors, start=1):
                print(f"\nAuthor {index}:\nName: {author[0]}\nBiography: {author[1]}\n")
    except Error as e:
        print(f"Failed to display authors: {e}")
    finally:
        cursor.close()
        connection.close()


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
