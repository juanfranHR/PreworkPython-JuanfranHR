"""Define una función que reciba un número entero y retorne True si es
un número primo, de lo contrario retorne False."""


def is_primo(num):
    primo = True
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            primo = False
            break
    return primo
