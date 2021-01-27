# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


with open('sum_numb.txt', 'w') as obj:
    print('34 34 1 13 3', file=obj)

with open('sum_numb.txt', 'r+') as obj:
    data = obj.read()
    data = data.split()

for i in range(len(data)):
    try:
       data[i] = int(data[i])
    except ValueError:
      pass

data = sum(data)
print(data)