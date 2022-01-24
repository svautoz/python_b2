# number = int(input('Введите число: '))
# print(f'Квадрат числа {number} равен {number **2}')
# print('Квадрат числа {1} равен {0}'.format(number, number ** 2))

# 1.По двум заданным числам проверять является ли первое квадратом второго

# def IsSquare(a, b):
#     return a == b * b

# print(IsSquare(4, 2))
# print(IsSquare(4, 3))


# 2.Даны два числа. Показать большее и меньшее число
# number1 = int(input('Введите первое число: '))
# number2 = int(input('Введите второе число: '))

# if number1 < number2:
#     print(f'Первое число {number1} меньше второго {number2}')
# elif number1 > number2:
#     print(f'Первое число {number1} больше второго {number2}')

# 3.По заданному номеру дня недели вывести его название

# def NameOfDay(day_number):
#     if day_number > 7 or day_number < 1 : return False
#     day_list = ['понедельник', 'вторник', 'среда',
#                 'четверг', 'пятница', 'суббота', 'воскресенье']
#     return day_list[day_number - 1]


# print(NameOfDay(4), NameOfDay(7), NameOfDay(10), NameOfDay(-5))

# 4.Найти максимальное из трех чисел
# num_list = [4, 55, 9, 17]
# max = num_list[0]

# for num in num_list:
#     if num > max:
#         max = num

# print(max)

# 5.Написать программу вычисления значения функции y = f(a)
# def f(a):
#     return a + 1

# a = 10
# y = f(a)
# print(y)

# 6.Выяснить является ли число чётным
# number = int(input('Введите число: '))
# if number % 2 == 0:
#     print('Число четное')
# else:
#     print('Число нечетное')

# 7.Показать числа от -N до N
# def ShowFromNToN(N):
#     print(list(range(-N, N+1)))

# ShowFromNToN(5)

# 8.Показать четные числа от 1 до N

# N = int(input('Введите число N: '))

# def showN(N):
#     for i in range(1, N + 1):
#         if i % 2 == 0:
#             print(i)

# showN(N)

# 9.Показать последнюю цифру трёхзначного числа
# def ShowThirdDigit(number):
#     if number > -100 and number < 100: return False
#     if number < 0: number = -number
#     print(f'Третья цифра {number // 100 % 10}')

# ShowThirdDigit(36)

# 10.Показать вторую цифру трёхзначного числа
# number = int(input('Введите трехзначное число: '))

# def GetSecondDigit(number):
#     return number // 10 % 10

# print(GetSecondDigit(number))

# 11.Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
# def GetGreaterDigit(number):
#     firstDigit =  number % 10
#     secondDigit =  number // 10
#     if firstDigit > secondDigit: return firstDigit
#     else: return secondDigit

# print(GetGreaterDigit(85), GetGreaterDigit(35), GetGreaterDigit(89))

# 12.Удалить вторую цифру трёхзначного числа
# number = int(input('Введите трехзначное число: '))

# def DeleteSecondDigit(number):
#     return number // 100 * 10 + number % 10

# print(DeleteSecondDigit(number))

# 13.Выяснить, кратно ли число заданному, если нет, вывести остаток.
# def IsMultiple(number_1, number_2):
#     result = number_1 % number_2
#     if result == 0:
#         return True
#     else:
#         return result


# print(IsMultiple(8, 2), IsMultiple(10, 3), IsMultiple(-6, 2))

# 14.Найти третью цифру числа или сообщить, что её нет
# number = int(input('Введите число: '))

# def GetThirdDigit(number):
#     if number < 100:
#         return 'Цифры нет'
#     return number % 1000 // 100

# print(GetThirdDigit(number))

# 16.Дано число обозначающее день недели. Выяснить является номер дня недели выходным
# number = int(input('Введите день недели: '))

# def IsWeekend(number):
#     if 5 < number < 8:
#         print('Выходной')
#     else:
#         print('Будни')

# IsWeekend(number)
