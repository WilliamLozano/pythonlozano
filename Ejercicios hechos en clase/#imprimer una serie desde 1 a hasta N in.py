#imprimer una serie desde 1 a hasta N ingresado por el usuario
#pero cada vez que encuentre un multiplo de 7 debe indicarlo
#con while.

serie = 1 # esta variable se inicia con 1
while serie <= int(input("Ingrese un numero para repetir la serie cuantas veces sea necesario : ")): # se utiliza el bucle while para repetir la variable "serie" cuantas veces sea necesario

    if serie %7 == 0: #se utiliza el condicional if de la variable "serie" para comprobar cada vez que se haya alcanzado un multiplo de 7 y se imprimira un mensaje cada vez que pase
     print("es multiplo de 7 pai")
else: #a cambio si no lo es simplemente se ira imprimiendo la serie hasta que sea de nuevo multiplo de 7.
    print(serie)
serie +=1
