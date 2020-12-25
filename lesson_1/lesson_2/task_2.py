quantity_el = int(input('Введите колличество элементов для списка'))
i = 0
user_list = []
while i < quantity_el:
    user_list.append(input(f"Введите {i + 1} элемент списка"))
    i += 1
print(user_list)
el = 0
for element in range(int(len(user_list)/2)):
    user_list[el], user_list[el + 1] = user_list[el +1], user_list[el]
    el += 2
print(user_list)


