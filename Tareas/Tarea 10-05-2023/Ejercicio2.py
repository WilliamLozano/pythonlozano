import random


def generar_lista(n):
    lista = []
    for _ in range(n):
        lista.append(random.randint(1,100))
    return lista


print("Estamos en la Operacion A.")

print("///////////////////////////////////////////////////////////////////////////")

n = int(input("Ingrese el número de elementos para los arreglos: "))

def suma_lista(numero):
    resultado = 0
    for elemento in numero:
        resultado += elemento
    return resultado
    
arreglo1 = [random.randint(1, 25) for _ in range(n)]
arreglo2 = [random.randint(1, 25) for _ in range(n)]

suma_arreglo1 = suma_lista(arreglo1)
suma_arreglo2 = suma_lista(arreglo2)

print("Arreglo 1:", arreglo1)
print("Arreglo 2:", arreglo2)

if suma_arreglo1 > suma_arreglo2:
    print(f"La suma de el arreglo 1 es mayor que la suma del arreglo 2 : {suma_arreglo1}")
elif suma_arreglo1 < suma_arreglo2:
    print(f"La suma de el arreglo 2 es mayor que la suma del arreglo 1 : {suma_arreglo2}")
else:
    print(f"Las 2 sumas tienen el mismo resultado. {suma_arreglo1}")

print("Estamos en la Operacion B.")

print("///////////////////////////////////////////////////////////////////////////")

n = int(input("Ingrese el número de elementos para los arreglos: "))

def Mayor(numero):
    maximo = numero[0]
    for elemento in numero:
        if elemento > maximo:
            len(numero)
            maximo = elemento
    return maximo

arreglo1 = [random.randint(1, 25) for _ in range(n)]
arreglo2 = [random.randint(1, 25) for _ in range(n)]

Mayor_arreglo1 = Mayor(arreglo1)
Mayor_arreglo2 = Mayor(arreglo2)

print("Arreglo 1:", arreglo1)
print("Arreglo 2:", arreglo2)


if Mayor_arreglo1 > Mayor_arreglo2:
    print(f"El arreglo 1 tiene el numero mas grande : {arreglo1}")
elif Mayor_arreglo1 < Mayor_arreglo2:
    print(f"El arreglo 2 tiene el numero mas grande : {arreglo2}")
else:
    print("Los 2 arreglos tienen el mismo numero maximo")

print("Estamos en la Operacion C.")

print("///////////////////////////////////////////////////////////////////////////")

n = int(input("Ingrese el número de elementos para los arreglos: "))

def Menor(numero):
    menor = numero[0]
    for elemento in numero:
        if elemento < menor:
            menor = elemento
    return menor

arreglo1 = [random.randint(1, 25) for _ in range(n)]
arreglo2 = [random.randint(1, 25) for _ in range(n)]

Menor_arreglo1 = Menor(arreglo1)
Menor_arreglo2 = Menor(arreglo2)

print("Arreglo 1:", arreglo1)
print("Arreglo 2:", arreglo2)

if Menor_arreglo1 > Menor_arreglo2:
    print(f"El arreglo 1 tiene el numero mas pequeño : {arreglo1}")
elif Menor_arreglo1 < Menor_arreglo2:
    print(f"El arreglo 2 tiene el numero mas pequeño : {arreglo2}")

print("Estamos en la Operacion D.")

print("///////////////////////////////////////////////////////////////////////////")

n = int(input("Ingrese el número de elementos para los arreglos: "))

def calcular_promedio(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Las listas deben tener la misma longitud")
    
    suma = 0
    for i in range(len(list1)):
        suma += list1[i] + list2[i]
    
    promedio = suma / len(list1)
    return promedio


arreglo1 = [random.randint(1, 25) for _ in range(n)]
arreglo2 = [random.randint(1, 25) for _ in range(n)]

Promedio_arreglo1 = calcular_promedio(arreglo1)
Promedio_arreglo2 = calcular_promedio(arreglo2)

print("Arreglo 1:", arreglo1)
print("Arreglo 2:", arreglo2)

#Resultado_Promedio = Promedio_arreglo1 / Promedio_arreglo2

#print(f"El promedio en conjunto de los 2 arreglos es: {Resultado_Promedio}")
print(f"El promedio en conjunto de los 2 arreglos es: {Promedio_arreglo1}")

print("///////////////////////////////////////////////////////////////////////////")  

print("Estamos en la operacion E")