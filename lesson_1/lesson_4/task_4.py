my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [my_list[el] for el in range(0, len(my_list)) if my_list.count(my_list[el]) < 2]
print(new_list)
