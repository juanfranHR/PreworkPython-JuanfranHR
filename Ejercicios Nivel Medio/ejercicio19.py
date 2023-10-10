"""Define una función que tome dos listas y retorne True si tienen al
menos un miembro en común, de lo contrario, retorne False."""


def algo_comun(lista1, lista2):
    comun = False
    for i in lista1:
        if i in lista2:
            comun = True
            break
    return comun
