# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open("staff_money.txt", "r+", encoding='utf8') as f_obj:
    data = f_obj.read()
    data = data.split()
for i in range(len(data)):
    try:
       data[i] = int(data[i])
    except ValueError:
      pass

democracy = {data[i]: data[i+1] for i in range(0, len(data), 2)}
print(democracy)
min_sum = min(democracy)
print('Cотрудники имеещие оклад менее 20 тыс: ', min_sum)
sum_dict = sum(democracy.values()) / len(democracy)
print('Cредняя величина дохода сотрудников = ', sum_dict)
