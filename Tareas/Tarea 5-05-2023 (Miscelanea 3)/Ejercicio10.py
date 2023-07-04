def busqueda_elemento(arreglo, elemento):
    contador = 0
    posiciones = []
    
    for i in range(len(arreglo)):
        if arreglo[i] == elemento:
            contador += 1
            posiciones.append(i)
    
    return contador, posiciones

# Ejemplo de uso
arreglo = [1, 2, 3, 2, 4, 2, 5]
elemento = 2

cantidad, posiciones = busqueda_elemento(arreglo, elemento)

print(f"El elemento {elemento} aparece {cantidad} veces.")
print(f"Se encuentra en las posiciones: {posiciones}")
