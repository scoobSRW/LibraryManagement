class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_available = True

    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            print(f"You have successfully borrowed '{self.__title}'.")
        else:
            print(f"The book '{self.__title}' is currently unavailable.")

    def return_book(self):
        self.__is_available = True
        print(f"The book '{self.__title}' has been returned.")

    def display_details(self):
        availability = "Available" if self.__is_available else "Borrowed"
        print(f"Title: {self.__title}\nAuthor: {self.__author}\nGenre: {self.__genre}\nPublication Date: {self.__publication_date}\nStatus: {availability}")

    def is_available(self):
        return self.__is_available

    def get_title(self):
        return self.__title