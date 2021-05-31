from lesson04.book import Book
from lesson04.book_tree import BookTree

if __name__ == '__main__':
    books_tree = BookTree()
    books_tree.add(Book(13,1,2,3,4))
    books_tree.add(Book(10,1,2,3,4))
    books_tree.add(Book(7,1,2,3,4))
    books_tree.add(Book(20,1,2,3,4))
    books_tree.add(Book(25,1,2,3,4))
    books_tree.add(Book(15,1,2,3,4))
    books_tree.print()

    book_dict = {}
    book_dict[1] = 1
    book_dict[11] = 2

    print(book_dict)

    book_set = set()
    book_set.add(1)
    book_set.add(1)
    print(book_set)