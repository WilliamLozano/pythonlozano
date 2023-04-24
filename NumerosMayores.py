

numero = int(input("Ingrese un numero: "))
print("este es el numero 1 :", numero)

numero2 = int(input("Ingrese un numero: "))
print("este es el numero 2 :", numero2)

numero3 = int(input("Ingrese un numero: "))
print("este es el numero 3 :", numero3)

if numero > numero2:
   print("Este es el numero mayor :", numero)
elif numero2 > numero:
    print("Este es el numero mayor :", numero2)
elif numero3 > numero2 > numero:
    print("Este es el numero mayor :", numero3)
