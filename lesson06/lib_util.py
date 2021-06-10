from lesson06.library_classes import Author, Book


class GetData:
    def get_book(self):
        pass
    def get_author(self):
        pass

class GetDataFromConsole(GetData):

    def get_book(self):
        return self.get_book_from_console()

    def get_author(self):
        return self.get_author_from_console()

    def get_author_from_console(self):
        author_id = input("Enter book author id")
        author_name = input("Enter book author name")
        return Author(author_id, author_name)

    def get_book_from_console(self):
        book_id = input("Enter book id")
        book_name = input("Enter book name")
        book_year = input("Enter book year")
        return Book(book_id,book_name,self.get_author_from_console(),book_year)