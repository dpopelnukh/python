int1 = int(input("Введите первое число: "))
int2 = int(input("Введите второе число: "))
int3 = int(input("Введите третье число: "))


def func(x, y, z):
    if x >= z and y >= z:
        return x + y
    elif y < x < z:
        return x + z
    else:
        return y + z


print(f'Результат - {func(int1, int2, int3)}')
