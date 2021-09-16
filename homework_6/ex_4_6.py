class Cars:
    name = None
    speed = None
    color = None
    is_police = False

    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        return "Машина поехала"
    def stop(self):
        return "Машина остановилась"
    def turn(self, direction):
        return 'Машина повернула ' + direction

class TownCar(Cars):
    family = None
    def __init__(self, name, speed, color, family = True):
        name = None
        speed = None
        color = None
        self.family = family

class SportCar(Cars):
    def __init__(self, name, speed, color):
        name = None
        speed = None
        color = None

class WorkCar(Cars):
    def __init__(self, name, speed, color, is_police):
        name = None
        speed = None
        color = None
        is_police = False

class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        name = None
        speed = None
        color = True

Kia = TownCar('Kia Rio', 60, 'white')
print(Kia.name, Kia.color, Kia.speed, Kia.is_police)
print(Kia.go(), Kia.turn('направо'), Kia.stop())
sport_car = SportCar('Mazda', 240, 'orange')
work1 = WorkCar('Lada', 90, 'grey', True)
work2 = WorkCar('BMW', 90, 'white', False)
police = PoliceCar('police', 100, 'blue')
