from itertools import count, cycle, islice

# а) итератор, генерирующий целые числа, начиная с указанного,


a = int(input("Укажите первое число последовательности >>> "))
n = int(input("Укажите количество элементов >>> "))

for i in islice(count(a), n):
    print(i)
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
print()
list_int = [2, 3, 5, 7]
print(list_int)

for el in islice(cycle(list_int), 10):
    print(el)
