# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. Используйте
# в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных значений
# необходимо запускать скрипт с параметрами.

# from sys import argv
#
# prod, bet, reward = map(int, argv[1:])
# print(f'Заработная плата сотрудника составляет {prod * bet + reward}')


# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

# li = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# n_li = [li[i] for i in range(1, len(li)) if li[i] > li[i - 1]]
# print(n_li)


# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
# Подсказка: используйте функцию range() и генератор.

# li1 = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]


# 4. Представлен список чисел. Определите элементы списка, не имеющие повторений. Сформируйте итоговый массив чисел,
# соответствующих требованию. Элементы выведите в порядке их следования в исходном списке. Для выполнения задания
# обязательно используйте генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

# li2 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# n_li2 = [el for el in li2 if li2.count(el) == 1]
# print(n_li2)


# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти чётные
# числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

# from functools import reduce
#
#
# def mult(a, b):
#     return a * b
#
#
# li3 = [i for i in range(100, 1001) if i % 2 == 0]
# print(reduce(mult, li3))


# 6. Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее. Подсказка: используйте функцию count() и
# cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите условие
# его завершения. #### Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем
# цикл. Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

# from itertools import count, cycle
#
#
# def it1(a):
#     for i in count(a):
#         print(i)
#         if i > a + 10:
#             return
#
#
# def it2(sp):
#     s = 0
#     for i in cycle(sp):
#         print(i)
#         s += 1
#         if s > len(sp) * 10:
#             return
#
#
# a = 3
# sp = ['Hassliebe', 'Moonlight', 'Introduction', 'Liebesleid', 'Ballade']
#
# it1(a)
# it2(sp)


# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
# должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n). Она отвечает за
# получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

# def fact(x):
#     if x == 1:
#         f = 1
#         yield f
#         return f
#     else:
#         y = yield from fact(x - 1)
#         f = x * y
#     yield f
#     return f
#
#
# n = 4
# for i in fact(n):
#     print(i)
