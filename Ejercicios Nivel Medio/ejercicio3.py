"""Define una función que tome una lista y retorne una nueva lista con
los elementos únicos de la lista original."""


def unicos(lista):
    return [elemento for elemento in lista if lista.count(elemento) == 1]


print(unicos([4, 4, 5, 6, 6, 7, 8, 9, 9, 9, 10, 101, 101, 23, 25, 4, 5, 65]))
