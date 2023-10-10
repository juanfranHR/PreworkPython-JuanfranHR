"""Dados dos números, crea una función para encontrar el mínimo común múltiplo
(MCM) de los dos números, que se les pasarán como argumento a la función, y
devuelva el MCM."""


def mcm(a, b):
    divisores_a = []
    divisores_b = []
    for i in range(2, a + 1):
        while a % i == 0:
            divisores_a.append(i)
            a /= i
    for j in range(2, b + 1):
        while b % j == 0:
            divisores_b.append(j)
            b /= j

    factores = list(set(divisores_a) | set(divisores_b))
    mcm = 1
    for factor in factores:
        if divisores_a.count(factor) >= divisores_b.count(factor):
            mcm *= factor ** divisores_a.count(factor)
        else:
            mcm *= factor ** divisores_b.count(factor)

    return mcm
