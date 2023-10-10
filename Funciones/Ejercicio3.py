"""Ejercicio3. Define una función que tome un número y determine si es primo."""


def es_primo(num):
    primo = True
    for divisor in range(2, num):
        if (num % divisor == 0) and ((num != 1) and (num != 2)):
            primo = False
            break
    return primo
