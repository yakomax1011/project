# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки, инструмент: ручка.')

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки, инструмент: карандаш.')

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки, инструмент: маркер.')

test = Stationery('Альбом_1.0')
test.draw()

test1 = Pen('Альбом_1.1')
test1.draw()

test2 = Pencil('Альбом_1.2')
test2.draw()