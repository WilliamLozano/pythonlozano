import random
import statistics

# variable para generar el 1 arreglo de n elementos con numeros random generados aleatoriamente.

print("Estamos en la operacion A")

print("///////////////////////////////////////////////////////////////////////////")

n = int(input("Ingrese el número de elementos para los arreglos: "))

# Llenar el primer arreglo con números aleatorios
arreglo1 = [random.randint(1, 100) for _ in range(n)]

# Llenar el segundo arreglo con números aleatorios
arreglo2 = [random.randint(1, 100) for _ in range(n)]

# Calcular la suma de cada arreglo

suma_arreglo1 = sum(arreglo1)
suma_arreglo2 = sum(arreglo2)

# Imprimir las listas
print("Arreglo 1:", arreglo1)
print("Arreglo 2:", arreglo2)

# Comparar las sumas e imprimir el resultado

if suma_arreglo1 > suma_arreglo2:
    print(f"El arreglo 1 tiene la suma mas alta. {suma_arreglo1}")
elif suma_arreglo1 < suma_arreglo2: 
    print(f"El arreglo 2 tiene la suma mas alta. {suma_arreglo2}")
else:
    print(f"Los 2 arreglos tienen la misma suma {suma_arreglo1}")   

print("///////////////////////////////////////////////////////////////////////////")

print("Estamos en la operacion B")

n = int(input("Ingrese el número de elementos para los arreglos :  "))

# Llenar el primer arreglo con números aleatorios
arreglo1 = [random.randint(1, 100) for _ in range(n)]

# Llenar el segundo arreglo con números aleatorios
arreglo2 = [random.randint(1, 100) for _ in range(n)]

# Calcular los numeros mayores e imprimir el resultado

mayor_arreglo1 = max(arreglo1)
mayor_arreglo2 = max(arreglo2)

# Imprimir las listas

print(f"Arreglo 1: {arreglo1}")
print(f"Arreglo 2: {arreglo2}")

# Comparar los numeros mayores e imprimir el resultado

if mayor_arreglo1 > mayor_arreglo2:
    print(f"El arreglo1 tiene el numero mayor: {mayor_arreglo1}")
elif mayor_arreglo1 < mayor_arreglo2:
    print(f"El arreglo2 tiene el numero mayor: {mayor_arreglo2}")
else:
    print(f"Ambos arreglos tienen el mismo numero mayor: {mayor_arreglo1} ")

print("///////////////////////////////////////////////////////////////////////////")

print("Estamos en la operacion C")    

n = int(input("Ingrese el número de elementos para los arreglos : "))

# Llenar el primer arreglo con números aleatorios
arreglo1 = [random.randint(1, 100) for _ in range(n)]

# Llenar el segundo arreglo con números aleatorios
arreglo2 = [random.randint(1, 100) for _ in range(n)]

# Calcular los numeros menores e imprimir el resultado

menor_arreglo1 = min(arreglo1)
menor_arreglo2 = min(arreglo2)

# Imprimir las listas

print(f"Arreglo 1: {arreglo1}")
print(f"Arreglo 2: {arreglo2}")

# Comparar los numeros e imprimir el resultado

if menor_arreglo1 > menor_arreglo2:
    print(f"El arreglo1 tiene el numero menor: {menor_arreglo1}")
elif menor_arreglo1 < menor_arreglo2:
    print(f"El arreglo2 tiene el numero menor: {menor_arreglo2}")
else:
    print(f"Ambos arreglos tienen el mismo numero menor: {menor_arreglo1}")

print("///////////////////////////////////////////////////////////////////////////")    

print("Estamos en la operacion D")

n = int(input("Ingrese el número de elementos para los arreglos : "))

# LLenar el primer arreglo con números aleatorios
arreglo1 = [random.randint(1, 100) for _ in range(n)]

# LLenar el segundo arreglo con números aleatorios
arreglo2 = [random.randint(1, 100) for _ in range(n)]

# Calcular el promedio en conjunto de los 2 arreglos. 

promedio_arreglo1 = statistics.mean(arreglo1)
promedio_arreglo2 = statistics.mean(arreglo2)

