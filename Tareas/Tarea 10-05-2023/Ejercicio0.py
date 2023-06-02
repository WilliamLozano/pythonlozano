import random

# Función para generar la población con datos aleatorios
def generar_poblacion(tamano, minimo, maximo):
    poblacion = []
    for _ in range(tamano):
        dato = random.randint(minimo, maximo)
        poblacion.append(dato)
    return poblacion

# Función para ordenar una lista de datos de forma ascendente
def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Función para calcular el percentil de una lista de datos
def calcular_percentil(lista, percentil):
    ordenar_lista(lista)
    n = len(lista)
    k = (percentil / 100) * (n - 1)
    f = int(k)
    c = k - f
    if f + 1 < n:
        return lista[f] + c * (lista[f + 1] - lista[f])
    else:
        return lista[f]

# Función para calcular los cuartiles de una población
def calcular_cuartiles(poblacion):
    cuartil_1 = calcular_percentil(poblacion, 25)
    cuartil_2 = calcular_percentil(poblacion, 50)
    cuartil_3 = calcular_percentil(poblacion, 75)
    cuartiles = [cuartil_1, cuartil_2, cuartil_3]
    return cuartiles

# Función para calcular los quintiles de una población
def calcular_quintiles(poblacion):
    quintil_1 = calcular_percentil(poblacion, 20)
    quintil_2 = calcular_percentil(poblacion, 40)
    quintil_3 = calcular_percentil(poblacion, 60)
    quintil_4 = calcular_percentil(poblacion, 80)
    quintiles = [quintil_1, quintil_2, quintil_3, quintil_4]
    return quintiles

# Función para calcular el promedio de una lista de datos
def calcular_promedio(datos):
    suma = 0
    n = len(datos)
    for dato in datos:
        suma += dato
    promedio = suma / n
    return promedio

# Función para calcular el promedio por cuartil
def calcular_promedio_por_cuartil(poblacion, cuartiles):
    promedios = []
    for i in range(len(cuartiles) - 1):
        cuartil_actual = cuartiles[i]
        cuartil_siguiente = cuartiles[i + 1]
        datos_cuartil = [dato for dato in poblacion if cuartil_actual <= dato < cuartil_siguiente]
        promedio_cuartil = calcular_promedio(datos_cuartil)
        promedios.append(promedio_cuartil)
    return promedios

# Función para calcular el promedio por quintil
def calcular_promedio_por_quintil(poblacion, quintiles):
    promedios = []
    for i in range(len(quintiles) - 1):
        quintil_actual = quintiles[i]
        quintil_siguiente = quintiles[i + 1]
        datos_quintil = [dato for dato in poblacion if quintil_actual<= dato < quintil_siguiente]
        promedio_quintil = calcular_promedio(datos_quintil)
        promedios.append(promedio_quintil)
    return promedios

# Función para obtener el mayor valor por cuartil
def obtener_mayor_por_cuartil(poblacion, cuartiles):
    mayores = []
    for i in range(len(cuartiles) - 1):
        cuartil_actual = cuartiles[i]
        cuartil_siguiente = cuartiles[i + 1]
        datos_cuartil = [dato for dato in poblacion if cuartil_actual <= dato < cuartil_siguiente]
        mayor_cuartil = max(datos_cuartil)
        mayores.append(mayor_cuartil)
    return mayores

# Función para obtener el menor valor por cuartil
def obtener_menor_por_cuartil(poblacion, cuartiles):
    menores = []
    for i in range(len(cuartiles) - 1):
        cuartil_actual = cuartiles[i]
        cuartil_siguiente = cuartiles[i + 1]
        datos_cuartil = [dato for dato in poblacion if cuartil_actual <= dato < cuartil_siguiente]
        menor_cuartil = min(datos_cuartil)
        menores.append(menor_cuartil)
    return menores

# Función para obtener el mayor valor por quintil
def obtener_mayor_por_quintil(poblacion, quintiles):
    mayores = []
    for i in range(len(quintiles) - 1):
        quintil_actual = quintiles[i]
        quintil_siguiente = quintiles[i + 1]
        datos_quintil = [dato for dato in poblacion if quintil_actual <= dato < quintil_siguiente]
        mayor_quintil = max(datos_quintil)
        mayores.append(mayor_quintil)
    return mayores

