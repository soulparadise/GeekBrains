a = 10
print(a, type(a))
b = 'Строка'
print(b, type(b))
c = 5.25
print(c, type(c))
d = True
print(d, type(d))

while True:
    a = input('Введите целое число для переменной a:')
    try:
        a = int(a)
        print('Вы ввели:', a)
        break
    except:
        print('Вы ввели не числовое значение.')

b = input('Введите даныые для переменной b:')
print('Вы ввели:', b)
print('Программа завершена. До свидания.')


