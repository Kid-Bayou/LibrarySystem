import schedule
import time
from library import Library, User

def check_for_new_books(library):
    book_titles = ["The Great Gatsby", "1984", "To Kill a Mockingbird", "Moby Dick"]
    if len(library.get_books()) < len(book_titles):
        book_title = book_titles[len(library.get_books())]
        library.add_book(book_title)

def main():
    library = Library()
    user1 = User("Alice")
    user2 = User("Bob")

    library.attach(user1)
    library.attach(user2)

    schedule.every(10).seconds.do(check_for_new_books, library)

    print("Library system started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
