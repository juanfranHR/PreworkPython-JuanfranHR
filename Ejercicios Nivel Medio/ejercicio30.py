"""Define una función que reciba una lista de cadenas y retorne la
cadena más larga en la lista."""


def cadena_larga(lista):
    maxima = ""
    for i in lista:
        if len(i) > len(maxima):
            maxima = i
    return maxima
