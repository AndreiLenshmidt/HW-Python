# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

rand_list = [12,'sadf',5643]

list1 = list(filter(lambda x: type(x) == int ,rand_list))
print(list1)

list2 = list(filter(lambda x: type(x) == str ,rand_list))
print(list2)

