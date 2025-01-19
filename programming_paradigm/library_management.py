class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_checked_out(self):
        return self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        return self._books

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                return f"Book '{title}' checked out."
        return f"Book '{title}' not available."

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                return f"Book '{title}' returned."
        return f"Book '{title}' not found."

    def list_available_books(self):
        available_books = [book.title for book in self._books if not book.is_checked_out()]
        return available_books
