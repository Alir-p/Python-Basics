# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух
# матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

# class Matrix:
#     def __init__(self, li):
#         self.li = li
#
#     def __str__(self):
#         for i in self.li:
#             for j in i:
#                 print(f'{j:5}', end='')
#             print()
#         return ''
#
#     def __add__(self, other):
#         for i in range(len(self.li)):
#             for j in range(len(other.li[i])):
#                 self.li[i][j] = self.li[i][j] + other.li[i][j]
#         return Matrix(self.li)
#
#
# m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# m2 = Matrix([[0, 2, 4], [1, 3, 5], [6, 8, 10], [7, 9, 11]])
# print(m1 + m2)


# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

# from abc import ABC, abstractmethod
#
#
# class Clothes(ABC):
#
#     @abstractmethod
#     def __init__(self):
#         pass
#
#     @abstractmethod
#     def consumption(self):
#         pass
#
#
# class Coat(Clothes):
#     def __init__(self, name, v):
#         self.name = name
#         if v < 44:
#             self.size = 44
#         elif v > 68:
#             self.size = 68
#         else:
#             self.size = v
#
#     @property
#     def consumption(self):
#         return f'Для пошива пальто {self.name} потребуется {self.size / 6.5 + 0.5 :.2f} ткани'
#
#
# class Suit(Clothes):
#     def __init__(self, name, h):
#         self.name = name
#         if h < 164:
#             self.size = 164
#         elif h > 194:
#             self.size = 194
#         else:
#             self.size = h
#
#     @property
#     def consumption(self):
#         return f'Для пошива костюма {self.name} потребуется {2 * self.size + 0.3 :.2f} ткани'
#
#
# coat = Coat('Fin Flare', 44)
# suit = Suit('Stenser', 190)
# print(coat.consumption)
# print(suit.consumption)


# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его
# конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть
# реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять
# увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
# этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
# метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернёт
# строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернёт
# строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.

# class Cell:
#     def __init__(self, count: int):
#         self.count = count
#
#     def __add__(self, other):
#         return Cell(self.count + other.count)
#
#     def __sub__(self, other):
#         if self.count < other.count:
#             return 'Операция не возможна'
#         else:
#             return Cell(self.count - other.count)
#
#     def __mul__(self, other):
#         return Cell(self.count * other.count)
#
#     def __truediv__(self, other):
#         return Cell(self.count // other.count)
#
#     def make_order(self, row):
#         result = ''
#         for i in range(int(self.count / row)):
#             result += '*' * row + '\n'
#         result += '*' * (self.count % row) + '\n'
#         return result
#
#     def __str__(self):
#         return f'{self.count}'
#
#
# cell1 = Cell(17)
# cell2 = Cell(3)
# cell3 = Cell(7)
# print(cell1 + cell2)
# print(cell1 - cell2)
# print(cell2 - cell3)
# print(cell1 / cell3)
# print(cell2 * cell3)
# print(cell1.make_order(7))
