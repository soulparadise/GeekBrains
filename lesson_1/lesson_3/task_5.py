def my_func(arg):
    user_list_int = map(int, arg)
    func_sum = 0
    for i in user_list_int:
        func_sum = func_sum + i
    return func_sum


answer_sum = 0
while True:
    user_data = input('Введите последовательность чисел для сложения. Для выхода из программы введите q').lower()
    user_list = list(user_data.split())
    if 'q' in user_list:
        user_list.remove('q')
        answer_sum = answer_sum + my_func(user_list)
        user_list.clear()
        print(f'Программа завершена. Сумма введеных чисел равна: {answer_sum}')
        break
    else:
        answer_sum = answer_sum + my_func(user_list)
        user_list.clear()
        print(f'Сумма введеных чисел равна: {answer_sum}')
