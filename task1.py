x = int(input("Введите делимое: "))
y = int(input("Введите делитель: "))


def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Деление на ноль невозможно!"
    return result


print(f"Результат деления: {division(x, y)} ")
