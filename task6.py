wrd = input("Введите слово: ")


def int_func(word):
    return word.title()


print(int_func(wrd))
my_f = input("Введите слова: ")


def my_func2(my_string):
    wrds = my_string.split()
    new_string = ""
    for w in wrds:
        new_string += int_func(w)
        new_string += " "
    return new_string


print(my_func2(my_f))
