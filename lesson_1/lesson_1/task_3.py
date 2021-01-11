while True:
    n = input('Введите число')
    try:
        tmp = int(n)
        print(int(n) + int(n+n) + int(n+n+n))
        break
    except:
        print('Вы ввели не число. Повторите ввод')
