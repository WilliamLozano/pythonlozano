# utilizando el codigo de el profesor saque la suma, promedio, max, min, mediana, desviacion estandar

import random
lista = []
suma = []
tam = random.randint(10,20)
print(tam)


for i in range(tam):
    num=random.randrange(100)
    lista.append(num)

print(lista)

suma = 0

for i in range(len(lista)):
  suma += (lista[i])

print("La suma de los elementos de la lista es:", suma)




