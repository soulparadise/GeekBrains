with open('task_3.txt', encoding='utf-8') as f_obj:
    a = 0
    print('Список людей имеющих доходо больше 20.000:')
    for worker in f_obj.readlines():
        last_name, salary = worker.split()
        if float(salary) >= 20000:
            print(last_name, salary)
        a = a + float(salary)
        f_obj.seek(0)
    print(f'Средняя величина дохода всех сотрудников равна: {int(a / int(len(f_obj.readlines())))}')
