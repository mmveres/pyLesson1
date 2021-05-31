class Book:
    def __init__(self, udc, fio, name, year, number):
        self.udc = udc
        self.fio = fio
        self.name = name
        self.year = year
        self.number = number

    def __hash__(self):
        return self.udc + self.number





    def __str__(self):
        return f"{self.udc}, {self.fio}, {self.name}, {self.year}, {self.number}"
