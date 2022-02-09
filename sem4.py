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
from tkinter.messagebox import RETRY
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
# 1.Проходим цикл с каждым элементом. От элемента и до конца списка
# 2.В результат пишем текущую позицию. 
# 3.Если следующая позиция больше предыдущей A[i-1] < A[i], то вносим в результат. До конца списка.
# 4.Идем дальше на пункт 3
# 5.Если следующая позиция меньше (else от 3.), то  пропускаем и идем дальше на 3.. 
# 6.Как прошли список, то начинаем с первого элемента, но сравнение уже не со вторым, а с третьм, четвертым ....
# Итого три вложенности. А: проход по каждому элементу. В: Элемент из прошло цикла и следующий. С: Элемент из первого, второго цикла и до конца списка.

# Вариант с рекурсией
# def get_sub_list(item_index, init_lst, temp_list):
#     result_list = []
#     init_len = len(init_lst)
#     for sub_item_index in range(item_index, init_len):
#         if init_lst[sub_item_index] > temp_list[len(temp_list) - 1]:
#             temp_list += [init_lst[sub_item_index]]
#             result_list += [temp_list[:]]
#         else:
#             if init_lst[sub_item_index] > temp_list[0]:
#                 result_list += get_sub_list(sub_item_index, init_lst, [temp_list[0]])    
#     return result_list
# Рабочий вариант
# init_lst = [1, 5, 2, 3, 4, 6, 1, 7]
# result_list = []
# init_len = len(init_lst)

# def get_sub_list(item_index, init_lst, temp_list):
#     result_list = []
#     init_len = len(init_lst)
#     for sub_item_index in range(item_index, init_len):
#         if init_lst[sub_item_index] > temp_list[len(temp_list) - 1]:
#             temp_list += [init_lst[sub_item_index]]
#             result_list += [temp_list[:]]
#     return result_list

# for item_index in range(init_len):
#     temp_list = [init_lst[item_index]] 
#     result_list += [temp_list[:]]
#     for sub_item_index in range(item_index + 1, init_len):
#         result_list += get_sub_list(sub_item_index, init_lst, temp_list[:])

# print(result_list)
# print(len(result_list))

# result_list = [tuple(item) for item in result_list]
# print(set(result_list))
# print(len(set(result_list)))


# 57.	Дан список чисел. Выделить среди них максимальное количество чисел, удовлетворяющих условию предыдущей задачи. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# init_lst = [1, 5, 2, 3, 4, 6, 1, 7]
# result_list = []
# init_len = len(init_lst)

# for item_index in range(init_len):
#     temp_list = [init_lst[item_index]] 
#     result_list += [temp_list[:]]
#     for sub_item_index in range(item_index + 1, init_len):
#         result_list += get_sub_list(sub_item_index, init_lst, temp_list[:])

# print(result_list)
# print(len(result_list))   
# max_list = 0

# save_i_list = []
# for i_list in result_list:
#     if len(i_list) > max_list:
#         max_list = len(i_list)
#         save_i_list = i_list
# print(save_i_list)        

# print(max(map(lambda x: len(x), [i_list for i_list in result_list])))

# 58.	Напишите программу, удаляющую из текста все слова содержащие "абв".
# str = 'ываабв лповап абвцукв алоабвабв ываываыв'
# print(str)
# tr = str.split()
# [tr.remove(word) for word in tr[:] if 'абв' in word]        
# print(tr)


# 59.	Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
# https://cloud.mail.ru/public/kczH/yLqakTmUy
# sweets = 121
# max_sweets = 28
# turn = 1
# def get_hint_user(sweets, max_sweets):
#     if max_sweets >= sweets:
#         return sweets
#     number = sweets // max_sweets
#     y = number * max_sweets + 1
#     return sweets - y

