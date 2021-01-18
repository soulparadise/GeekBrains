from itertools import count, cycle

a, b = int(input('Введите начальное число итератора')), int(input('Введите конечное число итератора'))
for el in count(a):
    if el > b:
        break
    else:
        print(el)

my_list = list(input('Введите слово для записи в строку'))
count_stop = int(input('Введите колличество повторений строки'))
print(my_list)
c = 0
for el in cycle(my_list):
    if c > (len(my_list) * count_stop) - 1:
        break
    print(el)
    c += 1
