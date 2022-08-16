import sys

_, name, rate, hours = sys.argv


def calculate_salary(r, h):
    try:
        return int(r) * int(h) * 1.25
    except TypeError:
        print("Операция применена к объекту несоответствующего типа")
        exit()


print(f"сотрудник заработал: {calculate_salary(rate, hours)}")
