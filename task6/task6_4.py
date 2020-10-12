# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше
# 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Внимание! Ваша машина начала движение!')

    def stop(self):
        print('Стоп. Машина остановилась.')

    def turn_left(self, *args):
        self.left = args
        print('Поворот налево.')

    def turn_right(self, *args):
        self.right = args
        print('Поворот направо.')

    def show_speed(self):
        print('Ваша скорость: ', self.speed, 'км/ч')

class TownCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            print('Внимание превышение скорости!')
        else:
            print(self.speed)

    def parktronic(self, **kwargs):
        self.min_distance = kwargs
        print('Активирован режим парктроник.')

class SportCar(Car):
    def kick_down(self):
        print('Внимание. Моментальное повышение оборотов.')

class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            print('Внимание превышение скорости!')
        else:
            print(self.speed)

    def dump_truck(self):
        print("Автивирован режим саморазгрузки.")

class PoliceCar(Car):
    def dump_truck(self):
        print("Сирена активирована.")


test = Car(50, 'Белый', 'Лада', False)
test.go()
test.stop()
test.turn_left(1)
test.show_speed()

test2 = TownCar(60, 'Синий', 'Volvo', True)
test2.show_speed()