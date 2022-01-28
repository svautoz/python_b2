# https://github.com/iksergey/ProfCode/blob/master/Docs/006Tasks.md
# https://github.com/iksergey/HelloCode/blob/main/ex.md
import random
import library as lib
from functools import reduce


# # 18.Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y
# def CheckFunc(x, y):
#     return (not(x or y)) == ((not x) and (not y))


# print(CheckFunc(True, True), CheckFunc(False, False),
#       CheckFunc(True, False), CheckFunc(False, True))

# # 20.Задать номер четверти, показать диапазоны для возможных координат
# quarter = int(input('Введите номер четверти>>> '))
# if quarter == 1:
#     print(f'x > 0, y > 0')
# elif quarter == 2:
#     print(f'x < 0, y > 0')
# elif quarter == 3:
#     print(f'x < 0, y < 0')
# elif quarter == 4:
#     print(f'x > 0, y < 0')
# else:
#     print('Неверно указан номер четверти')


# 22.Найти расстояние между точками в пространстве 2D/3D

# def GetLength(list):
#     point1, point2 = list
#     i = 0
#     length = 0
#     while i < len(point1):
#         length += (point1[i]-point2[i])**2
#         i += 1
#     return length**0.5


# points = [[1, 1, 5], [-1, 1, 5]]
# print(GetLength(points))

# 24.Найти кубы чисел от 1 до N
# N = 10
# for number in range(1, N + 1):
#     print(number**3)

# 26.Возведите число А в натуральную степень B используя цикл
# A = 2
# B = 6
# i = 0
# result = 1
# while i < B:
#     result *= A
#     i += 1
# print(result)


# 28.Подсчитать сумму цифр в числе
# number = input('Введите число>>> ')
# num = str(number)
# result = 0
# for i in num:
#     result += int(i)

# print(result)


# 30.Показать кубы чисел, заканчивающихся на четную цифру
# list = [12, 7, 89, 64, 44]
# for i in list:
#     if i % 2 == 0:
#         print(i, '>>>', i**3)


# 32.Задать массив из 8 элементов, заполненных нулями и единицами вывести их на экран
# import random
# list  = []
# for i in range(8):
#     list.append(random.randint(0, 1))

# print(list)

# 34.Написать программу замену элементов массива на противоположные
# list = [45, 66, -34, -43]
# print([number * (-1) for number in list])


# 15. Дано число. Проверить кратно ли оно 7 и 23
# number = random.randrange(0, 500, 23)
# print(f'Кратность числа {number} 7 и 23:', 'Кратность подтверждена' if not(number % 7 or number % 23) else 'Не кратно')

# 17. По двум заданным числам проверять является ли одно квадратом другого
# a, b = 4, 2
# print(a**2 == b or b**2 == a)

# 19. Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0
# coordinates = [[1, 3], [-5, 10], [-34, -32], [4, -45]]
# def get_quater(coordinate):
#     if coordinate[0] > 0 and coordinate[1] > 0:
#         print('Первая четверть')
#     elif coordinate[0] < 0 and coordinate[1] > 0:
#         print('Вторая четверть')
#     elif coordinate[0] < 0 and coordinate[1] < 0:
#         print('Третья четверть')
#     elif coordinate[0] > 0 and coordinate[1] < 0:
#         print('Четвертая четверть')

# for coordinate in coordinates:
#     get_quater(coordinate)

# 21. Программа проверяет пятизначное число на палиндромом.
# number = 4588545
# str_number = str(number)
# length = int(len(str_number) / 2)
# print('Палиндром') if str_number[0:length] == str_number[-1:-(length+1):-1] else print('Не палиндром')

# 23. Показать таблицу квадратов чисел от 1 до N
# N = 15
# for i in range(1, N + 1):
#     print(f'Квадрат числа {i} = {i**2}')

# 25. Найти сумму чисел от 1 до А
# A = random.randint(1, 10)
# print(A)

# print(reduce(lambda x, y: x + y,range(1, A + 1)))

