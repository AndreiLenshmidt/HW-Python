# 1) Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
# [1,2,3,4,22,234,24] ----> [22, 24]

list_num = list(map(int, input('Введите несколько чисел через пробел: ').split()))
print(list_num)

list_num = list(filter(lambda x: x < 100 and x > 9, list_num))
print(list_num)