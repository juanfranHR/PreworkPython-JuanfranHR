"""Define una función que tome una cadena y retorne la cantidad de
letras mayúsculas y minúsculas en la cadena."""


# Usamos la tabla ASCII para que sólo tenga en cuenta unicamente las letras. Si aparecen otros caracteres en el string no se contabilizan
def minusMayus(s):
    minus = 0
    mayus = 0
    for c in s:
        if ord(c) >= 97 and ord(c) <= 122:
            minus += 1
        elif ord(c) >= 65 and ord(c) <= 90:
            mayus += 1
    return minus, mayus
