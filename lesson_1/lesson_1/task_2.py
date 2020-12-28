while True:
    quantity_sec = input('Введите колличество секунд:')
    try:
        quantity_sec = int(quantity_sec)
        hour = quantity_sec // 3600
        minute = quantity_sec // 60 - hour * 60
        second = quantity_sec % 60
        print(f"{hour}:{minute}:{second}")
        break
    except:
        print('Вы ввели не числовое значение.')
