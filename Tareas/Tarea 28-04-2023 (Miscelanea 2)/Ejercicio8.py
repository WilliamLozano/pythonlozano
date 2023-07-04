numero = input("Ingrese un número de hasta 9 dígitos: ")

# Imprimir el número en orden inverso
for i in range(len(numero)-1, -1, -1):
    print(numero[i], end="")
