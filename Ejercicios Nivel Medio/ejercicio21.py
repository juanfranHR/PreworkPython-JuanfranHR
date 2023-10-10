"""Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene."""


def digitOrChar(s):
    char = 0
    digit = 0
    for c in s:
        if c.isdigit() == True:
            digit += 1
        else:
            char += 1
    return digit, char
