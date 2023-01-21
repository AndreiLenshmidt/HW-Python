# Задача1 - Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

# 120 21 ---> 99 бот 4 -> 95 .... бот --->29 --> 27 >> 2конф

# a) Добавьте игру против бота

# Доп b) Подумайте как наделить бота ""интеллектом"" (Теория игр)

print('На столе лежит 120 конфета. Играют два игрока делая ход друг после друга. Первый ход делает человек. За один ход можно забрать не более чем 28 конфет, но не менее 1. Победитель - тот, кто забирает со стола последние конфеты')

import random

def pc_random_logic():
    return random.randint(1, 28)

def pc_loose_logic(sum):
    if sum <= 114 and sum > 87:
        return sum - 87
    if sum == 87:
        return 1
    elif sum < 87:
        return sum - 58

def pc_start_logic(sum):
    if sum == 119:
        return 3
    elif sum == 118:
        return 2
    elif sum == 117:
        return 1
    elif sum == 116:
        return pc_random_logic() # - pc loose
    elif sum <= 115:
        return 33 - (120 - sum)

def pc_main_logic(human, sum):
    if sum <= 87 and sum >= 59:
        return 29 - human
    elif sum <= 58 and sum >= 29:
        return 29 - human
    elif sum < 29:
        return sum

def amount_candy_test(amount):
    if (amount > 28):
        amount == 28
        print(f'Вы не можете взять больше 28 конфет, будем считать что вы взяли 28 конфет')
        return 28
    elif (amount < 1):
        print(f'Вы не можете взять меньше 1 конфет, будем считать что вы взяли 1 конфет')
        return 1
    else:
        return amount

sum = 120
count = 1

while sum >= 115:
    print('-----------------------')
    human = int(input(f'Ход №{count}, ваш ход. Возьмите от 1 до 28 конфет: '))
    human = amount_candy_test(human)
    sum = sum - human
    print(f'Осталось {sum} конфет')
    computer = pc_start_logic(sum)
    print(f'Ход №{count}, ПК ходит. Компьютер взял: {computer} конфет')
    sum = sum - computer
    print(f'Осталось {sum} конфет')
    count +=1

while sum <= 114 and sum > 87:
    print('-----------------------')
    human = int(input(f'Ход №{count}, ваш ход. Возьмите от 1 до 28 конфет: '))
    human = amount_candy_test(human)
    sum = sum - human
    print(f'Осталось {sum} конфет')
    computer = pc_loose_logic(sum)
    print(f'Ход №{count}, ПК ходит. Компьютер взял: {computer} конфет')
    sum = sum - computer
    print(f'Осталось {sum} конфет')
    count +=1

while sum <= 87 and sum > 0:
    print('-----------------------')
    human = int(input(f'Ход №{count}, ваш ход. Возьмите от 1 до 28 конфет: '))
    human = amount_candy_test(human)
    sum = sum - human
    print(f'Осталось {sum} конфет')
    computer = pc_main_logic(human, sum)
    print(f'Ход №{count}, ПК ходит. Компьютер взял: {computer} конфет')
    sum = sum - computer
    print(f'Осталось {sum} конфет')
    count +=1

if sum == 0:
    print('-----------------------')
    print('Копьютер победил')
if sum < 0:
    print('-----------------------')
    print('Вы победили!!!')