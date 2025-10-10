"""Exercise 1: Class Methods for Counting Instances Instruction:

Create a class Book with a class variable total_books to count the number of book instances created.
Implement a class method display_total_books() to display the total number of books created."""

class Book:
    total_books = 0
    def __init__(self,name):
        self.name = name
        Book.total_books += 1
        pass
    @classmethod
    def display_total_books(cls):
        return cls.total_books
book1 = Book("How to be poor")
book1 = Book("How to be rich")
print(f"{Book.display_total_books()}")
