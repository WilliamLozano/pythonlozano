# utilizando el codigo de el profesor saque la suma, promedio, max, min, mediana, desviacion estandar

import random
lista = []
resta = []
tam = random.randint(10,20)
print(tam)


for i in range(tam):
    num=random.randrange(100)
    lista.append(num)

print(lista)

resta = 0

for i in range (len(lista)):
    resta -= (lista[i])

print("La resta de los elementos de la lista es :", resta)