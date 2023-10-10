"""Define una función que tome un número y calcule su serie de
Fibonacci."""


def fibonacci(num):
    fibonacci = [0, 1]
    for i in range(2, num + 1):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    return fibonacci[-1]
