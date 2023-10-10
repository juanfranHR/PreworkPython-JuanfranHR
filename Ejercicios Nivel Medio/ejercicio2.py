"""Ejercicio: Define una función que tome un número y retorne una lista de sus
divisores."""


def divisores(num):
    divisores = [1]
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            divisores.append(i)
    divisores.append(num)
    return divisores
