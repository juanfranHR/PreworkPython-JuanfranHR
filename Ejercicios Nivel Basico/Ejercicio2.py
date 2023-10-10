"""Crea una función a la que pases un número como argumento, calcule el factorial
de ese número y haga print del resultado."""


def factorial(num):
    total = 1
    while num > 0:
        total *= num
        num -= 1
    print(total)
