# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем.
# б окончании ввода данных свидетельствует пустая строка.

my_f = open('test_for_task1.txt', 'w', encoding='utf8')
line = input('Введите текст \n')
while line:
    my_f.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_f.close()
my_f = open('test_for_task1.txt', 'r', encoding='utf8')
content = my_f.readlines()
print(content)
my_f.close()