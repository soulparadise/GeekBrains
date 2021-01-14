with open('task_2.txt', 'w', encoding='utf-8') as f_obj:
    while True:
        a = input('Please enter data for write to file')
        f_obj.write(a + '\n')
        if a == '':
            break
