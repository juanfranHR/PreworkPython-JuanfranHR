"""Define una función que tome una cadena y cuente el número de
vocales en la cadena."""


def num_vocales(s):
    vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    return len([letra for letra in s if letra in vocales])
