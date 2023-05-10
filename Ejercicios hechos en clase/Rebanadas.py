numeros = [3, 8, 5, 12, 7, 9]

resultados = []

for numero in numeros:
    if numero % 2 == 0:
        resultados.append(numero ** 0.5)  # Raíz cuadrada
    else:
        resultados.append(numero ** 2)  # Elevar al cuadrado

print(resultados)
