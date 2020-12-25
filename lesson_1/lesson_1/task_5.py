income = int(input('Введите выручку компании:'))
cost = int(input('Введите траты компании:'))
profit = income - cost
if profit > 0:
    print('Компания работает с прибылью')
    print(f"Рентабельность выручки {profit / income:.2f}")
    worker = int(input('Введите колличество сотрудников в компании'))
    print(f"Прибыль компании на одого сотрудника составляет {profit / worker:.2f}")
elif income == cost:
    print('Компания работает в ноль')
else:
    print('Компания работает в убыток')