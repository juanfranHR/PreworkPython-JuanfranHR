"""Define una función que utilice un bucle para imprimir los primeros n
números de la serie de Fibonacci."""


def fibonacci(n):
    fibonacci = [0, 1]
    for i in range(2, n + 1):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    return fibonacci[-1]
