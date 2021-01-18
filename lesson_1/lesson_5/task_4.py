from typing import List

ru_numeral = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
result_list = []
with open('task_4.txt', encoding='utf-8') as f_obj:
    for element in f_obj:
        numeral = element.split(' - ')
        print(numeral)
        if numeral[0] in ru_numeral:
            new_numeral = ru_numeral[numeral[0]]
            result_list.append(new_numeral + ' - ' + numeral[1])
print(result_list)

with open('task_4_result.txt', 'w', encoding='utf-8') as new_f_obj:
    new_f_obj.writelines(result_list)





