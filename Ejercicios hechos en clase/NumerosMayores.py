

numero = int(input("Ingrese un numero: ")) # se declara la variable numero la cual es entera con un imput adentro, indicando ingresar un numero al sistema
print("este es el numero 1 :", numero)

numero2 = int(input("Ingrese un numero: "))
print("este es el numero 2 :", numero2)

numero3 = int(input("Ingrese un numero: "))
print("este es el numero 3 :", numero3)

if numero > numero2: #acá se utiliza la condicional if para hacer referencia que la variable "numero" es mayor que la variable "numero2"
   print("Este es el numero mayor :", numero)
elif numero2 > numero:
    print("Este es el numero mayor :", numero2) #acá se utiliza la condicional elif para hacer referencia que la variable "numero2" es mayor que la variable "numero"
elif numero3 > numero2 > numero: #de nuevo se hace uso de la condicional elif para hacer referencia que la variable "numero3" es mayor que las variables "numero2" y "numero1"
    print("Este es el numero mayor :", numero3)
