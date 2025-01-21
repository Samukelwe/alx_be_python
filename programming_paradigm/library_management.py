class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_book_out(self):
        if self._is_checked_out == False:
            self._is_checked_out = True

    def return_book(self):
        if self._is_checked_out == True:
            self._is_checked_out = False

    def is_available(self):
        return self._is_checked_out == False


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if title == book.title:
                book.check_book_out()

    def return_book(self, title):
        for book in self._books:
            if title == book.title:
                book.return_book()

    def list_available_books(self):
        for book in self._books:
            if book.is_available() == True:
                print(f"{book.title} by {book.author}")