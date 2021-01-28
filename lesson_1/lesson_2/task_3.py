mount_list = ['Зима', 'Весна', 'Лето', 'Осень']
mount_number = int(input('Введите номер месяца'))
mount_dict = {1: 'Invierno', 2: 'Primavera', 3: 'Verano', 4: 'Otoño'}
if 1 <= mount_number <= 12:
    if 3 <= mount_number <= 5:
        print(mount_list[1])
        print(mount_dict.get(2))
    elif 6 <= mount_number <= 8:
        print(mount_list[2])
        print(mount_dict.get(3))
    elif 9 <= mount_number <= 11:
        print(mount_list[3])
        print(mount_dict.get(4))
    else:
        print(mount_list[0])
        print(mount_dict.get(1))
else:
    print('Вы ввели неправильное значение')
