# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

# li_st = []
# with open('test.txt', 'w', encoding='utf-8') as f:
#     print('Введите построчно текст. Для выхода введите пустую строку.')
#     while True:
#         st = input()
#         if st == '':
#             break
#         else:
#             li_st.append(st + '\n')
#     f.writelines(li_st)


# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в
# каждой строке.

# with open('test.txt', 'r', encoding='utf-8') as f1:
#     li_st1 = f1.readlines()
#     print(f'В файле строк - {len(li_st1)}')
#     i = 0
#     for st1 in li_st1:
#         word = st1.count(' ')
#         i += 1
#         print(f'Количество слов в {i}-й строке - {word + 1}')


# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее
# 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить
# подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

# with open('list of employees.txt', 'r', encoding='utf-8') as f2:
#     li_st2 = f2.readlines()
#     i = 0
#     average = 0
#     print('Список сотрудников с окладом меньше 20000: ', end='')
#     for workers in li_st2:
#         worker, salary = workers.split()
#         if int(salary) < 20000:
#             print(worker, end=' ')
#         i += 1
#         average += int(salary)
#     print()
#     print(f'Средняя зарплата: {round(average / i)}')


# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

# glossary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
# f3 = open('file1.txt', 'r', encoding='utf-8')
# n_f3 = open('file1_new.txt', 'a', encoding='utf-8')
# li_st3 = f3.readlines()
# n_li_st3 = []
# for st3 in li_st3:
#     word = st3.split()
#     word[0] = glossary[word[0]]
#     n_f3.write(' '.join(word))
#     n_f3.write('\n')
# f3.close()
# n_f3.close()


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить её на экран.

# with open('test1.txt', 'w', encoding='utf-8') as f4:
#     print('Введите числа разделенные пробелом. Для выхода введите любую букву.')
#     x = 0
#     while True:
#         li = input(': ').split()
#         for i in li:
#             try:
#                 x = int(i)
#             except ValueError:
#                 x = 'stop'
#                 break
#             f4.write(f'{x} ')
#         if x == 'stop':
#             break
#
# with open('test1.txt', 'r', encoding='utf-8') as f5:
#     li_st4 = f5.readline().split()
#     s = 0
#     for st4 in li_st4:
#         s += int(st4)
#     print(f'Сумма чисел в файле равна {s}')
