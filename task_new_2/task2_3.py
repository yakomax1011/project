# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то,
# что загадано. Если за 10 попыток число не отгадано, вывести правильный ответ.

import random

num_true = random.randrange(0, 100)

for i in range(10, 0, -1):
  user_num = int(input('Введите число от 1 до 100: '))
  if user_num == num_true:
    print(f'Победа! Да, верное цисло = {num_true}. Заказываем билеты в Лас-Вегас?')
    exit()
  elif user_num < num_true:
    print('Искомое число больше введенного вами. Задумайтесь.')
  else:
    print('Искомое число меньше введенного вами. Задумайтесь.')

print(f'Неудача. Используйте метод двоичного поиска в следующий раз. Верное число = {num_true}')
