class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __eq__(self, other_author) -> bool:
        return self.name == other_author.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __str__(self):
        return f"{self.id}, {self.name}"

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def del_book(self, book):
        self.books.remove(book)

    def __str__(self):
        return f"{self.id}, {self.name}"

class Book:
    def __init__(self, id, name, author, year):
        self.id = id
        self.name = name
        self.author = author
        self.year = year

    def __eq__(self, other_book) -> bool:
        return self.id == other_book.id and \
               self.name == other_book.name and \
               self.author == other_book.author and \
               self.year == other_book.year

    def __hash__(self) -> int:
        return hash(self.id,self.name,self.author,self.year)

    def __str__(self):
        return f"{self.id}, {self.name}, {self.author}, {self.year}"

    def __repr__(self) -> str:
        return self.__str__()


class Book_Account:
    def __init__(self, book, count, user=None):
        self.book = book
        self.count = count
        self.user = user

    def remove_book_to_user(self,user):
        if self.count>0:
            self.count=-1
            user.add_book(self.book)
        else:
            raise BookNotAvailableException()


class BookNotAvailableException(Exception):
    pass


class Library:
    def __init__(self):
        self.books_account = []
        self.users = []

    def add_book(self, book,count):
        for book_account in self.books_account:
            if book_account.book == book:
                book_account.count+=1
                return
        self.books_account.append(Book_Account(book,count))

    def delete_book(self, book, user):
        for book_account in self.books_account:
            if book_account.book == book:
                book_account.remove_book_to_user(user)

    def get_search_books_by_author(self, author):
        books_by_author = []
        for book_account in self.books_account:
            if book_account.book.author == author:
                books_by_author.append(book_account.book)
        return books_by_author

    def get_search_books_by_name(self, name):
        books_by_author = []
        for book_account in self.books_account:
            if book_account.book.name == name:
                books_by_author.append(book_account.book)
        return books_by_author

    def get_search_books_by_year(self, year):
        books_by_author = []
        for book_account in self.books_account:
            if book_account.book.year == year:
                books_by_author.append(book_account.book)
        return books_by_author


    def sort_books_by_author(self, author):
        self.books_account.sort(key = lambda a: a.book.author.name )
    def sort_books_by_name(self, name):
        self.books_account.sort(key = lambda a: a.book.name )
    def sort_books_by_year(self, year):
        self.books_account.sort(key = lambda a: a.book.year )

