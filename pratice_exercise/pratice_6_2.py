class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author} has {self.pages} pages"
    def __repr__(self):
        return f"this rep repr"
    
book = Book("top 1","yinka","10000")
print(book)