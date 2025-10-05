class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books=[]
    def add_book(self, book):
        self._books.append(book)
        print(self._books)
    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                self._books.remove(book.title)
                return
        # if not found or already checked out
        print(f"Book '{title}' is not available for checkout.")
    def return_book(self,title):
        add_book(title)
    def list_available_books(self):
        for i in self._books:
            print(f"{self._books}")