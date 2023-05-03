# utilizando el codigo de el profesor saque la suma, promedio, max, min, mediana, desviacion estandar

import random
lista = []
menor = []
tam = random.randint(10,20)
print(tam)


for i in range(tam):
    num=random.randrange(100)
    lista.append(num)

print(lista)

menor = lista[0]

for i in range (len(lista)):
    if lista[i] < menor:
     menor = lista[i]

print("El mayor número de la lista es:", menor)

