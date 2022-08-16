def my_sum():
    sum_res = 0
    ext = False
    while not ext:
        numb = input('введите числа через пробел или s - для выхода ').split()
        res = 0
        for el in numb:
            if el == 's':
                ext = True
                break
            else:
                res = res + int(el)
        sum_res = sum_res + res
        print(f'сумма = {sum_res}')
    print(f'общая сумма = {sum_res}')


my_sum()
