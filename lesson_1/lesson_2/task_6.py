item_list = []
i = 1
while True:
    user_answer = input("Для добавления нового товара введите: добавить. Для завершения программы введите: выход. Для "
                        "вывода аналитики введите: аналитика").lower()
    if user_answer == 'выход':
        print('Программа завершена')
        break
    elif user_answer == 'добавить':
        name_item = input('Введите название добавляемого товара')
        price_item = input('Введите цену для нового товара')
        value_item = input('Введите колличество товара на складе')
        unit_item = input('Введите еденицу измерения товара')
        item_dict = dict(название=name_item, цена=price_item, колличество=value_item, ед=unit_item)
        item_tuple = (i, item_dict)
        item_list.append(item_tuple)
        i += 1
    elif user_answer == 'аналитика':
        name = []
        price = []
        value = []
        unit = []
        for el in item_list:
            name.append(el[1].get('название'))
            price.append(el[1].get('цена'))
            value.append(el[1].get('колличество'))
            unit.append(el[1].get('ед'))
        analitics = dict(название=name, цена=price, колличество=value, ед=value)
        for element in analitics:
            print(element, analitics[element])






