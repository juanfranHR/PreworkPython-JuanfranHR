"""Define una función que encuentre el elemento más común en una lista."""


def moda_lista(lista):
    ocurrencias = 0
    numero = 0
    for i in set(lista):
        if lista.count(i) > ocurrencias:
            numero = i
            ocurrencias = lista.count(i)
    return numero


print(moda_lista([4, 4, 5, 5, 5, 6, 7, 6, 6, 9, 8, 2, 1, 0, 3, 2, 4]))
