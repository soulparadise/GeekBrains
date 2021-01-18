with open('task_6.txt', encoding='utf-8') as f_obj:
    my_line = f_obj.readlines()


my_dict = dict()
for line in my_line:
    split_line = line.split()
    discipline = split_line[0]
    a = 0
    for x in split_line[1:]:
        if '(' in x:
            a = a + int(x[:x.find('(')])
    print(a)
    my_dict[discipline[:-1]] = a
print(my_dict)


