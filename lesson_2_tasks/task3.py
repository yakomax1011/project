#Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#Напишите решения через list и через dict.


winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

month = int(input('Введите месяц вашего рождения: '))

if month in winter:
    print('Winter')
if month in spring:
    print('Spring')
if month in summer:
    print('Summer')
if month in autumn:
    print('Autumn')



#Вариант решения №2

seasons = {'Winter': (1, 2, 12),
           'Spring': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)}

month = int(input('Введите месяц вашего рождения: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)

