class ListCar:
    class IterCarList:
        def __init__(self, iter_obj):
            self.iter_obj = iter_obj
            self.num = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.num == len(self.iter_obj):
                raise StopIteration
            num = self.num
            self.num += 1
            return self.iter_obj[num]


    def __init__(self, cars = list()):
        self.car_list = cars

    def append(self, car):
        self.car_list.append(car)

    def aver(self):
        return sum(car.speed for car in self.car_list)/len(self.car_list)

    def __str__(self):
       return f"{self.car_list.__str__()}"
       return f"{str(self.car_list)}"

    def __repr__(self):
       return f"{self.car_list.__repr__()}"

    def __iter__(self):
      #  return self.car_list.__iter__()
        return ListCar.IterCarList(self.car_list)

