
# Задача 1 - Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# day_of_week = int(input("Введите цифру соответсвующего дня недели от 1 до 7. Ваше число: "))

# if day_of_week == 6:
#     print('Да')
# elif day_of_week == 7:
#     print('Да')
# else:
#     print('Нет')

# Задача 2 - (!!!Доп!!!) Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# (0,0,0), (0,0,1) и тд.

# liststr = ['000', '001', '011', '101', '110', '100', '111']

# def Boolstr(x):
#     y = bool(int(x))
#     return y

# check_for_trueth = True

# for i in range(6):
#     x = Boolstr(liststr[i][0])
#     y = Boolstr(liststr[i][1])
#     z = Boolstr(liststr[i][2])
#     expression = not(x and y and z) == (not(x) or not(y) or not(z))
#     print(f'Для X:{x} Y:{y} Z:{z} - expression is {expression}')
#     check_for_trueth *=expression

# if check_for_trueth:
#     print('Утверждение истинно для всех значений XYZ')
# else:
#     print('Утверждение ложно')

# Задача 3 - Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

# x = int(input('Введите координату Х: '))
# y = int(input('Введите координату Y: '))

# if x==0 and y==0:
#     print('Вы ввели точку начала отсчета, введите отличные от 0 значения Х и У')
# elif x>0 and y>0:
#     print('Точка находтся в четверти №1')
# elif x<0 and y>0:
#     print('Точка находтся в четверти №2')
# elif x<0 and y<0:
#     print('Точка находтся в четверти №3')
# else:
#     print('Точка находтся в четверти №4')

# Задача 4 - Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# i = 0
# number = 5

# while (number>4 and i<5):
#     number = int(input('Введите номер четверти №:'))
#     print('Вы ввели неправильный номер четверти, введите число от 1 до 4')
#     i+=1

# if number==1:
#     print('X ∈ (0, ∞), Y ∈ (0, ∞)')
# elif number==2:
#     print('X ∈ (-∞, 0), Y ∈ (0, ∞)')
# elif number==3:
#     print('X ∈ (-∞, 0), Y ∈ (-∞, 0)')
# elif number==4:
#     print('X ∈ (0, ∞), Y ∈ (-∞, 0)')
# else:
#     print('Вы ввели неправильный номер четверти, введите число от 1 до 4')

# Задача 5 - Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# x1 = int(input('Введите координату X1: '))
# y1 = int(input('Введите координату Y1: '))
# x2 = int(input('Введите координату X2: '))
# y2 = int(input('Введите координату Y2: '))

# distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
# print(distance)
