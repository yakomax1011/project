# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

obj2 = open('eng _to_ru_finish.txt', 'w', encoding='utf8')
obj = open('eng _to_ru_start.txt', 'r', encoding='utf8')

data = obj.readline()
data = data.replace('One', 'Один')
print(data.strip(), file=obj2)
print(data.strip())

data = obj.readline()
data = data.replace('Two', 'Два')
print(data.strip(), file=obj2)
print(data.strip())

data = obj.readline()
data = data.replace('Three', 'Три')
print(data.strip(), file=obj2)
print(data.strip())

data = obj.readline()
data = data.replace('Four', 'Четыре')
print(data.strip(), file=obj2)
print(data.strip())

obj2.close()
obj.close()