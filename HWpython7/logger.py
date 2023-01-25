def read_book(path):
    with open(path, 'r') as file:
        data = file.read()
    if data == '':
        data = 'Файл пустой'
    return data        


def write_book(data):
    surname = 'Фамилия: ' + data[0] + '\n'
    name = 'Имя: ' + data[1] + '\n'
    phone = 'Телефон: ' + data[2] + '\n'
    discription = 'Описание: ' + data[3] + '\n'
    path = 'D:/Прогучение/HW-Python/HWpython7/book.txt'
    with open(path, 'a') as file:
        file.write(surname)
        file.write(name)
        file.write(phone)
        file.write(discription)
    
def write_book_format2(data):

    format2 = 'Фамилия: ' + data[0] + ', ' +'Имя: ' + data[1] + ', ' + 'Телефон: ' + data[0] + ', ' + 'Описание: ' + data[3] + '\n'
    path = 'D:/Прогучение/HW-Python/HWpython7/book2.txt'
    with open(path, 'a') as file:
        file.write(format2)

