user_list = (input('Введите строку из нескольки слов разделенных пробелом').split())
print(user_list)
for ind, el in enumerate(user_list):
    print(ind + 1, el[:10])
