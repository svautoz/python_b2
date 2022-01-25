# https://github.com/iksergey/ProfCode/blob/master/Docs/006Tasks.md
# https://github.com/iksergey/HelloCode/blob/main/ex.md

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
# for number in list:
    