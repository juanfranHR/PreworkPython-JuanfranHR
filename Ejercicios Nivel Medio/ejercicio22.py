"""Define una función que reciba una lista de números y retorne la
suma acumulada de los números"""


def suma_acumulada(lista):
    return [sum(lista[:elemento]) for elemento in lista]
