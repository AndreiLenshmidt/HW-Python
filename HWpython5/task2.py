# 2) Создайте программу для игры в ""Крестики-нолики"" человек vs человек.

# 1 | 2 | X
# 4 | X | O
# X | 8 | O

def game_logic(numbers_list):
    pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9 = numbers_list
    if pos1 == pos2 == pos3:
        return True
    elif pos4 == pos5 == pos6:
        return True
    elif pos7 == pos8 == pos9:
        return True
    elif pos1 == pos4 == pos7:
        return True
    elif pos2 == pos5 == pos8:
        return True
    elif pos3 == pos6 == pos9:
        return True
    elif pos1 == pos5 == pos9:
        return True
    elif pos3 == pos5 == pos7:
        return True
    elif type(pos1) and type(pos2) and type(pos3) and type(pos4) and type(pos5) and type(pos6) and type(pos7) and type(pos8) and type(pos9) == str:
        return 2
    else:
        return False

def draw_game_pole(numbers_list):
    print(f'  {numbers_list[0]}  |  {numbers_list[1]}  |  {numbers_list[2]}')
    print('-----------------')
    print(f'  {numbers_list[3]}  |  {numbers_list[4]}  |  {numbers_list[5]}')
    print('-----------------')
    print(f'  {numbers_list[6]}  |  {numbers_list[7]}  |  {numbers_list[8]}')
    return '-------------------------'

numbers_list = [i for i in range(1,10)]

game_over = False
print('')

print(draw_game_pole(numbers_list))

while True:

    print('')

    pos = int(input('Введите позицию для X:'))
       
    numbers_list[pos-1] = 'X'
    print('')
    print(draw_game_pole(numbers_list))
    
    game_over = game_logic(numbers_list)
    if game_over == True:
        print('')
        print('Побели Х')
        break
    elif game_over == 2:
        print('')
        print('Ничья')
        break

    print('')
    pos = int(input('Введите позицию для O:'))
    print('')
   
    print(draw_game_pole(numbers_list))
    numbers_list[pos-1] = 'O'

    game_over = game_logic(numbers_list)
    if game_over == True:
        print('')
        print('Побели О')
        break






