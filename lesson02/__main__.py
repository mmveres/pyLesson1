def get_list_by_cycle():
    arr = []
    for i in range(10):
        arr.append(i ** 2)
    print(arr)

class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __repr__(self):
        return f"{self.name}, {self.speed}"

def square(x):
    return x**2

def to_lower(ch):
    return ch.lower()

if __name__ == '__main__':
    arr = [10,2,30,4,5]
    arr.sort(reverse=True)
    print(arr)
    chars = ['a','b','A','c','B']
    chars_sorted = sorted(chars, key= to_lower)
    chars.sort(key= lambda ch : ch.lower())
    chars.sort(key= to_lower)
    chars.sort(key= str.lower)


    print(chars)

    cars = [Car('Ford', 100), Car('BMW',120), Car('Audi',110)]
    cars.sort(key=lambda car: car.speed, reverse=True )
    print(cars)

    arrSquare = map(lambda x: x**2, arr)
    arrSquare = map(square, arr)
    print(list(arrSquare))