# print(sum(i for i in range(1, A + 1)))

# 27. Определить количество цифр в числе
# number = random.randint(1, 54545454)
# print(number)
# print(len(str(number)))

# 29. Написать программу вычисления произведения чисел от 1 до N
# N = random.randint(1, 10)
# print(N)
# result = 1
# for i in range(1, N+1):
#     result *= i
# print(result)

# Почувствуй себя сеньором*
# 31. Задать массив из 8 элементов и вывести их на экран
# print(lib.make_array(8))

# # 32. Задать массив из 8 элементов, заполненных нулями и единицами вывести их на экран
# print(lib.make_array(8, (0, 1)))

# 33. Задать массив из 12 элементов, заполненных числами из [0,9]. Найти сумму положительных/отрицательных элементов массива
# lst = lib.make_array(12, (-9, 9))
# print(lst)
# pos_sum = 0
# for i in lst:
#     pos_sum += i if i > 0 else 0
# print(f'Сумма положительных элементов: {pos_sum}')

# 34. Написать программу замену элементов массива на противоположные
# lst = lib.make_array(12, (-9, 9))
# print(lst)
# # for i, val in enumerate(lst):
# #     lst[i] = -val

# lst = [-i for i in lst]

# print(lst)

# 35. Определить, присутствует ли в заданном массиве, некоторое число
# lst = lib.make_array(12, (-9, 9))
# number = 5
# print(lst)
# print ('Присутствует') if number in lst else print ('Отсутствует')

# 36. Задать массив, заполнить случайными положительными трёхзначными числами. Показать количество нечетных\четных чисел
# lst = lib.make_array(10, (100, 999))
# print(lst)
# even_sum = 0
# for i in lst:
#     even_sum += 0 if i % 2 else 1
# print(even_sum)

# 37. В одномерном массиве из 123 чисел найти количество элементов из отрезка [10,99]
# lst = lib.make_array(123, (0, 999))
# sum = 0
# print(lst)
# for i in lst:
#     sum += 1 if i in range(10, 100) else 0
# print(sum)

# 38. Найти сумму чисел одномерного массива стоящих на нечетной позиции
# lst = lib.make_array(12, (0, 9))
# print(lst)
# print(sum(lst[::2]))

# 39. Найти произведение пар чисел в одномерном массиве. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# lst = lib.make_array(10, (0, 9))
# new_lst = []
# print(lst)
# for i in range(int(len(lst) / 2)):
#     new_lst += [lst[i] * lst[-i-1]]
# print(new_lst)


# 40. В Указанном массиве вещественных чисел найдите разницу между максимальным и минимальным элементом
# lst = lib.make_float_array(10, (0, 9))
# print(lst)
# print(max(lst) - min(lst))


# ## Почувствуй себя лидом*
# 41. Выяснить являются ли три числа сторонами треугольника
# lst = lib.make_array(3, (0, 100))
# print(lst)

# for i in lst:
#     temp_list = lst[:]
#     temp_list.remove(i)
#     if i > sum(temp_list):
#         print('не является')
#         break
# else:
#     print('является')

# 42. Определить сколько чисел больше 0 введено с клавиатуры
# list = lib.digit_input()
# result = 0
# print(list)
# for i in list:
#     result += i if i > 0 else 0
# print(result)

# 43. Написать программу преобразования десятичного числа в двоичное

# 44. Найти точку пересечения двух прямых заданных уравнением y = k1 * x + b1, y = k2 * x + b2, b1 k1 и b2 и k2 заданы
# 45. Показать числа Фибоначчи
# 46. Написать программу масштабирования фигуры
# ```
# Тут для тех кто далеко улетел, чтобы задавались вершины фигуры списком (одной строкой)
# например: "(0,0) (2,0) (2,2) (0,2)"
# коэффициент масштабирования k задавался отдельно - 2 или 4 или 0.5
# В результате показать координаты, которые получатся.
# при k = 2 получаем "(0,0) (4,0) (4,4) (0,4)"
# ```
# 47. Написать программу копирования массива
