"""Ejercicio: Define una función que reciba una lista de palabras y un entero n, y
retorne la lista de palabras que son más largas que n."""


def palabras_largas(lista_palabras, n):
    return [palabra for palabra in lista_palabras if len(palabra) > n]