# Imprimir las listas

print(f"Arreglo 1: {arreglo1}")
print(f"Arreglo 2: {arreglo2}")

# Calcular el promedio conjunto de los 2 arreglos

Resultado = promedio_arreglo1 + promedio_arreglo2

print(f"El promedio en conjunto de los 2 arreglos es: {Resultado}")

print("///////////////////////////////////////////////////////////////////////////")  

print("Estamos en la operacion E")

import random
import statistics

n = int(input("Ingrese el número de elementos para los arreglos: "))

# Llenar el primer arreglo con números aleatorios
arreglo1 = [random.randint(1, 100) for _ in range(n)]

# Llenar el segundo arreglo con números aleatorios
arreglo2 = [random.randint(1, 100) for _ in range(n)]

# Unir los dos arreglos
arreglo_unido = arreglo1 + arreglo2

# Calcular el promedio conjunto
promedio_conjunto = statistics.mean(arreglo_unido)

# Calcular el promedio del primer arreglo
promedio_arreglo1 = statistics.mean(arreglo1)

# Calcular el promedio del segundo arreglo
promedio_arreglo2 = statistics.mean(arreglo2)

# Imprimir los 2 arreglos

print(f"Arreglo 1: {arreglo1}")
print(f"Arreglo 2: {arreglo2}")

# Comparar los promedios y mostrar los resultados
if promedio_arreglo1 > promedio_conjunto:
    print("El promedio del primer arreglo está por encima del promedio conjunto.")
elif promedio_arreglo1 < promedio_conjunto:
    print("El promedio del primer arreglo está por debajo del promedio conjunto.")
else:
    print("El promedio del primer arreglo es igual al promedio conjunto.")

if promedio_arreglo2 > promedio_conjunto:
    print("El promedio del segundo arreglo está por encima del promedio conjunto.")
elif promedio_arreglo2 < promedio_conjunto:
    print("El promedio del segundo arreglo está por debajo del promedio conjunto.")
else:
    print("El promedio del segundo arreglo es igual al promedio conjunto.")
    
print("///////////////////////////////////////////////////////////////////////////")  

print("Estamos en la operacion F y G")

n = int(input("Ingrese el número de elementos para los arreglos: "))

# Llenar el primer arreglo con números aleatorios
arreglo1 = [random.randint(1, 100) for _ in range(n)]

# Llenar el segundo arreglo con números aleatorios
arreglo2 = [random.randint(1, 100) for _ in range(n)]

# Contadores para pares e impares
contador_pares_arreglo1 = 0
contador_pares_arreglo2 = 0
contador_impares_arreglo1 = 0
contador_impares_arreglo2 = 0

# Imprimir los 2 arreglos

print(f"Arreglo 1: {arreglo1}")
print(f"Arreglo 2: {arreglo2}")

# Verificar pares e impares en el primer arreglo
for num in arreglo1:
    if num % 2 == 0:
        contador_pares_arreglo1 += 1
    else:
        contador_impares_arreglo1 += 1

# Verificar pares e impares en el segundo arreglo
for num in arreglo2:
    if num % 2 == 0:
        contador_pares_arreglo2 += 1
    else:
        contador_impares_arreglo2 += 1

# Comparar la cantidad de pares
if contador_pares_arreglo1 > contador_pares_arreglo2:
    print("El arreglo 1 tiene una mayor cantidad de números pares.")
elif contador_pares_arreglo1 < contador_pares_arreglo2:
    print("El arreglo 2 tiene una mayor cantidad de números pares.")
else:
    print("Ambos arreglos tienen la misma cantidad de números pares.")

# Comparar la cantidad de impares
if contador_impares_arreglo1 > contador_impares_arreglo2:
    print("El arreglo 1 tiene una mayor cantidad de números impares.")
elif contador_impares_arreglo1 < contador_impares_arreglo2:
    print("El arreglo 2 tiene una mayor cantidad de números impares.")
else:
    print("Ambos arreglos tienen la misma cantidad de números impares.")

print("///////////////////////////////////////////////////////////////////////////")  

