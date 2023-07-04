import random

def llenar_arreglo(n):
    arreglo = []
    numero_anterior = random.randint(1, 10)  # Generar el primer número aleatorio entre 1 y 10

    for _ in range(n):
        siguiente_decena = (numero_anterior // 10 + 1) * 10  # Calcular la siguiente decena
        num = random.randint(numero_anterior, siguiente_decena - 1)  # Generar un número aleatorio entre el número anterior y la siguiente decena - 1

        arreglo.append(num)
        numero_anterior = num

    return arreglo

# Pedir al usuario la cantidad de elementos para el arreglo
n = int(input("Ingrese la cantidad de elementos para el arreglo: "))

# Llenar el arreglo con números aleatorios según las restricciones
arreglo = llenar_arreglo(n)

# Imprimir el arreglo resultante
print(arreglo)
