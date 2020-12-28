def division(dividend, divider):
    if divider == 0:
        print('Деление на ноль')
    else:
        return dividend / divider


dividend = int(input('Введите первое число'))
divider = int(input('Введите второе число'))
print(f"Результат деления равен {division(dividend, divider)}")
