num_primos = 0

for numero in range(2, 1001):
    es_primo = True

    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

    if es_primo:
        print(numero, "es un número primo.")
        num_primos += 1

print("En total hay", num_primos, "números primos entre 1 y 1000.")

