#4. Программа принимает действительное положительное число x и целое отрицательное число y.
#Необходимо выполнить возведение числа x в степень y.
#Задание необходимо реализовать в виде функции my_func(x, y).
#При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
#Подсказка: попробуйте решить задачу двумя способами.
#Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **,
#предусматривающая использование цикла.

#def log(x, y):
#    sum = x ** y
#    return sum

def log(x, y):
    y_1 = y * -1     #abc(y)
    sum = 1
    for i in range(1, y_1 + 1):
        sum *= x
        sum_f = 1 / sum
    return sum_f

x = int(input('Введите степень основания: '))
y = int(input('Введите натуральная показатель: '))
final = log(x, y)
print(final)