# 3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input('Введите число: N = ')

list_number = [i for i in number]
list_number = list(filter(lambda x: x != '-' and x !=',', list_number))
list_number = list(map(int, list_number))

sum = 0
for i in list_number:
    sum +=i
print(f'Сумма цифр введенного числа равна: {sum}')
