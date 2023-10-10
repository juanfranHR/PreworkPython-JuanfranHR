"""Crea una función que, dado un número, verifique si un número es primo."""


def is_primo(num):
    for i in range(2, (num // 2) + 1):
        if num % i == 0 and num != 2:
            return False
            break
    return True
