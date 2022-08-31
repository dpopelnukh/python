"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDivisionError(Exception):
    def __str__(self):
        return f'На ноль делить нельзя!'


def dell(x, y):
    if y == 0:
        raise ZeroDivisionError
    else:
        return x/y


a = int(input("ведите чило a: "))
b = int(input("ведите чило b: "))
try:
    print(dell(a, b))
except ZeroDivisionError as exception:
    print(exception)
