"""Crea una función que, dado un número, sume los dígitos de ese número y
devuelva el resultado."""


def suma_digitos(num):
    return sum([int(digito) for digito in str(num)])
