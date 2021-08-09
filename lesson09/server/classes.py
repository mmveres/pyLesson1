class Student:
    def __init__(self, name, age):
        self.age = age
        self.name = name
    def __repr__(self):
        return f"{self.name}, {self.age}"