# def get_hint_comp(sweets, max_sweets):
#     if max_sweets >= sweets:
#         return sweets
#     number = sweets // max_sweets    
#     y = number * max_sweets + 1
#     if y >= sweets:
#         y = (number - 1) * max_sweets + 1
#     return (random.randint(1, sweets if max_sweets > sweets else max_sweets) 
#     if sweets - y == 0 else sweets - y)

# def get_sweets(turn):
#     while True:
#         if turn == 1:
#             print(f'Заберите {get_hint_user(sweets, max_sweets)} конфет')
#             sweet_count = int(input(f'Сколько конфет забрать игроку {turn}:'))
#         else:
#             sweet_count = get_hint_comp(sweets, max_sweets)
#             print(f'Бот ввел число: {sweet_count}')
#         if sweet_count >= max_sweets:
#             sweet_count = max_sweets
#         return sweet_count    

# while True:
#     print(f'Конфет осталось {sweets}')
#     sweets -= get_sweets(turn)
#     if sweets <= 0:
#         turn = 'Бот' if turn == 2 else 'Человек'
#         print(f'Победил игрок {turn}')
#         break    
#     turn = 2 if turn == 1 else 1


# a.	Добавьте игру против бота
# b.	Подумайте как наделить бота "интеллектом" 
# 60.	Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.
# def print_table(table_list):
#     for index, row in enumerate(table_list, 1):
#         print(row, end=' ')
#         if not(index % 3): print('')
        

# def init_table():
#     return [i for i in range(1, 10)]

# def turn(lst, players_turn):    
#     while True:
#         cell = int(input('Введите ячейку для крестика: '))
#         if not (lst[cell - 1] in ['O','X']): break
#     lst[cell - 1] = players_turn 

# def check_win(lst, players_turn):
#     index_set = {index for index, value in enumerate(lst,1) if value == players_turn}
#     for ch_set in win_list:
#         if index_set == ch_set:
#             return players_turn           
#     return False

# table_list = init_table()
# win_list = [{1,2,3}, {4,5,6}, {7,8,9}, {1,5,9}, {3,5,7}, {1,4,7}, {2,5,8}, {3,6,9}]
# players_turn = 'X'

# for i in range(1, 10):    
#     print_table(table_list)
#     print(f'\nХод {i}')
#     turn(table_list, players_turn)
#     check = check_win(table_list, players_turn)
#     if check != False:
#         print(f'Победил {players_turn}')
#         print_table(table_list)
#         break
#     players_turn = 'X' if players_turn == 'O' else 'O'
# 61.	Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. 
# приоритет операций стандартный. Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -6; 

# def parse_exp(expression: str):
#     sub_str = ''
#     ex_list = []
#     for char in expression:
#         if char.isdigit():
#             sub_str += char
#         else:
#             ex_list.append(int(sub_str))
#             ex_list.append(char)
#             sub_str = ''
#     ex_list.append(int(sub_str))
#     index = 0
#     while index < len(ex_list):
#         if ex_list[index] in ['*', '/']:
#             ex_list = mod_list(ex_list, index)
#             index = 0
#         index += 1   
#     index = 0
#     while index < len(ex_list):
#         if ex_list[index] in ['+', '-']:
#             ex_list = mod_list(ex_list, index)
#             index = 0
#         index += 1  
#     return ex_list

# def mod_list(ex_list, index):
#     sub_list = [ex_list[index - 1], ex_list[index], ex_list[index + 1]]
#     ex_list.pop(index - 1)
#     ex_list.pop(index - 1)
#     ex_list.pop(index - 1)
#     ex_list.insert(index - 1, sub_list)
#     return ex_list

# def calc(ex_list: list):
#     if isinstance(ex_list[0], list):
#         a = calc(ex_list[0])
#     else:
#         a = ex_list[0]
#     if isinstance(ex_list[2], list):
#         b = calc(ex_list[2])
#     else:
#         b = ex_list[2]

