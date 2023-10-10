"""Define una función que reciba una lista de números y retorne el
segundo número más grande de la lista."""


def segundon(lista):
    return sorted(lista, reverse=True)[1]
