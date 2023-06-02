# #tamaño lista (por pueblo): minimo 200 maximo 2500.{validación}
# Llenar Icfes {Resultados. 100 - 500}
# Hallar valor de cada cuartil
# Hallar valor de cada quintil
# Funcion que retorne el valor y la posicion dada la lista y el numero de cuartil y quintil
# Promedio por cada cuartil
# Promedio por cada quintil
# Mayor y menor por separado de cada cuartil y quintil respectivamente
# Generar listas separadas por cuartil y quintil

import random
n=random.randint(2,25)
m = random.randint(100, 500)



def llenarlista(n,m):
    lista=[]
    lista=[random.randrange(100, 500)for x in range(n)]
    return lista




def ascender(lista):
    listam=lista
    for i in range(n):
        for o in range(i+1,n):
            if listam[i] > listam[o]:
                listam[i],listam[o] = listam[o],listam[i]
    #c=(n+1)//4  
    #listam = range(c-1)
    #print(listam)
    return listam


l1 = (llenarlista (n,m))
print(l1)

print(ascender(l1))

def calc_cuart(lista):
    cuart = []
    size = len(lista)
    cuart.append(lista[size // 4])
    cuart.append(lista[size // 2])
    cuart.append(lista[(3 * size) // 4]) 
    return cuart

print(calc_cuart(l1))