#     if ex_list[1] == '+':    
#         return a + b  
#     elif ex_list[1] == '-':    
#         return a - b  
#     elif ex_list[1] == '*':    
#         return a * b 
#     elif ex_list[1] == '/':    
#         return a / b
#     return result

# # def calc(ex_list: list):
# #     for oper in ex_list[1: len(ex_list) - 1: 2]:

# #     return result
# # [2, +, 2, *, 2, /, 2]
# # [2, +, [[2*2], /, 2]]


# expression =  '22*3+3*2-4+2*2-10/2'  #input('Введите выражение: ')
# parsed_list = parse_exp(expression)
# print(parsed_list[0])
# print(calc(parsed_list[0]))
# # print(calc(parse_exp(expression)))
 
# a.	Добавить возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 => 9;

# def parse_exp(expression: str):
#     sub_str = ''
#     ex_list = []
#     for char in expression:
#         if char.isdigit():
#             sub_str += char
#             continue
#         else:      
#             if sub_str != '': ex_list.append(int(sub_str))
#             ex_list.append(char)
#         sub_str = ''
        
#     if sub_str != '': ex_list.append(int(sub_str))
#     index = 0
#     while index < len(ex_list):
#         if ex_list[index] == '(': start = index  
#         if ex_list[index] == ')':  
#             ex_list.insert(start, ex_list[start + 1:index])
#             [ex_list.pop(start + 1) for i in range(index - start + 1)]
#         index += 1   
#     index = 0
#     while index < len(ex_list):
#         if ex_list[index] in ['*', '/']:
#             ex_list = mod_list(ex_list, index)
#             index = 0
#         index += 1   
#     index = 0
#     while index < len(ex_list):
#         if ex_list[index] in ['+', '-']:
#             ex_list = mod_list(ex_list, index)
#             index = 0
#         index += 1  
#     return ex_list

# def mod_list(ex_list, index):
#     sub_list = [ex_list[index - 1], ex_list[index], ex_list[index + 1]]
#     [ex_list.pop(index - 1) for i in range(3)]
#     ex_list.insert(index - 1, sub_list)
#     return ex_list

# def calc(ex_list: list):
#     if isinstance(ex_list[0], list):
#         a = calc(ex_list[0])
#     else:
#         a = ex_list[0]
#     if isinstance(ex_list[2], list):
#         b = calc(ex_list[2])
#     else:
#         b = ex_list[2]
#     if ex_list[1] == '+':    
#         return a + b  
#     elif ex_list[1] == '-':    
#         return a - b  
#     elif ex_list[1] == '*':    
#         return a * b 
#     elif ex_list[1] == '/':    
#         return a / b
#     return result

# expression = '(2+2)*2+8/2+4/(1+1)*3' #'20+3*2-4+2*2-100/2'  #input('Введите выражение: ')
# parsed_list = parse_exp(expression)
# print(parsed_list[0])
# print(calc(parsed_list[0]))

# 62.	Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.

# def set_archive(data, path):
#     str2= ''
#     i = 0
#     sub_str = data[0]
#     for char in data:    
#         if sub_str == char:
#             i += 1
#             continue
#         str2 += str(i) + sub_str
#         sub_str = char
#         i = 1
#     str2 += str(i) + sub_str    
#     with open(path, 'w') as file:
#         file.write(str2)

# def get_archive(path):
#     with open(path, 'r') as file:
#          data = file.read()
#     str2= ''
#     sub_str = ''
#     for char in data:    
#         if char.isdigit():
#             sub_str += char
#         else:
#             str2 += char*int(sub_str)
#             sub_str = ''
#     return str2
    

# text = input('Введите текст для архивации: ')

# set_archive(text, 'archive.txt')
# print(get_archive('archive.txt'))

# 63.Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10, 11] => [2, 10]

lst =[1, 2, 3, 5, 1, 5, 3, 10, 11]
dct = dict.fromkeys(lst, 0)
print(dct)
for item in lst:
    dct[item] += 1

print([index for index, value in dct.items() if value == 1])