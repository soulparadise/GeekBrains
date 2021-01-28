import math


def factorial_func(n):
    yield math.factorial(n)


for el in factorial_func(5):
    print(el)
