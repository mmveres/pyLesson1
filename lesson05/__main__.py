class Person:
    def __init__(self, age, name, gps):
        self.age = age
        self.name = name
        self.gps = gps

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __hash__(self):
        print('The hash is:')
        return hash((self.age, self.name))



if __name__ == '__main__':
    person1 = Person(23, 'Adam', 11)
    print(hash(person1))
    person2 = Person(23, 'Adam', 12)
    print(hash(person2))
    print(person1==person2)