import random

def llenar_arreglo(n):
    arreglo = []
    numeros_existentes = set()

    while len(arreglo) < n:
        num = random.randint(1, 100)  # Generar un número aleatorio entre 1 y 100

        if num not in numeros_existentes:
            arreglo.append(num)
            numeros_existentes.add(num)
        else:
            print(f"El número {num} ya está en el arreglo")

    return arreglo

# Pedir al usuario la cantidad de elementos para el arreglo
n = int(input("Ingrese la cantidad de elementos para el arreglo: "))

# Llenar el arreglo con números aleatorios sin repeticiones
arreglo = llenar_arreglo(n)

# Imprimir el arreglo resultante
print(arreglo)
