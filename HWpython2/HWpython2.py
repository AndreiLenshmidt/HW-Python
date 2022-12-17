# Задача1 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# number = int(input('Input a number: N = '))
# result = 1

# for i in range(1, number+1):
#     result*=i
#     print(result, end =" ")

# if number<0:
#     print("1 0", end =" ")
#     for i in range(1, -number+1):
#         result*=i
#         print(-result, end =" ")

# Задача2 - Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

# number = int(input('Input a number: N = '))
# divider = 1

# for i in range(2,number):
#     if number%i == 0:
#         print(f'Minimal divider of input number is: {i}')
#         break

# Задача3 - Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.

# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]

# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]

# list_of_index = [2,0,4,4,1]
# new_list = []

# number = int(input('Input a number: N = '))

# for n in range(-number, number+1):
#     new_list.append(n)

# result = 1

# for i in list_of_index:
#     result *= new_list[i]

# print(list_of_index)
# print(new_list)
# print(result)

# Задача4 - Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

# number = int(input('Input a number: N = '))

# sum = 0

# for i in range(0,number+1,2):
#     sum+=i

# print(sum)