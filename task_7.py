from itertools import count

n = int(input("Укажите целое неотрицательное число >>> "))


def factgen():
    factorial = 1
    for el in count(1):
        factorial = factorial * el
        yield factorial


gen = factgen()
i = 0
for elem in gen:
    if i < n:
        print(elem)
        i += 1
    else:
        break
