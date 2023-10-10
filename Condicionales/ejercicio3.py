"""Ejercicio3. Dado tres números, encuentra y muestra el mayor de ellos."""
numero1 = 18
numero2 = 23
numero3 = 49

if (numero1 > numero2) and (numero1 > numero3):
    print(f"El primer número es el mayor: {numero1}")
elif (numero2 > numero1) and (numero2 > numero3):
    print(f"El segundo número es el mayor: {numero2}")
else:
    print(f"El tercer número es el mayor: {numero3}")
