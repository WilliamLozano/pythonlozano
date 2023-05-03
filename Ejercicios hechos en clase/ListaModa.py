import random

lista = []
tam = random.randint(10,20)
print(tam)

for i in range(tam):
    num = random.randrange(100)
    lista.append(num)

print(lista)

# Moda de la lista
lista_ordenada = sorted(lista)
moda = lista_ordenada[0]
frecuencia_maxima = 1
frecuencia_actual = 1

for i in range(1, len(lista_ordenada)):
    if lista_ordenada[i] == lista_ordenada[i-1]:
        frecuencia_actual += 1
    else:
        if frecuencia_actual > frecuencia_maxima:
            moda = lista_ordenada[i-1]
            frecuencia_maxima = frecuencia_actual
        frecuencia_actual = 1

if frecuencia_actual > frecuencia_maxima:
    moda = lista_ordenada[-1]

print("La moda de la lista es:", moda)
