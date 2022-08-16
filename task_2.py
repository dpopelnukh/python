import random
primary_list = random.sample(range(1, 1000), 20)
print(primary_list)

# вариант без генератора
list2 = []
for el in range(len(primary_list) - 1):
    if primary_list[el] < primary_list[el+1]:
        list2.append(primary_list[el+1])
print(list2)


# вариант с генератором
list3 = [primary_list[el+1] for el in range(len(primary_list) - 1) if primary_list[el] < primary_list[el+1]]

print(list3)
