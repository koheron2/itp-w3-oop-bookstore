#virtualenv = 'KAO_books'
class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        
    def get_books(self):
        return self.books
        
    def search_books(self, title=None, author=None):
        books_w_query = []
        if title == None:
            self.author = author
            for book in self.books:
                if self.author == book.author:
                    books_w_query.append(book)
        else:
            self.title = title.lower()
            for book in self.books:
                title = book.title
                lower_title = title.lower()
                try: 
                    lower_title.index(self.title)
                except ValueError:
                    pass
                else: 
                    books_w_query.append(book)
        return books_w_query
        
            
                    

class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
    
    def get_books(self):
        return self.books


class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.author.add_book(self)
        
    
