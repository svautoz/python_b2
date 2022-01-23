# number = int(input('Введите число: '))
# print(f'Квадрат числа {number} равен {number **2}')
# print('Квадрат числа {1} равен {0}'.format(number, number ** 2))


# 2.Даны два числа. Показать большее и меньшее число
# number1 = int(input('Введите первое число: '))
# number2 = int(input('Введите второе число: '))

# if number1 < number2:
#     print(f'Первое число {number1} меньше второго {number2}')
# elif number1 > number2:
#     print(f'Первое число {number1} больше второго {number2}')


# 4.Найти максимальное из трех чисел
# num_list = [4, 55, 9, 17]
# max = num_list[0]

# for num in num_list:
#     if num > max:
#         max = num

# print(max)

# 6.Выяснить является ли число чётным
# number = int(input('Введите число: '))
# if number % 2 == 0:
#     print('Число четное')
# else:
#     print('Число нечетное')

# 8.Показать четные числа от 1 до N

# N = int(input('Введите число N: '))

# def showN(N):
#     for i in range(1, N + 1):
#         if i % 2 == 0:
#             print(i)

# showN(N)


# 10.Показать вторую цифру трёхзначного числа
# number = int(input('Введите трехзначное число: '))

# def GetSecondDigit(number):
#     return number // 10 % 10

# print(GetSecondDigit(number))

# 12.Удалить вторую цифру трёхзначного числа
# number = int(input('Введите трехзначное число: '))

# def DeleteSecondDigit(number):
#     return number // 100 * 10 + number % 10 

# print(DeleteSecondDigit(number))

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