import re

def sring_to_list(expression):
    list_num = re.split(r"[-+*/]", expression)

    ex_list = list(filter(lambda x: x == '+' or x == "-" or x == "*" or x == "/", expression))
    ex_list.append('=')

    res_list = []

    for i in range(0, len(list_num)):
        res_list.append(list_num[i])
        res_list.append(ex_list[i])

    return res_list

