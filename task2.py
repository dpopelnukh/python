name_i = input('Введите ваше имя: ')
s_name_i = input('Введите вашу фамилию: ')
year_i = int(input('Введите год вашего рождения: '))
city_i = input('Введите город проживания: ')
email_i = input('Введите ваш адрес эл. почты: ')
ph_number_i = input('Введите ваш номер телефона: ')


def func(name, s_name, year, city, email, ph_number):
    print(
        f"Имя - {name}; Фамилия - {s_name}; Год рождения - {year}; Город - {city}; Адрес эл. почты - {email}; телефон - {ph_number}")


func(name=name_i, s_name=s_name_i, year=year_i, city=city_i, email=email_i, ph_number=ph_number_i)