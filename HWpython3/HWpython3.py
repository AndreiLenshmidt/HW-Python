# Задача 1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.


# numbers_list = [2, 12, 0, 4, 5, 21, 8, 15, 17]
# sum = 0
# for i in range(1,len(numbers_list),2):
#     sum += numbers_list[i]

# print(sum)


# задача 2 - Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.


# numbers_list = [2, 12, 0, 4, 5, 21, 8, 15, 17]

# i = 0; j = len(numbers_list)-1
# while (i < len(numbers_list)/2):
#     multiply = numbers_list[i]*numbers_list[j]
#     print(multiply, end=' ')
#     i+=1; j-=1


# Задача 3 - Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


# max = 0.0; min = 0.9999999999
# float_list = [0.199, 102.01, 1.79, 35.404, 2.999, 3.0]

# for i in range(len(float_list)):
#     if float_list[i]%1>max:
#         max = float_list[i]%1
#     if float_list[i]%1<min:
#         min = float_list[1]%1

# print(round(max-min, 4))


# Задача 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.


# num = int(input('Input a number '))
# temp = num
# bin_num = ''

# while temp != 0:
#     bin_num += str(temp%2)
#     temp = temp//2

# bin_num = int(bin_num[::-1])

# print(bin_num)


# Задача 5 - Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


# def Fibonacci(num):
#     if num == 1:
#         return 0
#     elif num in [2,3]:
#         return 1
#     else:
#         return Fibonacci(num-1) + Fibonacci(num-2)

# def Negative_fibonacci(num):
#     if num == 1:
#         return 0
#     elif num == 2:
#         return 1
#     elif num == 3:
#         return -1
#     else:
#         return Negative_fibonacci(num-2) - Negative_fibonacci(num-1)

# n = int(input('Input a Fibonacci number '))
# list_fib = []

# for i in range(-n-1, 0):
#     list_fib.append(Negative_fibonacci(-i))
    
# for i in range(2, n+2):
#     list_fib.append(Fibonacci(i))

# print(list_fib)