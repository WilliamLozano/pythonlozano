import random

def generar_lista(tam_min, tam_max):
    tamaño = random.randint(tam_min, tam_max)
    lista = []
    for _ in range(tamaño):
        lista.append(random.randint(100, 500))
    return lista

def ordenar_lista(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def calcular_cuartiles(lista):
    cuartiles = []
    size = len(lista)
    cuartiles.append(lista[size // 4])  # Primer cuartil
    cuartiles.append(lista[size // 2])  # Segundo cuartil (mediana)
    cuartiles.append(lista[(3 * size) // 4])  # Tercer cuartil
    return cuartiles

def calcular_quintiles(lista):
    quintiles = []
    size = len(lista)
    quintiles.append(lista[size // 5])  # Primer quintil
    quintiles.append(lista[(2 * size) // 5])  # Segundo quintil
    quintiles.append(lista[(3 * size) // 5])  # Tercer quintil
    quintiles.append(lista[(4 * size) // 5])  # Cuarto quintil
    return quintiles

# Tamaño de la lista por pueblo
tam_minimo = 200
tam_maximo = 2500

# Generar lista de tamaño aleatorio
icfes_resultados = generar_lista(tam_minimo, tam_maximo)

# Ordenar la lista de resultados
icfes_resultados_ordenados = ordenar_lista(icfes_resultados)

# Hallar el valor de cada cuartil
cuartiles = calcular_cuartiles(icfes_resultados_ordenados)

# Hallar el valor de cada quintil
quintiles = calcular_quintiles(icfes_resultados_ordenados)

print("Cuartiles:", cuartiles)
print("Quintiles:", quintiles)
