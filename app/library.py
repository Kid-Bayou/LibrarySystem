import random
from observer import Observer, Subject

class Library(Subject):
    def __init__(self):
        super().__init__()
        self._books = []

    def add_book(self, book_title):
        self._books.append(book_title)
        print(f"Book '{book_title}' added to the library.")
        self.notify(book_title)

    def get_books(self):
        return self._books

class User(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, book_title):
        if random.randint(1, 3) == 1:
            print(f"Notification for {self.name}: A new book '{book_title}' is available!")
