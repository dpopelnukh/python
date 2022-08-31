"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class Error:
    def __init__(self, *args):
        self.my_list = []
        self.stop = False

    def mylist(self):
        while not self.stop:
            try:
                val = int(input('Введите значения: '))
                self.my_list.append(val)
                print(f'Текущий список: {self.my_list} \n ')
            except:
                print(f"Вы ввели не число!")
                stop = input(f'Попробовать еще раз? "stop" для выхода из программы, введите любой символ, чтобы продолжить.')

                if stop == 'stop':
                    self.stop = True

                else:
                    print(self.my_list)
        print(f'Конечный список: {self.my_list} \n ')


try_except = Error()
try_except.mylist()
