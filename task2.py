name = input('Введите ваше имя: ')
s_name = input('Введите вашу фамилию: ')
year = int(input('Введите год вашего рождения: '))
city = input('Введите город проживания: ')
email = input('Введите ваш адрес эл. почты: ')
ph_number = input('Введите ваш номер телефона: ')


def func(name, s_name, year, city, email, ph_number):
    print(
        f"Имя - {name}; Фамилия - {s_name}; Год рождения - {year}; Город - {city}; Адрес эл. почты - {email}; телефон - {ph_number}")


func(name, s_name, year, city, email, ph_number)