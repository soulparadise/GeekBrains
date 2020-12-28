def my_func(x, y):
    return x ** abs(y)


def my_function(x, y):
    a = x
    for f in range(1, abs(y)):
        a = a * x
    return a


print(my_func(7, -18))
print(my_function(7, -18))
