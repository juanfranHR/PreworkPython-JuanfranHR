"""Define una función que reciba una cadena y retorne la cantidad de
letras vocales en la cadena."""


def num_vocales(s):
    return sum(
        [s.count(letra) for letra in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]]
    )
