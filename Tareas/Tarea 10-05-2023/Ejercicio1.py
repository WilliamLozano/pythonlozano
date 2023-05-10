#1. Llenar un arreglo de n elementos con números generados con la función random. N es
#ingresado por el usuario. Diseñe un menú con las siguientes operaciones.
#a. Imprimir arreglo original (El primero que se generó)
#b. Suma
#c. Promedio
#d. Mayor
#e. Menor
#f. Ordenar ascendente (No perder el arreglo original; el del punto a)
#g. Ordenar descendente (No perder el arreglo original; el del punto a)
#h. Moda
#i. Mediana
#j. Buscar. Decir si encuentra el número, en qué posición(es) está, cuantas veces está

import random
import statistics
import math

#Funcion para generar una lista con numeros entre 1 a 100

def generar_lista(n):
    lista = []
    for _ in range(n):
        lista.append(random.randint(1,100))
    return lista

def lista_original(lista):
    print(f"Lista Original : {lista}")

def Calcular_suma(lista):
    Suma = sum(lista)
    print(f"Suma de la lista : {Suma}")

def Calcular_promedio(lista):
    Promedio = sum(lista) / len(lista)
    print(f"Promedio de la lista: {Promedio}")

def Calcular_mayor(lista):
    Mayor = max(lista)
    print(f"Número máximo de la lista : {Mayor}")

def Calcular_menor(lista):
    Menor = min(lista)
    print(f"Número menor de la lista : {Menor}")

def Calcular_ascendente(lista):
    Ascendente = sorted(lista)
    print(f"Ordenar la lista de forma Ascendente: {Ascendente}")

def Calcular_descendente(lista):
    Descendente = sorted(lista, reverse=True)
    print(f"Ordenar la lista de forma Descendente: {Descendente}")

def Calcular_moda(lista):
    Moda = statistics.mode(lista)
    print(f"Moda de la lista : {Moda}")

def Calcular_Media(lista):
    Media = statistics.median(lista)
    print(f"Media de la lista : {Media}")

def Buscar_numero(lista, numero):
    posiciones = []
    conteo = 0
    for i, num in enumerate(lista):
        if num == numero:
            posiciones.append(i)
            conteo += 1
    if posiciones:
        print("El número", numero, "se encuentra en las posiciones:", posiciones)
        print("Número de ocurrencias:", conteo)
    else:
        print("El número", numero, "no se encuentra en el arreglo.")

def Mostrar_menu(lista):
    Opcion = ""
    while Opcion != "K":
        print("\n--- Menú ---")
        print("A")
        print("B")
        print("C")
        print("D")
        print("E")
        print("F")
        print("G")
        print("H")
        print("I")
        print("J")
        print("K")

    Opcion = input("Seleccione una Opción : ")

    if Opcion == "A":
        lista_original(lista)
    

def main():
    n = int(input("Ingrese la cantidad de elementos del arreglo: "))
    arreglo = generar_lista(n)

    Mostrar_menu(arreglo)

if __name__ == "__main__":
    main()