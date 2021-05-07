class Car:
    def __init__(self, name, speed, year):
        self.name = name
        self.speed = speed
        self.year = year

    def __str__(self):
        return f"STR {self.name}, {self.speed}, {self.year}"

    def __repr__(self):
        return f"REPR ({self.name}, {self.speed}, {self.year})"