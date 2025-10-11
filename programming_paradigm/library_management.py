"""Implement a Library class with a private list _books to store instances of Book. Include methods to add_book, check_out_book(title), return_book(title), and list_available_books"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
class Library:
    def __init__(self):
        self._books = []
    def add_book(self,Book):
        self._books.append(Book)
    def check_out_book(self,title):
        for book_title in self._books:
            if book_title.title == title:
                book_title._is_checked_out = True
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = False
    def list_available_books(self):
        for book in self._books:
            print(f"{book.title} by {book.author}")
