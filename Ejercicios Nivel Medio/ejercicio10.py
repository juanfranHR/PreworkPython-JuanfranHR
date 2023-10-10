"""Define una función que reciba dos listas y retorne la intersección de
ambas (los elementos que están en las dos listas)."""


def list_intersection(lista1, lista2):
    interseccion = []
    for i in lista1:
        if (i in lista2) and (i not in interseccion):
            interseccion.append(i)
    return interseccion
