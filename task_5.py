from functools import reduce


list = [el for el in range(100, 1001) if el % 2 == 0]
print(list)


def my_func(prev, cur):
    return prev * cur


print(reduce(my_func, list))
