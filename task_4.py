"""
Задание 4.

Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).

А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    name: str
    color: str
    speed: int
    is_police: bool

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return 'начал движение'

    def stop(self):
        return 'остановился'

    def turn(self, dir):
        if dir == 'left':
            return 'повернул налево'
        elif dir == 'right':
            return 'повернул направо'
        else:
            return 'неверное направление'

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return 'превысил скорость'
        else:
            return self.speed


class SportCar(Car):
    def sport_car(self):
        return '- sport car.'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return 'превысил скорость'
        else:
            return self.speed


class PoliceCar(Car):
    def ispolice(self):
        if self.is_police is True:
            return "- police car."


bmw = TownCar("bmw", "Blue", 80, False)
cat = WorkCar("cat", "Gray", 30, False)
ferrari = SportCar("ferrari", "White", 160, False)
ford = PoliceCar("Police Car", "Black", 100, True)

print(
    f'Марка городского авто: {bmw.name}.\nЦвет рабочей машины: {cat.color}. \nСкорость спортивного авто: {ferrari.speed}км/ч.\nЛада - полицейский автомобиль: {ford.is_police}.')
print(f'{ferrari.name} {ferrari.sport_car()}\n{ferrari.name} {ferrari.go()} и {ferrari.turn("left")}.')
print(f'{bmw.name} {bmw.show_speed()} и {bmw.stop()}.')
print(f'{cat.name} {cat.turn("right")} и его скорость составляет сейчас {cat.show_speed()}км/ч.')
print(f'{ford.name} {ford.ispolice()}')
