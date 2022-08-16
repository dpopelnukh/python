"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


def summary():
    with open("test.txt", "w+") as f:
        line = input('введите числа через пробел : ')
        f.writelines(line)
        f.seek(0)
        num = f.readline().split()
        print(sum(map(float, num)))


summary()

