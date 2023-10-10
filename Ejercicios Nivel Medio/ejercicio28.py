"""Define una función que reciba un número entero positivo y retorne la
suma de los cuadrados de todos los números pares menores o iguales a ese
número."""


def suma_cuadrados(num):
    return sum([numero**2 for numero in range(num + 1) if numero % 2 == 0])
