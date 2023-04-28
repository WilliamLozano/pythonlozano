inicio = int(input("Ingrese el número de inicio: "))
fin = int(input("Ingrese el número final: "))
cantidad = int(input("Ingrese la cantidad a incrementar o decrementar: "))
N = int(input("Ingrese el número del cual desea contar los múltiplos: "))

if inicio < fin:
    serie = range(inicio, fin + 1, cantidad)
else:
    serie = range(inicio, fin - 1, -cantidad)

multiplos = 0
for i in serie:
    if i % N == 0:
        multiplos += 1

print("Hay", multiplos, "múltiplos de", N, "en la serie.")
