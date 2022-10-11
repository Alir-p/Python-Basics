# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год»
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

# class Date:
#     def __init__(self, incom_date):
#         self.income_date = incom_date
#
#     @classmethod
#     def sep(cls, income_date):
#         new_date = income_date.split('-')
#         return list(map(int, new_date))
#
#     @staticmethod
#     def valid(income_date):
#         day, month, year = Date.sep(income_date)
#         if day not in range(1, 32):
#             return 'Неверный день'
#         elif month not in range(1, 13):
#             return 'Неверный месяц'
#         elif year not in range(2023):
#             return 'Неверный год'
#         else:
#             return 'Дата верна'
#
#
# today = Date('08-10-2022')
# print(Date.valid('11-13-2001'))
# print(today.valid('11-1-2202'))
# print(Date.valid('11-1-2001'))
# print(Date.sep(today.income_date))
# print(today.sep('25-11-2000'))


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

# class DivisionByZero(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# def div():
#     try:
#         num1 = int(input('Введите делимое: '))
#         num2 = int(input('Введите делитель: '))
#         if num2 == 0:
#             raise DivisionByZero("Деление на ноль!")
#         else:
#             return num1 / num2
#     except (ValueError, DivisionByZero) as err:
#         return err
#
#
# print(div())


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо
# только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами выводится на
# экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. Во время ввода
# пользователем очередного элемента необходимо реализовать проверку типа элемента. Вносить его в список, только если
# введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее
# сообщение. При этом работа скрипта не должна завершаться.

# class MyError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# def check():
#     li = []
#     while True:
#         i = input('Введите положительное целое число, для окончания введите «stop»: ')
#         if i == 'stop':
#             return print(f'Ввод завершен. Итоговый список {li}')
#         else:
#             try:
#                 for j in i:
#                     if ord(j) not in range(48, 58):
#                         raise MyError('Недопустимое значение!')
#             except MyError as err:
#                 print(err)
#             else:
#                 li.append(int(i))
#
#
# check()


# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
# базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а
# также других данных, можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

# class MyError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# class Warehouse:
#     uid = {}
#     dept = ['Склад', 'Отдел1', 'Отдел2', 'Отдел3']
#
#     def accept(self, id_eqp):
#         idq = id_eqp.name
#         print(f'Принимаем на баланс {idq}')
#         for num, dep in enumerate(self.dept, 1):
#             print(f'{num}. {dep}', end=' ')
#         print()
#         while True:
#             try:
#                 c_dep = int(input(f'Выберите целевой отдел [ ]: '))
#                 n_dep = int(input(f'Укажите количество принимаемой техники: '))
#                 if c_dep not in range(1, len(self.dept) + 1):
#                     raise MyError('Недопустимое значение отдела!')
#                 elif n_dep not in range(1, 100):
#                     raise MyError('Недопустимое значение количества!')
#                 else:
#                     self.uid.update({idq: {self.dept[c_dep - 1]: n_dep}})
#                     # print(self.uid.items())
#                     break
#             except (MyError, ValueError) as err:
#                 print(err)
#
#
# class OfficeEquipment:
#     def __init__(self, name, price, producer):
#         self.name = name
#         self.price = price
#         self.producer = producer
#
#
# class Printer(OfficeEquipment):
#     def __init__(self, name, price, producer, color: bool):
#         super().__init__(name, price, producer)
#         self.type = 'printer'
#         self.color = color  # цветной или черно-белый
#
#
# class Scanner(OfficeEquipment):
#     def __init__(self, name, price, producer, format_a):
#         super().__init__(name, price, producer)
#         self.type = 'scaner'
#         self.format_a = format_a  # формат А0-8
#
#
# class Copier(OfficeEquipment):
#     def __init__(self, name, price, producer, speed):
#         super().__init__(name, price, producer)
#         self.type = 'copier'
#         self.speed = speed  # страниц в минуту
#
#
# pr1 = Printer('HL-L2300DR', 17999, 'Brother', False)
# pr2 = Printer('Color LaserJet 150nw', 42499, 'HP', True)
# sc1 = Scanner('OpticPro A360 Plus', 89699, 'Plustek', 'A3')
# sc2 = Scanner('CanoScan LiDE 400', 25499, 'Canon ', 'A4')
# cop1 = Copier('M6500W', 12799, 'Pantum', 22)
# cop2 = Copier('ECOSYS M3655idn', 159999, 'Kyocera', 55)
#
# storage = Warehouse()
# storage.accept(pr1)
# storage.accept(sc2)
# storage.accept(cop2)
# print(storage.uid.items())


# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
# (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

# class ComplexNumber:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __add__(self, other):
#         return ComplexNumber((self.a + other.a), (self.b + other.b))
#
#     def __mul__(self, other):
#         return ComplexNumber((self.a * other.a - (self.b * other.b)), (self.b * other.a + (self.a * other.b)))
#
#     def __str__(self):
#         if self.b < 0:
#             return f'{self.a}{self.b}*i'
#         else:
#             return f'{self.a}+{self.b}*i'
#
#
# c1 = ComplexNumber(7, -7)
# c2 = ComplexNumber(2, 3)
# print(c1 + c2)
# print(c1 * c2)
