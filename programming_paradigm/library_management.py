class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out_book(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.add(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if title == book.title:
                self.book.check_out_book()

    def return_book(self, title):
        for book in self._books:
            if title == book.title:
                self.book.return_book()

    def list_available_books():
        for book in books:
            print("{book.title} by {book.author}")
