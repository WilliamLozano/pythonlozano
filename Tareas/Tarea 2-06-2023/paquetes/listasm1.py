# modulo_listas.py

def sumar_elementos(lista):
    """Calcula la suma de todos los elementos de una lista."""
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

def obtener_elemento_mayor(lista):
    """Devuelve el elemento más grande de una lista."""
    mayor = lista[0]
    for elemento in lista:
        if elemento > mayor:
            mayor = elemento
    return mayor

def obtener_elemento_menor(lista):
    """Devuelve el elemento más pequeño de una lista."""
    menor = lista[0]
    for elemento in lista:
        if elemento < menor:
            menor = elemento
    return menor

def eliminar_duplicados(lista):
    """Elimina los elementos duplicados de una lista."""
    lista_sin_duplicados = []
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    return lista_sin_duplicados

def invertir_lista(lista):
    """Invierte el orden de los elementos de una lista."""
    lista_invertida = []
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida
