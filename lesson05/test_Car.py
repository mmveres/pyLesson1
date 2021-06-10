from lesson05.Car import Car


def test_brake():
    car = Car(50)
    car.brake()
    assert car.speed == 45



def test_say_state():
    assert False


def test_accelerate():
    assert False



def test_step():
    assert False


def test_average_speed():
    assert False


def test_sum():
    assert Car.sum(4,5)==9

def test_multy():
    assert Car.multy(4,5)==20