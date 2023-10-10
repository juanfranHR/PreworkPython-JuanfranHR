"""Define una función que tome dos listas y retorne la lista de
elementos que no están en ambas listas."""


def noInterseccion(lista1, lista2):
    if lista1 >= lista2:
        return [element for element in lista1 if element not in lista2]
    else:
        return [element for element in lista2 if element not in lista1]
