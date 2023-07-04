
def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

# Crear lista de números
numeros = list(range(2, 16))

# Calcular factoriales y guardar en nueva lista
factoriales = []
for numero in numeros:
    resultado = factorial(numero)
    factoriales.append(resultado)
    print(f"Factorial de {numero}: {resultado}")

# Imprimir lista de factoriales
print("Lista de factoriales:", factoriales)
