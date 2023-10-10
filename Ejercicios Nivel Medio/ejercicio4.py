"""Define una función que tome un número y retorne la suma de sus
dígitos."""


def suma_digitos(num):
    return sum([int(cifra) for cifra in str(num)])
