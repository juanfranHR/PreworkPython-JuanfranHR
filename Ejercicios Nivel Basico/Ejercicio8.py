"""Crea una función que, dado un número, verifique si un número es positivo,
negativo o cero."""


def tipo_numero(numero):
    if numero > 0:
        print("El número es positivo")
    elif numero < 0:
        print("El número es negativo")
    else:
        print("El número es 0")
