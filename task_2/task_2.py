"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open("test.txt", "r", encoding='utf-8') as f:
    cont = f.read()
    f.seek(0)
    lines = f.readlines()
    print(f'количество строк: {len(lines)}')
    f.seek(0)
    for i, line in enumerate(lines):
        words = line.split()
        print(f'количество слов в {i + 1}-ой строке: {len(words)}')
