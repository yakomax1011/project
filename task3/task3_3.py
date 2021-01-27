#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
#и возвращает сумму наибольших двух аргументов.

def too_max(a, b, c):
    num = [a, b, c]
    e = max(num)
    num.remove(max(num))
    f = max(num)
    return e, f

a = int(input('Введите число для сравнения: '))
b = int(input('Введите число для сравнения: '))
c = int(input('Введите число для сравнения: '))

final_num = too_max(a, b, c)
print(final_num)

#def too_max(a, b, c):
#    list = []
#    n = int('Введите количество элементов для сравнения: ')
#    for i in range(n):
#        new_element = int(input('Введите числа для сравнения: '))
#        list.append(new_element)
#    b = max(list)
#    list.remove(max(list))
#    c = max(list)
#    return b, c
#
#final_num = too_max()
#print(final_num)