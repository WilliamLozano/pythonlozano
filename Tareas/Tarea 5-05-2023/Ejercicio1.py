import random
import statistics

# Función para generar un arreglo de n elementos con números generados aleatoriamente
def generar_arreglo(n):
    arreglo = []
    for _ in range(n):
        arreglo.append(random.randint(1, 100))  # Genera números aleatorios entre 1 y 100
    return arreglo

# Función para imprimir el arreglo original
def imprimir_arreglo(arreglo):
    print("Arreglo original:", arreglo)

# Función para calcular la suma de los elementos del arreglo
def calcular_suma(arreglo):
    suma = sum(arreglo)
    print("Suma:", suma)

# Función para calcular el promedio de los elementos del arreglo
def calcular_promedio(arreglo):
    promedio = sum(arreglo) / len(arreglo)
    print("Promedio:", promedio)

# Función para encontrar el valor máximo en el arreglo
def encontrar_mayor(arreglo):
    mayor = max(arreglo)
    print("Mayor:", mayor)

# Función para encontrar el valor mínimo en el arreglo
def encontrar_menor(arreglo):
    menor = min(arreglo)
    print("Menor:", menor)

# Función para ordenar el arreglo en orden ascendente
def ordenar_ascendente(arreglo):
    arreglo_ordenado = sorted(arreglo)
    print("Arreglo ordenado ascendente:", arreglo_ordenado)

# Función para ordenar el arreglo en orden descendente
def ordenar_descendente(arreglo):
    arreglo_ordenado = sorted(arreglo, reverse=True)
    print("Arreglo ordenado descendente:", arreglo_ordenado)

# Función para encontrar la moda en el arreglo
def encontrar_moda(arreglo):
    moda = statistics.mode(arreglo)
    print("Moda:", moda)

# Función para encontrar la mediana en el arreglo
def encontrar_mediana(arreglo):
    mediana = statistics.median(arreglo)
    print("Mediana:", mediana)

# Función para buscar un número en el arreglo
def buscar_numero(arreglo, numero):
    posiciones = []
    conteo = 0
    for i, num in enumerate(arreglo):
        if num == numero:
            posiciones.append(i)
            conteo += 1
    if posiciones:
        print("El número", numero, "se encuentra en las posiciones:", posiciones)
        print("Número de ocurrencias:", conteo)
    else:
        print("El número", numero, "no se encuentra en el arreglo.")

# Función para mostrar el menú y manejar las opciones
def mostrar_menu(arreglo):
    opcion = ""
    while opcion != "k":
        print("\n--- Menú ---")
        print("a. Imprimir arreglo original")
        print("b. Suma")
        print("c. Promedio")
        print("d. Mayor")
        print("e. Menor")
        print("f. Ordenar ascendente")
        print("g. Ordenar descendente")
        print("h. Moda")
        print("i. Mediana")
        print("j. Buscar")
        print("k. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "a":
            imprimir_arreglo(arreglo)
        elif opcion == "b":
            calcular_suma(arreglo)
        elif opcion == "c":
            calcular_promedio(arreglo)
        elif opcion == "d":
            encontrar_mayor(arreglo)
        elif opcion == "e":
            encontrar_menor(arreglo)
        elif opcion == "f":
            ordenar_ascendente(arreglo)
        elif opcion == "g":
            ordenar_descendente(arreglo)
        elif opcion == "h":
            encontrar_moda(arreglo)
        elif opcion == "i":
            encontrar_mediana(arreglo)
        elif opcion == "j":
            numero = int(input("Ingresa el número que deseas buscar: "))
            buscar_numero(arreglo, numero)
        elif opcion == "k":
            print("Saliendo del programa...")
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

# Función principal
def main():
    n = int(input("Ingrese la cantidad de elementos del arreglo: "))
    arreglo = generar_arreglo(n)

    mostrar_menu(arreglo)

if __name__ == "__main__":
    main()