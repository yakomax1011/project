#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#имя, фамилия, год рождения, город проживания, email, телефон.
#Функция должна принимать параметры как именованные аргументы.
#Реализовать вывод данных о пользователе одной строкой.

def my_dir(**kwargs):
    name_user = input('Введите ваше имя: ')
    surname_user = input('Введите вашу фамилию: ')
    age_user = (input('Введите год вашего рождения: '))
    city_user = input('Введите город вашего проживания:  ')
    email_user = input('Введите ваш адрес электронной почты: ')
    tel_user = input('Введите ваш контактный телеофн для связи: ')
    output_screen = dict(name = name_user,
                         surname = surname_user,
                         age = age_user,
                         city = city_user,
                         email = email_user,
                         telephone = tel_user)
    return output_screen

x = my_dir()
print(x)

