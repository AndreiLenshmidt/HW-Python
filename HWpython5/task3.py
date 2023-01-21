# 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb"
# stroka = "3a4b2c3b"

# Вывод: stroka = "aaabbbbccbbb"


def string_to_rle(string):
    rle_stroka = ''
    while string != '':
        count = 1
        for i in range(0, len(string)-1):
            if string[i] == string[i+1]:
                count +=1
            else:
                break
        simbol = string[count-1:count]
        rle_stroka = rle_stroka + str(count)+simbol
        string = string[count:]

    return rle_stroka

def rle_to_string(rle_stroka):
    string = ''
    while rle_stroka != '':
        count = 1
        number = int(rle_stroka[count-1])
        simbol = rle_stroka[count]
        string = string + str(number*simbol)
        count+=1
        rle_stroka = rle_stroka[count:]
        
    return string

stroka = input('Введите любую строку: ')
print(stroka)

rle_string = string_to_rle(stroka)
print(rle_string)

any_string = rle_to_string(rle_string)
print(any_string)

