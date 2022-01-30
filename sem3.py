from functools import reduce
import os
import random
import datetime
from time import sleep
import os

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
# # max = 25
# # for i in range(15):
# #     print(random_mid_sq(min, max))



# 40.Определить, присутствует ли в заданном списке строк, некоторое число
# lst = ['wejkrjkwerh dgff', 'wersdfgkjdj23365', 'sdf4fjdgfgg', 'fdgdgdfg3']
# number = 4
# print('да') if sum([str(number) in item for item in lst]) else print('нет')