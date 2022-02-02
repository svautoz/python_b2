from functools import reduce
from lib2to3.pytree import convert
import os
import random
import datetime
from time import sleep
import os
import math

# 31.Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д.
# N = 5
# user_set = set()
# mult = 1
# for i in range(N):
#     user_set.add(mult)
#     mult *= (-3)
# print(user_set)

# N = 10
# user_set = set((-3) ** i for i in range(N))
# print(user_set)


# 32.Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3k + 1.
# N = 5
# user_dict = {k: 3*k +1 for k in range(1, N+1)}
# print(user_dict)

# 33.Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
# str_1 = "к"
# str_2 = "крокодил кушает курицу"
# print(str_2.count(str_1))

# 34.Подсчитать сумму цифр в вещественном числе.
# float_number = 3.145
# sum_result = reduce(lambda a, b: a + b, [int(i) if i.isdigit() else 0 for i in str(float_number)])
# print(sum_result)

# 35.Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]
# Факториал
# N = 5
# lst = []
# mult = 1
# for i in range(1, N + 1):
#     lst += [i * mult]
#     mult = i * mult
# print(lst)
#
# def fact(number):
#     if number == 1: return 1
#     return number * fact(number - 1)

# N = 5
# lst = [fact(i) for i in range(1, N+1)]
# print(lst)


# 36.Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму
# n = 5
# lst = [(1+i / n)*i for i in range(1, n + 1)]
# print(lst)
# print(f'Сумма элементов списка = {sum(lst):.2f}')

# 37.Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число
# N = 5
# lst = [i for i in range(-N, N +1)]
# print(lst)

# with open("./file.txt", "r") as file:
#     mult = 1
#     for line in file:
#         mult *= lst[int(line)]
# print(mult)

# 38.Реализовать алгоритм перемешивания списка.
# def shuffle_list(lst):
#     sh_list = []
#     list_len = len(lst)
#     for i in range(1, list_len + 1):
#         rand_index = random.randint(0, list_len - i)
#         sh_list.append(lst.pop(rand_index))
#     return sh_list

# lst = [34, 564, 33, 5, 3, 8, 334]
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(lst)
# print(shuffle_list(lst))

# 39.Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел
# RAND_MAX = 9999
# def random_number(min, max):
#     while True:
#         rand_num = 0
#         current_date_time = datetime.datetime.now().timestamp() % 1
#         rand_num = int(str(current_date_time)[-1:-5:-1])
#         # Равномерно распределяем рандомное число в нашем диапазоне
#         fraction = 1.0 / (RAND_MAX + 1.0); 
#         rand_num = rand_num * fraction * (max - min + 1) + min    
#         return int(rand_num)

# for i in range(5):
#     sleep(1)
#     print(random_number(1, 10))


# Возьму готовый алгоритм
# Метод срединных квадратов
# RAND_MAX = 9999

# def random_mid_sq(min, max):    
#     if os.path.isfile('seed.txt'):
#         with open('seed.txt','r') as file:
#             seed = int(file.readline())
#     else:
#         seed = int(str(datetime.datetime.now().timestamp() % 1)[-1:-5:-1])           
#     for i in range(5):
#         if seed < 1001: seed *= max  # если число меньше заданной длины
#         seed = seed ** 2        
#         seed = int(str(seed)[2: 6]) + max - min  #добавляем значения, чтобы не ушло  в 0
#     with open('seed.txt','w') as file:
#             file.write(str(int(seed)))
#     # Равномерно распределяем рандомное число в нашем диапазоне
#     fraction = 1.0 / (RAND_MAX + 1.0); 
#     seed = seed * fraction * (max - min + 1) + min    
#     return int(seed)
    

# min = 1
# max = 250
# for i in range(15):
#     print(random_mid_sq(min, max))



# 40.Определить, присутствует ли в заданном списке строк, некоторое число
# lst = ['wejkrjkwerh dgff', 'wersdfgkjdj23365', 'sdf4fjdgfgg', 'fdgdgdfg3']
# number = 4
# print('да') if sum([str(number) in item for item in lst]) else print('нет')

