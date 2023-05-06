def ordenar_burbuja_mayor_menor(arreglo):
    n = len(arreglo)
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arreglo[j] < arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

def ordenar_burbuja_menor_mayor(arreglo):
    n = len(arreglo)
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

# Ejemplo de uso
arreglo = [5, 2, 8, 1, 9, 3]
print("Arreglo original:", arreglo)

# Ordenar de mayor a menor
ordenar_burbuja_mayor_menor(arreglo)
print("Ordenado de mayor a menor:", arreglo)

# Ordenar de menor a mayor
ordenar_burbuja_menor_mayor(arreglo)
print("Ordenado de menor a mayor:", arreglo)
