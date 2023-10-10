"""Define una función que tome una cadena y retorne un diccionario
con la cantidad de apariciones de cada caracter en la cadena."""


def ocurrencias_dict(s):
    return {c: s.count(c) for c in set(s)}
