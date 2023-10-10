"""Escribe una función que reciba una lista de tuplas y retorne una lista
ordenada basada en el último elemento de cada tupla."""


def tuplas_ordered(lista):
    ordered = []
    tuple_aux = (0, 0)
    while len(lista) > 0:
        minimo = 999999999999
        print("Estoy aqui")
        for tuple in lista:
            if tuple[1] < minimo:
                minimo = tuple[1]
                tuple_aux = tuple
        ordered.append(tuple_aux)
        lista.remove(tuple_aux)
    return ordered
