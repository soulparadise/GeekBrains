with open('task_6.txt', encoding='utf-8') as f_obj:
    for line in f_obj:
         discipline = line.split(':')[0]
         print(discipline)
         hours = line.split('(')
         print(hours)