"""Define una función que tome un número y retorne un diccionario con
la tabla de multiplicar de ese número del 1 al 10."""


def tabla_dict(num):
    return {
        "1": num * 1,
        "2": num * 2,
        "3": num * 3,
        "4": num * 4,
        "5": num * 5,
        "6": num * 6,
        "7": num * 7,
        "8": num * 8,
        "9": num * 9,
        "10": num * 10,
    }


print(tabla_dict(5))
