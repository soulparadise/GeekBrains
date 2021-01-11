from functools import reduce

new_list = [el for el in range(100, 1001) if el % 2 == 0]
print(new_list)
print(reduce(lambda a, b: a * b, new_list))
