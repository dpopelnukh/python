"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open('f_py.txt', 'w+', encoding='utf-8') as my_f:
    text = input('Введите текст: ')
    while text:
        my_f.writelines(f"{text}\n")
        text = input('Введите текст: ')
        if not text:
            break
    my_f.seek(0)
    content = my_f.read()
    print(content)