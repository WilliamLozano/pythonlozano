num_perfectos = 0

for numero in range(1, 1001):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i

    if suma_divisores == numero:
        print(numero, "es un número perfecto.")
        num_perfectos += 1

print("En total hay", num_perfectos, "números perfectos entre 1 y 1000.")
