
def task1():
    valuesting = "python"
    print(valuesting)
    inputvalue = input("Введите ваше значение:")
    print("Ваще значение:" + inputvalue)



def task2():
    seconds = int(input("Введите секунды"))
    hours = seconds / 60 // 60
    minutes = (seconds - hours * 60 * 60) // 60
    sec = seconds - hours * 60 * 60 - minutes * 60
    print('{}:{}:{}'.format(int(hours), int(minutes), int(sec)))


def task3():
    n = int(input("Введите число - "))
    total = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
    print("Сумма чисел n + nn + nnn - %d" % total)


def task4():
    n = abs(int(input("Введите целое положительное число ")))
    max = n % 10
    while n >= 1:
        n = n // 10
        if n % 10 > max:
            max = n % 10
        if n > 9:
            continue
        else:
            print("Максимальное цифра в числе ", max)
            break

def task5():
    profit = float(input("Введите выручку фирмы "))
    costs = float(input("Введите издержки фирмы "))
    if profit > costs:
        print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / costs:.2f}")
        workers = int(input("Введите количество сотрудников фирмы "))
        print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
    elif profit == costs:
        print("Фирма работает в ноль")
    else:
        print("Фирма работает в убыток")

def task7():
    a = int(input("Введите результаты пробежки первого дня в км "))
    b = int(input("Введите общий желаемый результат в км "))
    result_days = 1
    result_km = a
    while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
    print(f"Вы достигнете требуемых показателей на %.d день" % result_days)



if __name__ == "__main__":
    task7()

