from book import Book
from user import User
from author import Author

books = []
users = []
authors = []

def main_menu():
    while True:
        print("\nMain Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit")
        choice = input("Choose an option: ")
        if choice == '1':
            book_operations_menu()
        elif choice == '2':
            user_operations_menu()
        elif choice == '3':
            author_operations_menu()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def book_operations_menu():
    while True:
        print("\nBook Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books\n6. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == '1':
            add_new_book()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            search_book()
        elif choice == '5':
            display_all_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

def user_operations_menu():
    while True:
        print("\nUser Operations:\n1. Add a new user\n2. View user details\n3. Display all users\n4. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == '1':
            add_new_user()
        elif choice == '2':
            view_user_details()
        elif choice == '3':
            display_all_users()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

def author_operations_menu():
    while True:
        print("\nAuthor Operations:\n1. Add a new author\n2. View author details\n3. Display all authors\n4. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == '1':
            add_new_author()
        elif choice == '2':
            view_author_details()
        elif choice == '3':
            display_all_authors()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

def add_new_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    genre = input("Enter the genre: ")
    publication_date = input("Enter the publication date: ")
    book = Book(title, author, genre, publication_date)
    books.append(book)
    print(f"Book '{title}' added successfully!")

def borrow_book():
    title = input("Enter the book title to borrow: ")
    for book in books:
        if book.get_title() == title:
            if book.is_available():
                book.borrow()
                return
            else:
                print(f"'{title}' is already borrowed.")
                return
    print(f"Book '{title}' not found.")

def return_book():
    title = input("Enter the book title to return: ")
    for book in books:
        if book.get_title() == title:
            if not book.is_available():
                book.return_book()
                return
            else:
                print(f"'{title}' is already available.")
                return
    print(f"Book '{title}' not found.")

def search_book():
    title = input("Enter the book title to search for: ")
    for book in books:
        if book.get_title() == title:
            book.display_details()
            return
    print(f"Book '{title}' not found.")

def display_all_books():
    if books:
        for book in books:
            book.display_details()
            print("-" * 20)
    else:
        print("No books available.")

def add_new_user():
    name = input("Enter the user's name: ")
    library_id = input("Enter the user's library ID: ")
    user = User(name, library_id)
    users.append(user)
    print(f"User '{name}' added successfully!")

def view_user_details():
    name = input("Enter the user's name to view details: ")
    for user in users:
        if user.get_name() == name:
            user.display_details()
            return
    print(f"User '{name}' not found.")

def display_all_users():
    if users:
        for user in users:
            user.display_details()
            print("-" * 20)
    else:
        print("No users available.")

def add_new_author():
    name = input("Enter the author's name: ")
    biography = input("Enter the author's biography: ")
    author = Author(name, biography)
    authors.append(author)
    print(f"Author '{name}' added successfully!")

def view_author_details():
    name = input("Enter the author's name to view details: ")
    for author in authors:
        if author.get_name() == name:
            author.display_details()
            return
    print(f"Author '{name}' not found.")

def display_all_authors():
    if authors:
        for author in authors:
            author.display_details()
            print("-" * 20)
    else:
        print("No authors available.")

if __name__ == "__main__":
    main_menu()
