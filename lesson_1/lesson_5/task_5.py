with open('task_5.txt', 'w', encoding='utf-8') as f_obj:
    f_obj.write('123 456 678 432 42 2 4 3 23')

with open('task_5.txt', encoding='utf-8') as new_f_obj:
    number = new_f_obj.readline().split()
    print(sum(map(int, number)))