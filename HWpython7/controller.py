from ui import add_in_book, ask_for_user, show_book
from logger import read_book, write_book, write_book_format2

path1 = 'D:/Прогучение/HW-Python/HWpython7/book.txt'
path2 = 'D:/Прогучение/HW-Python/HWpython7/book2.txt'

def run_note_book():
    comand = ask_for_user()
    while True:
        if comand == 1:
            a = read_book(path2)
            show_book(a)
            comand = ask_for_user()
        elif comand == 2:
            data = add_in_book()
            write_book(data)
            write_book_format2(data)
            comand = ask_for_user()
        else:
            break

            
