class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def add_borrowed_book(self, book_title):
        self.__borrowed_books.append(book_title)
        print(f"'{book_title}' has been added to {self.__name}'s borrowed books.")

    def return_borrowed_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)
            print(f"'{book_title}' has been returned by {self.__name}.")
        else:
            print(f"'{book_title}' is not borrowed by {self.__name}.")

    def display_details(self):
        print(f"Name: {self.__name}\nLibrary ID: {self.__library_id}\nBorrowed Books: {', '.join(self.__borrowed_books) if self.__borrowed_books else 'None'}")

    def get_name(self):
        return self.__name
