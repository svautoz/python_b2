# with open('./list.txt', 'r') as file:
#     string = file.readline()
#     lst = string.split(' ')
#     lst = [int(i) for i in lst]
#     print(lst)
#     new_list = [(i, i**2) for i in lst if i % 2 ==0]
#     print(new_list)

from functools import reduce
from operator import eq
import os
import random
from unittest import result

# 52.	Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# lst = [4, 6, 4, 8, 546, 56, 23, 56, 332,45]
# print(list(set(lst)))
# 53.	Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k. *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# k = 5
# equation_str = reduce(lambda x, y:  x + y, [str(i) + '**x' + str(random.randint(0, 100)) + ' + ' for i in range(k + 1)])
# print(equation_str)
# equation_str = equation_str[-4: -len(equation_str) - 1: -1]
# equation_str += ' = 0'
# print(equation_str)
# with open('ex53.txt', 'w') as file:
#     file.write(equation_str)

# 54.	Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.
# def get_k_eq(eq_str):
#     k = 0
#     eq_k_list = []
#     while True:
#         pow_str = ('x**' + str(k))
#         k += 1
#         k_end = eq_str.find(pow_str) - 1
#         if k_end == -2:
#             eq_k_list.append(0)
#             continue
#         i = k_end
#         number = ''
#         while eq_str[i] != ' ':
#             number += eq_str[i]
#             i -= 1
#         number = int(number[-1::-1])
#         if eq_str[i-1] == '-':
#             number = -1 * number
#         eq_k_list.append(number)
#         eq_str = eq_str[0:i-1]
#         if not len(eq_str):
#             return eq_k_list

# with open('ex54_1.txt') as file:
#     eq_1 = file.readline()
# with open('ex54_2.txt') as file:
#     eq_2 = file.readline()
# print(eq_1)
# print(eq_2)

# eq_k_list_1 = get_k_eq(eq_1)
# eq_k_list_2 = get_k_eq(eq_2)
# print(eq_k_list_1)
# print(eq_k_list_2)
# while len(eq_k_list_1) < len(eq_k_list_2):
#     eq_k_list_1 += [0]
# while len(eq_k_list_2) < len(eq_k_list_1):
#     eq_k_list_2 += [0]
     
# total_eq_k_list = [eq_k_list_1[i] + eq_k_list_2[i] for i in range(len(eq_k_list_2))]
# print(total_eq_k_list)

# k = len(total_eq_k_list) - 1
# equation_str = '0 = '
# for i in range(k + 1):
#     k = total_eq_k_list[i]
#     equation_str = equation_str + str(i) + '**x' + str(k)[-1::-1] + ' + '

# equation_str = equation_str[-3: -len(equation_str) - 1: -1]
# print(equation_str)
# with open('ex54.txt', 'w') as file:
#     file.write(equation_str)


# 55.	В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.
# def get_empty(lst):
#     for i in range(1, len(lst)):
#         if lst[i] - 1 != lst[i-1]:
#             return lst[i] - 1
#     return 1

# with open('ex55.txt', 'r') as file:
#     lst = file.readline().split()
# print(f'Это число {get_empty([int(i) for i in lst])}')

# 56.	Дан список чисел. Выделить среди них числа, удовлетворяющие условию: следующее больше предыдущего. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# init_lst = [1, 5, 2, 3, 4, 6, 1, 7]
# result_list = []

# for i in range(len(init_lst)):
#     j = i + 1
#     temp_list = [init_lst[i]]
#     while True:
#         if j == len(init_lst): break
#         if temp_list[len(temp_list) - 1] < init_lst[j]:
#             temp_list += [init_lst[j]]
#             j +=1
#         else:
#             break
#     result_list += [temp_list]
# print(result_list)

init_lst = [1, 5, 2, 3, 4, 6, 1, 7]
result_list = []

for i in range(len(init_lst)):
    j = i + 1
    temp_list = [init_lst[i]]
    new_init_list = init_lst[:]
    while True:        
        if j == len(new_init_list): break
        if temp_list[len(temp_list) - 1] < new_init_list[j]:
            temp_list += [new_init_list[j]]
            j +=1
        else:
            result_list += [temp_list]
            new_init_list.pop(j-1)
            temp_list = [init_lst[i]]
            j = i + 1
            
    result_list += [temp_list]
print(len(result_list))

# 57.	Дан список чисел. Выделить среди них максимальное количество чисел, удовлетворяющих условию предыдущей задачи. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]

# 58.	Напишите программу, удаляющую из текста все слова содержащие "абв".
# str = 'ываабв лповап абвцукв алоабвабв'
# print(str)
# str = str.split('абв')
# str = reduce(lambda x, y: x + y, [i for i in str])
# print(str)

# 59.	Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека

# a.	Добавьте игру против бота
# b.	Подумайте как наделить бота "интеллектом" 
# 60.	Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.
# 61.	Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет операций стандартный. Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -6; 
# a.	Добавить возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 => 9;
# 62.	Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# a.	входные и выходные данные хранятся в отдельных файлах
