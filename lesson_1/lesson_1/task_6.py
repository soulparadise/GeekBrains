a = int(input('Результат первого дня'))
b = int(input('Желаемый результат'))
day = 1
while True:
    day = day + 1
    a = a + a * 0.1
    if a >= b:
        print(f"На {day} день спортсмен достиг результата - не менее {b} км")
        break

