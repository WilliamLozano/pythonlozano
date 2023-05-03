import random

# Generar un número aleatorio entre 1 y 100
numero_a_adivinar = random.randint(1, 100)

while True:
    # Pedir al usuario que ingrese un número
    numero_ingresado = int(input("Adivina el número: "))

    # Verificar si el número ingresado es igual al número a adivinar
    if numero_ingresado == numero_a_adivinar:
        print("¡Felicidades! Adivinaste el número.")
        break

    # Indicar si el número ingresado es mayor o menor que el número a adivinar
    if numero_ingresado < numero_a_adivinar:
        print("El número ingresado es menor que el número a adivinar.")
    else:
        print("El número ingresado es mayor que el número a adivinar.")