def my_func(a, b, c):
    return a + b + c - min(a, b, c)


first_number = int(input('Введите первое число'))
second_number = int(input('Введите второе число'))
third_number = int(input('Введите третье число'))
print(my_func(first_number, second_number, third_number))




