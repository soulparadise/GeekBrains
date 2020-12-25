i = int(input('Введите целое положительное число'))
n = 0
while i > 1:
    a = i % 10
    i = i // 10
    if a > n:
        n = a
print(n)


