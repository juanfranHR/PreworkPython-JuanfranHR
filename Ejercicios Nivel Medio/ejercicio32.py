"""Define una función que reciba una cadena y retorne la misma cadena
pero con las palabras en orden inverso."""


def palabras_invertidas(s):
    s_new = ""
    palabras_invertidas = s.split()[::-1]
    for palabra in palabras_invertidas[:-1]:
        s_new += palabra + " "
    return s_new + palabras_invertidas[-1]
