with open('task_2.txt', encoding='utf-8') as f_obj:
    print(f'В файле содержится {len(f_obj.readlines())} строк')
    f_obj.seek(0)
    for number, line in enumerate(f_obj.readlines(), 1):
        print(line.strip())
        print(f'В строке номер {number} - {len(line.split())} слов \n')
