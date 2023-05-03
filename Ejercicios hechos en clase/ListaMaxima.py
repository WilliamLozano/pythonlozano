# utilizando el codigo de el profesor saque la suma, promedio, max, min, mediana, desviacion estandar

import random
lista = []
maximo = []
tam = random.randint(10,20)
print(tam)


for i in range(tam):
    num=random.randrange(100)
    lista.append(num)

print(lista)

maximo = lista[0]

for i in range (len(lista)):
    if lista[i] > maximo:
     maximo = lista[i]

print("El mayor número de la lista es:", maximo)
