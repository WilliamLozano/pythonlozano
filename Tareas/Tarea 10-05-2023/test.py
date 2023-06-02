import random

def generar_lista(n):
    lista = []
    for _ in range(n):
        lista.append(random.randint(1,100))
    return lista



def calcular_factoriales(lista, factoriales):
    factoriales = []
    factorial = 1
    for n in range(1, 101):
        factorial *= n
        factoriales.append(lista)
    return factoriales