"""Define una función que reciba un número entero n y retorne una lista
con los n primeros números primos."""


def num_primos(n):
    primos = []
    for numero in range(1, n + 1):
        primo = True
        for divisor in range(1, (numero // 2) + 1):
            if numero % divisor == 0:
                primo = False
                break
        if primo == True:
            primos.append(numero)
    return primos
