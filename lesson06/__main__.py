# Описать класс «домашняя библиотека».
# Предусмотреть возможность работы с произвольным числом книг,
# поиска книги по какому-либо признаку (например, по автору или по году издания),
# добавления книг в библиотеку,
# удаления книг из нее,
# сортировки книг по разным полям.
from lesson06.lib_util import GetDataFromConsole
from lesson06.library_classes import Library, Author, Book



def create_menu(library, data):


    menu_dict = dict()
    menu_dict[1]= lambda : library.add_book(data.get_book(),1);
    menu_dict[2]= lambda : library.delete_book(data.get_book());
    menu_dict[3]= lambda : print(library.get_search_books_by_author(data.get_author()));
    menu_dict[4]= lambda : print(library.get_search_books_by_name(data.get_book().name));
    menu_dict[5]= lambda : print(library.get_search_books_by_year(data.get_book().year));
    menu_dict[6]= lambda : print(library.sort_books_by_author(data.get_author()));
    menu_dict[7]= lambda : print(library.sort_books_by_name(data.get_book().name));
    menu_dict[8]= lambda : print(library.sort_books_by_year(data.get_book().year));
    return menu_dict




if __name__ == '__main__':
   # library = Library()
    menu = create_menu(Library(),GetDataFromConsole)
    while True:
        print("1.добавления книг в библиотеку")
        print("2.удаления книг из библиотеки")
        print("3.поиск книг по автору")
        print("4.поиск книг по названию")
        print("5.поиск книг по году")
        print("6.сортировка книг по автору")
        print("7.сортировка книг по названию")
        print("8.сортировка книг по году")
        print("0.выход")
        choice = int(input("введите вариант"))
        if choice == 0:
            break;
        else:
            menu[choice]()

