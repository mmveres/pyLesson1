from lesson03.oop.car import Car
from lesson03.oop.list_car import ListCar

if __name__ == '__main__':
    car1 = Car("Ford", 100, 10)
    cars = [Car("Ford1", 130, 20),
            Car("Ford3", 120, 10),
            Car("Ford2", 100, 30)]
    car_list = ListCar(cars)
    car_list.append(Car("Ford4", 110, 15))
    print(car_list.aver())

    print(car_list)

    for car in car_list:
        print(car)
