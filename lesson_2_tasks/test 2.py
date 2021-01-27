seasons = {'winter': (1, 2, 12),
           'spring': (3, 4, 5),
           'summer': (6, 7, 8),
           'autumn': (9, 10, 11)}

month = int(input('Введите месяц вашего рождения: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)