maximo = int(input("Ingresa el número máximo a superar: "))
suma = 0
n = 0

while suma <= maximo:
    n += 1
    suma += n

print("El número natural más pequeño para superar", maximo, "es", n)
