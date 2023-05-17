#generar una tupla de entre 1 a 15 y concatenarla con otra tupla, para despues cambiar la posicion dentro de la tupla y imprimirla en pantalla

import random
# tupla=float
# for tupla in range(random.randint(1,15)):
#     print("Los numeros de el 1 al 15")

# print(tupla)


tam=random.randint(1,15)
t=()

for i in range(tam):
    n=random.randrange(100)
    t+=(n,)

print(t)

t2 = (t)




