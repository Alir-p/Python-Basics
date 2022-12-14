# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) —
# на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
# завершать скрипт.

# from time import sleep
#
#
# class TrafficLight:
#
#     __color = ' '
#
#     def running(self):
#         color = ['красный', 'жёлтый', 'зеленый']
#         delay = [7, 2, 5]
#         for i in [0, 1, 2]:
#             self.__color = color[i]
#             print(self.__color)
#             sleep(delay[i])
#         print('Светофор погас')
#
#
# light = TrafficLight()
# light.running()


# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1
# см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

# class Road:
#
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     def calc(self, thick):
#         return self._width * self._length * thick * 25
#
#
# w = int(input('Введите ширину дороги (м): '))
# l = int(input('Введите длину дороги: (м): '))
# t = int(input('Введите толщину дороги: (см): '))
#
# road = Road(l, w)
# print(f'Необходимая масса асфальта составляет {road.calc(t)} кг')


# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
# (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров.

# class Worker:
#
#     _income = {'wage': 0, 'bonus': 0}
#
#     def __init__(self, s, n, p, w, b):
#         self.name = n
#         self.surname = s
#         self.position = p
#         self._income['wage'] = w
#         self._income['bonus'] = b
#
#
# class Position(Worker):
#
#     def get_full_name(self):
#         return f'{self.surname} {self.name}'
#
#     def get_total_income(self):
#         return self._income['wage'] + self._income['bonus']
#
#
# w1 = Position('Андреев', 'Денис', 'Слесарь', 10000, 1000)
#
# print(w1.get_full_name())
# print(w1.get_total_income())


# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите
# методы и покажите результат.

# class Car:
#     def __init__(self, name, color, speed, is_police=False):
#         self.name = name
#         self.color = color
#         self.speed = speed
#         self.is_police = is_police
#
#     def go(self):
#         print(f'Машина {self.name} поехала')
#
#     def stop(self):
#         print(f'Машина {self.name} остановилась')
#
#     def turn(self, direction):
#         side = {'l': 'налево', 'r': 'направо'}
#         print(f'Машина {self.name} поехала {side[direction]}')
#
#     def show_speed(self):
#         print(f'Текущая скорость {self.name} составляет {self.speed}')
#
#
# class TownCar(Car):
#     def show_speed(self):
#         print(f'Текущая скорость {self.name} {f"составляет {self.speed}" if self.speed <= 60 else "превышена" }')
#
#
# class SportCar(Car):
#     pass
#
#
# class WorkCar(Car):
#     def show_speed(self):
#         print(f'Текущая скорость {self.name} {f"составляет {self.speed}" if self.speed <= 40 else "превышена" }')
#
#
# class PoliceCar(Car):
#     pass
#
#
# car1 = PoliceCar('Police', 'blue', 100, True)
# car1.show_speed()
# print(car1.is_police)
#
# car2 = TownCar('Taxi', 'yellow', 80)
# car2.show_speed()
#
# car3 = SportCar('Racer', 'red', 150)
# car3.turn('r')
# car3.turn('l')
#
# car4 = WorkCar('Shovel', 'white', 30)
# car4.go()
# car4.stop()


# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное
# сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

# class Stationery:
#     def __init__(self, title='stylos'):
#         self.title = title
#
#     def draw(self):
#         print('Запуск отрисовки')
#
#
# class Pen(Stationery):
#     def draw(self):
#         print('Запуск отрисовки ручкой')
#
#
# class Pencil(Stationery):
#     def draw(self):
#         print('Запуск отрисовки карандашом')
#
#
# class Handle(Stationery):
#     def draw(self):
#         print('Запуск отрисовки маркером')
#
#
# accessory1 = Stationery()
# accessory1.draw()
#
# accessory2 = Pen('Parker')
# accessory2.draw()
#
# accessory3 = Pencil('Brauberg')
# accessory3.draw()
#
# accessory4 = Handle('Highlighter')
# accessory4.draw()
