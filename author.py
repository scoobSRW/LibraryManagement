class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def display_details(self):
        print(f"Name: {self.__name}\nBiography: {self.__biography}")

    def get_name(self):
        return self.__name
