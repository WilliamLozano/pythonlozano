numero = int(input("Introduce un número: "))

suma_divisores = 0

for i in range(1, numero):
    if numero % i == 0:
        suma_divisores += i

if suma_divisores == numero:
    print(numero, "es un número perfecto.")
else:
    print(numero, "no es un número perfecto.")
