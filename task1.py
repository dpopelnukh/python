def division():
    try:
        x = int(input("Введите делимое: "))
        y = int(input("Введите делитель: "))
        result = x / y
    except ZeroDivisionError:
        return "Деление на ноль невозможно!"
    return result


print(f"Результат деления: {division()} ")
