# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3


class ChinookCon:
    def __init__(self):
        self.database_name = 'Chinook_Sqlite.sqlite'
        self.conn = None


    def __enter__(self):
        self.conn = sqlite3.connect(self.database_name)
        return self


    def insert(self):
        cursor = self.conn.cursor()
        sql_statement = "insert into Artist values (Null, 'A Aagrh!')"
        try:
            cursor.execute(sql_statement)
         #   return cursor.fetchall()
        except sqlite3.DatabaseError as err:
            print("Error: ", err)
        else:
            self.conn.commit()

    def __exit__(self):
        self.conn.close()


def method_name():

    # Создаем соединение с нашей базой данных
    # В нашем примере у нас это просто файл базы
    try:
        conn = sqlite3.connect('Chinook_Sqlite.sqlite')

        # Создаем курсор - это специальный объект который делает запросы и получает их результаты
        cursor = conn.cursor()
        sql_statement = "SELECT Name FROM Artistic ORDER BY Name LIMIT 3"
        try:
            cursor.execute(sql_statement)
            result = cursor.fetchall()
        except sqlite3.DatabaseError as err:
            print("Error: ", err)
        else:
            conn.commit()

    finally:
        conn.close()


if __name__ == '__main__':
    with ChinookCon() as ch_db:
        ch_db.insert()
