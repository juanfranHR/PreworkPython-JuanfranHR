"""Dados dos números, crea una función para encontrar el máximo común divisor
(MCD) de esos dos números."""


def mcd(num1, num2):
    minimo = 0
    if num1 <= num2:
        minimo = num1
    else:
        minimo = num2
    for divisor in range(minimo, 1, -1):
        if num1 % divisor == 0 and num2 % divisor == 0:
            return divisor
        else:
            return 0


print(mcd(23, 46))
