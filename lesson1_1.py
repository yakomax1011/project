# Задание 1
x = 12
print(x)
x *= 4
print(x)

y = "ok?"
print(y + ' ок!')

age = input('Сколько вам лет: ')
name = input('Как вас зовут: ')
print(name,'.', age, '? А вы молодец!')

# Задание 2
sec = int(input('Введите  примерное количество секунд которое вы тратите на чистку зубов в день: '))
hrs = (sec // 3600)
mint = (sec // 60)
sec = (sec % 60)
print(f'На чисту зубов вы тратите: {hrs} часов, {mint} минут и {sec} секунд')

# Задание 3
num1 = int(input('Здравствуйте, нет времени объяснять, введите число: '))
num2 = int(f'{num1}{num1}')
num3 = int(f'{num1}{num1}{num1}')
sum = num1 + num2 + num3
print(sum)

# Задание 4
num = int(input('Введите большое число: '))
num2 = num%10
num = num//10
while num > 0:
    if num%10 > num2:
        num2 = num%10
    num = num//10
print('Cамая большая цифра в числе: ', num2)

# Задание 5
size_sum = int(input('Здравствуйте, введите общий оборот компании за месяц: '))
cost = int(input('Здравствуйте, введите общие расходы компании (включая закупку товаров) за месяц: '))

if cost > size_sum:
    print('Уважаемый, компания работает в минус. У вас убыток равный: ', cost - size_sum)
else:
    print('Уважаемый, поздравляем, компания имеет прибыль равную: ', size_sum - cost)
    profit = size_sum - cost
    equality = int(input('Товарищ, какое количество человек работает в вашей компании: '))
    profit_equality = round(profit / equality)
    print('Ваши сотрудники получают по:', profit_equality, 'рублей в месяц. Спасибо товарищ. Это настоящий коммунизм!')

# Задание 6

standard = int(input('Сколько километров в день вы пробегаете ? Введите число: '))
target = int(input('Сколько километров в день вы хотели бы пробегать ? Введите число: '))
day = 1
while True:
    print(day, '-й день: ', standard, 'километров')
    standard = standard * 1.1
    standard = int(standard * 100) / 100
    day += 1
    if standard > target:
        break
print('Вы достигните результата: ', target, 'километров на ', day, ' день, если каждый день будете увеличивать расстояние на 10 % относительно предыдущего')



