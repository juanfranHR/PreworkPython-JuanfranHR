"""Define una función que tome una lista de números y retorne el
número más grande de la lista."""


##Tres versiones
def maximo(lista):
    max = -1000
    for i in lista:
        if i > max:
            max = i
    return max


def maximo2(lista):
    return sorted(lista, reverse=True)[0]


def maximo3(lista):
    return max(lista)
