def ask_for_user():
    print('')
    user_choise = int(input('Введите 1 для вывода данных\nВведите 2 для добавление данных\nВведите число > 3 для выхода\n'))
    return user_choise

def show_book(data):
    print('')
    print(data)

def add_in_book():
    your_data = ['', '', '', '']
    your_data[0] = input('Фамилия: ')
    your_data[1] = input('Имя: ')
    your_data[2] = input('Телефон: ')
    your_data[3] = input('Описание: ')
    return your_data