# 41.Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.
# lst = ['sdf', 'serwerjhsd', 'sd234345', 'sdfsd', 'sdfsdf']
# sub_str = 'sdf'
# in_list = 0
# for i , item in enumerate(lst):
#     pos = item.find(sub_str)
#     if pos != -1:
#         in_list += 1
#     if in_list == 2:
#         print(i)

# # 42.Найти сумму чисел списка стоящих на нечетной позиции
# lst = [435, 5, 6, 5, 6, 32, 5, -5]
# print( sum([item if i % 2 else 0 for i, item in enumerate(lst)]) )

# 43.Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 
# lst = [4, 5, 3, 7, 3, 9, 5]
# list_len = len(lst)
# print([lst[i] * lst[list_len - i - 1] for i in range(0, list_len // 2 + 1)])

# 44.В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# lst = [1.1, 1.2, 3.1, 5.1, 10.01]
# float_lst = [round(item % 1, 2) for item in lst]
# print(float_lst)
# print(f'{max(float_lst) - min(float_lst) : .2f}')

# 45.Написать программу преобразования десятичного числа в двоичное
# number = 2
# str_number = ''
# while True:
#     if number < 2:
#         str_number += '1'        
#         break
#     str_number += str(number % 2)
#     number = number // 2
# str_number = str_number[::-1]
# print(str_number)

# 46.Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов
# 1 1 2 3 5 8 13
# def feb(N):
#     if N < 2: return 1
#     return feb(N-1) + feb(N-2)


# N = 10
# def feb_print(N):
#     list_1 = [0]
#     feb1 = 1
#     feb2 = 0
#     for i in range(N):
#         feb1, feb2 = feb2, feb1+feb2
#         list_1.append(feb2)
#         list_1.insert(0,((-1) **(i) * feb2))    
#     print(list_1)

# feb_print(N)

# 47.Строка содержит набор чисел. Показать большее и меньшее число
# string = '234738746152349'
# print(max([int(item) for item in string]))
# print(min([int(item) for item in string]))

# 48.Найти корни квадратного уравнения Ax² + Bx + C = 0
# Математикой
# Используя дополнительные библиотеки*
# def something():
#     A = 2
#     B = -5
#     C = 2
#     D = math.pow(B,2) - 4*A*C
#     if D < 0: return print('Нет корней')
#     if D == 0: return print((-B) / (2*A))     
#     x1 = (-B + math.sqrt(D)) / (2*A)
#     x2 = (-B - math.sqrt(D)) / (2*A)
#     print(x1, x2)

# something()



# 49.Найти НОК двух чисел
# def find_nok(A, B):
#     if A < B:
#         A, B = B, A
#     NOK = A
#     while True:
#         if not NOK % B:
#             return NOK            
#         else:
#             NOK += A 
# print(find_nok(45, 72))

# 50.Вычислить число  c заданной точностью d
#     Пример: при d = 0.001, π = 3.141. 10-1≤d≤10-10
# # d = '0.0000000000000000000000001'
# # print(d)
# # d = int(len(d) - 2)
# # pi = round(math.pi, d)
# print(f'{math.pi : .48f}')

# 51.Составить список простых множителей натурального числа N
# ограничение по перебору простых множителей sqrt(N)
# начинаем с наименьших простых множителей и до sqrt(N)
# def get_simple_list(N):
#     simple_list = []
#     lst = [number for number in range(2, int(N) + 1)]
#     for number in lst:
#         for i in range(2, number):
#             if not number % i:
#                 break
#         else:
#             simple_list.append(number)
#     return simple_list

# def get_simple_mult_list(simple_list, N):
#     mult_list = []
#     for sim_num in simple_list:
#         while not N % sim_num:
#             N /= sim_num
#             mult_list.append(sim_num)
#     if N > simple_list[-1]: mult_list.append(int(N))
#     return mult_list

# N = 3050
# simple_list = get_simple_list(N**0.5)
# print(N)
# print(simple_list)
# print(get_simple_mult_list(simple_list, N))