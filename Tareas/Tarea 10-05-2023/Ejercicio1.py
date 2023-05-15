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
    print(lista)
    print(f"Lista Original : {lista}")

def Calcular_suma(lista):
    print(lista) 
    Suma = sum(lista)
    print(f"Suma de la lista : {Suma}")

def Calcular_promedio(lista):
    print(lista) 
    Promedio = sum(lista) / len(lista)
    print(f"Promedio de la lista: {Promedio}")

def Calcular_mayor(lista):
    print(lista) 
    Mayor = max(lista)
    print(f"Número máximo de la lista : {Mayor}")

def Calcular_menor(lista):
    print(lista) 
    Menor = min(lista)
    print(f"Número menor de la lista : {Menor}")

def Calcular_ascendente(lista):
    print(lista) 
    Ascendente = sorted(lista)
    print(f"Ordenar la lista de forma Ascendente: {Ascendente}")

def Calcular_descendente(lista):
    print(lista) 
    Descendente = sorted(lista, reverse=True)
    print(f"Ordenar la lista de forma Descendente: {Descendente}")

def Calcular_moda(lista):
    print(lista) 
    Moda = statistics.mode(lista)
    print(f"Moda de la lista : {Moda}")

def Calcular_Media(lista):
    print(lista) 
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
        print("A - Imprimir arreglo original (El primero que se generó) ")
        print("B - Suma")
        print("C - Promedio")
        print("D - Mayor")
        print("E - Menor")
        print("F - Ascendente")
        print("G - Descendente")
        print("H - Moda")
        print("I - Mediana")
        print("J - Buscar")
        print("K - Salir del programa...") 
        break

    Opcion = input("Seleccione una Opción : ")
    
    if Opcion == "A":
        lista_original(lista)
    elif Opcion == "B":
        Calcular_suma(lista)
    elif Opcion == "C":
        Calcular_promedio(lista)
    elif Opcion == "D":
        Calcular_mayor(lista)
    elif Opcion == "E":
        Calcular_menor(lista)
    elif Opcion == "F":
        Calcular_ascendente(lista)
    elif Opcion == "G":
        Calcular_descendente(lista)
    elif Opcion == "H":
        Calcular_moda(lista)
    elif Opcion == "I":
        Calcular_Media(lista)
    elif Opcion == "J":
        numero = int(input("Ingresa el número que deseas buscar: "))
        Buscar_numero(lista, numero)
    elif Opcion == "K":
            print("Saliendo del programa... ", end="")
    else:
        print("La letra digitada en el menú es erronea.")             
    

def main():
    n = int(input("Ingrese la cantidad de elementos del arreglo: "))
    lista = generar_lista(n)
    
    Mostrar_menu(lista)

if __name__ == "__main__":
    main()
