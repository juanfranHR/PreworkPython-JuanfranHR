"""Ejercicio2. Defineuna función que tome un número y retorne su factorial."""


def factorial(num):
    factorial = 1
    while num > 0:
        factorial *= num
        num -= 1
    return factorial