# Función para obtener el menor valor por quintil
def obtener_menor_por_quintil(poblacion, quintiles):
    menores = []
    for i in range(len(quintiles) - 1):
        quintil_actual = quintiles[i]
        quintil_siguiente = quintiles[i + 1]
        datos_quintil = [dato for dato in poblacion if quintil_actual <= dato < quintil_siguiente]
        menor_quintil = min(datos_quintil)
        menores.append(menor_quintil)
    return menores

# Función para generar listas separadas por cuartil
def generar_listas_por_cuartil(poblacion, cuartiles):
    listas_cuartiles = []
    for i in range(len(cuartiles) - 1):
        cuartil_actual = cuartiles[i]
        cuartil_siguiente = cuartiles[i + 1]
        lista_cuartil = [dato for dato in poblacion if cuartil_actual <= dato < cuartil_siguiente]
        listas_cuartiles.append(lista_cuartil)
    return listas_cuartiles

# Función para generar listas separadas por quintil
def generar_listas_por_quintil(poblacion, quintiles):
    listas_quintiles = []
    for i in range(len(quintiles) - 1):
        quintil_actual = quintiles[i]
        quintil_siguiente = quintiles[i + 1]
        lista_quintil = [dato for dato in poblacion if quintil_actual <= dato < quintil_siguiente]
        listas_quintiles.append(lista_quintil)
    return listas_quintiles

# Función para mostrar el menú
def mostrar_menu():
    print("1. Calcular cuartiles")
    print("2. Calcular quintiles")
    print("3. Calcular promedio")
    print("4. Calcular promedio por cuartil")
    print("5. Calcular promedio por quintil")
    print("6. Obtener mayor por cuartil")
    print("7. Obtener menor por cuartil")
    print("8. Obtener mayor por quintil")
    print("9. Obtener menor por quintil")
    print("10. Generar listas por cuartil")
    print("11. Generar listas por quintil")
    print("0. Salir")

# Código principal del programa
if _name_ == "_main_":
    poblacion = generar_poblacion(100, 0, 100)  # Generar una población de ejemplo

    while True:
        mostrar_menu()
        opcion = int(input("Ingrese el número de la opción deseada: "))

        if opcion == 1:
            cuartiles = calcular_cuartiles(poblacion)
            print("Cuartiles:", cuartiles)
        elif opcion == 2:
            quintiles = calcular_quintiles(poblacion)
            print("Quintiles:", quintiles)
        elif opcion == 3:
            promedio = calcular_promedio(poblacion)
            print("Promedio:", promedio)
        elif opcion == 4:
            promedios_cuartiles = calcular_promedio_por_cuartil(poblacion, cuartiles)
            print("Promedio por cuartil:", promedios_cuartiles)
        elif opcion == 5:
            promedios_quintiles = calcular_promedio_por_quintil(poblacion, quintiles)
            print("Promedio por quintil:", promedios_quintiles)
        elif opcion == 6:
            mayor_por_cuartil = obtener_mayor_por_cuartil(poblacion, cuartiles)
            print("Mayor por cuartil:", mayor_por_cuartil)
        elif opcion == 7:
            menor_por_cuartil = obtener_menor_por_cuartil(poblacion, cuartiles)
            print("Menor por cuartil:", menor_por_cuartil)
        elif opcion == 8:
            mayor_por_quintil = obtener_mayor_por_quintil(poblacion, quintiles)
            print("Mayor por quintil:", mayor_por_quintil)
        elif opcion == 9:
            menor_por_quintil = obtener_menor_por_quintil(poblacion, quintiles)
            print("Menor por quintil:", menor_por_quintil)
        elif opcion == 10:
            listas_cuartiles = generar_listas_por_cuartil(poblacion, cuartiles)
            print("Listas por cuartil:")
            for i, lista in enumerate(listas_cuartiles):
                print(f"Cuartil {i+1}: {lista}")
        elif opcion == 11:
            listas_quintiles = generar_listas_por_quintil(poblacion, quintiles)
            print("Listas por quintil:")
            for i, lista in enumerate(listas_quintiles):
                print(f"Quintil {i+1}: {lista}")
        elif opcion == 0:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")