# Задача 1 - Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, сколько указал пользователь(БЕЗ round())


# n = int(input('Введите число знаков после запятой от 1 до 100, n = '))
# pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
# print(pi[0:n+2])


# Задача 2 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 6 | N = 12 | 32 | 13 | 9 | 18 | 21
# 2 * 3 | 2 * 2 * 3 | 2 * 2 * 2 * 2 * 2 | 13 | 3 * 3 | 2 * 3 * 3 | 3*7


# num = int(input('Input a number '))
# prime_divisor = []

# for i in range(2,num+1):
#     while num%i == 0:
#         prime_divisor.append(i)
#         num = num//i

# for i in prime_divisor:
#     print(i, end='*')
# print(1)

# Задача 3 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод:
# 3 1 2 3
# Вывод:
# 2 1


# item_list = [1,2,3,1,2,4,'a', 14, 'red', 'a', 'b']
# new_list = []

# for i in range(len(item_list)-1):
#     for j in range(i+1,len(item_list)-1):
#         if item_list[i] == item_list[j]:
#             new_list.append(item_list[i])
           
# new_list = set(item_list).difference(set(new_list))

# print(item_list)
# print(new_list)


# Задача 4 - Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 

# k = 6
#     ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h

#     a, b, c, d, e, h - рандом


# import random

# def Random_polinomial(pow):
#     polinominal = ''
#     for i in range(pow, 1, -1):
#         polinominal += str(random.randint(0,100))+'*x^'+ str(i) + '+'
#     polinominal += str(random.randint(0,100))+'*x'+'+'+str(random.randint(0,100))
#     return polinominal

# pow = int(input('Input your pow '))
# print(Random_polinomial(pow))

