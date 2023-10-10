"""Define una función que reciba un número y retorne la suma de sus
dígitos al cubo."""


def digitosCubo(num):
    return sum(int(i) ** 3 for i in str(num))
