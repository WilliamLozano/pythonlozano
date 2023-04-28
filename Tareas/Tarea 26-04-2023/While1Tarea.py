num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

while num1 <= num2:
    print("El primer número debe ser mayor que el segundo.")
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

resultado = num1 - num2

while resultado >= num2:
    resultado -= num2

print("El resultado final es:", resultado)
