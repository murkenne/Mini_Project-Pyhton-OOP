# Importing necessary modules for Book, User, and Author operations
from book_operations import book_operations_menu
from user_operations import user_operations_menu
from author_operations import author_operations_menu

# Main program loop for the Library Management System
def main():
    while True:
        print("\nWelcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")

        # Get user action
        action = input("Enter your choice (1, 2, 3, or 4): ").strip().lower()

        if action == "1":
            book_operations_menu()
        elif action == "2":
            user_operations_menu()
        elif action == "3":
            author_operations_menu()
        elif action == "4" or action == "quit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")


# Run the main program
if __name__ == "__main__":
    main()
