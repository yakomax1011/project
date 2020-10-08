# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

with open("firms.txt", "r+") as f_obj:
    data = f_obj.read()
    data = data.split()
for i in range(len(data)):
    try:
       data[i] = int(data[i])
    except ValueError:
      pass
total1 = data[2] - data[3]
total2 = data[6] - data[7]
total3 = data[10] - data[11]
total4 = data[14] - data[15]
average_profit = int((total1 + total2 + total3 + total4) / 4)
final = [{data[0] : total1,
          data[4] : total2,
          data[8] : total3,
          data[12] : total4,},
         {'average_profit': average_profit}]
print(final)

import json
with open('task5_7_js.json', 'w') as f:
    json.dump(final, f)
