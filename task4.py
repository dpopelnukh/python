def my_func1():
    x = float(input("Введите положительное число, возводимое в степень: "))
    y = float(input("Введите степень ввиде целого отрацельного числа: "))
    res = x ** y
    return res


print(f'Результат - {my_func1()}')


def my_func2():
    x = float(input("Введите положительное число, возводимое в степень: "))
    y = float(input("Введите степень ввиде целого отрацельного числа: "))
    res = 1
    while y < 0:
        res *= x
        y += 1
    res = 1 / res
    return res


print(f'Результат - {my_func2()}')
