"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    day_month_year: str

    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def dd1(cls, self):
        d = int(self.day_month_year[0:2])
        m = int(self.day_month_year[3:5])
        y = int(self.day_month_year[6:10])
        return Date.valid(d, m, y)

    @staticmethod
    def valid(d, m, y):
        if 0 < d < 32:
            if 0 < m < 13:
                if 0 < y < 2023:
                    return f'Day: {d}\nMonth: {m}\nYear: {y}'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'


d1 = Date("31-08-2022")
print(Date.dd1(d1))
