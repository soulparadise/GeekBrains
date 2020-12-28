def my_func(phone, birthday, surname, email, city, name):
    print(name, surname, birthday, city, email, phone)


user_data = {'name': '', 'surname': '', 'birthday': '', 'city': '', 'email': '',
             'phone': ''}
for f in user_data:
    user_data[f] = input(f'{f}: ')
#my_func(name=user_data.get('name'), surname=user_data.get('surname'), birthday=user_data.get('birthday'),
#        city=user_data.get('city'), email=user_data.get('email'), phone=user_data.get('phone'))
my_func(**user_data)
