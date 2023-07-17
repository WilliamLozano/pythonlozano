# 1. Comparar validación de número ingresado con while vs try-except en el caso de división por cero

# Comparación con try-except

try:
    num1 = int(input("Ingrese el primer numero al sistema : "))
    num2 = int(input("Ingrese el segundo numero al sistema : "))
    
    total = num1 / num2

    print(f"La división de los 2 numeros es : {total}")

except ZeroDivisionError:
    print("No puedes dividir por 0, pai tienes que ingresar un numero entero")

# Comparación con while



while True != 0:

    try: 
        num1 = int(input("Ingrese un numero al sistema  : "))
        num2 = int(input("Ingrese un numero al sistema  : "))

        total = num1 / num2
        
        print(f"La división de los 2 numeros es : {total}")

    except ZeroDivisionError:
        print("No se puede dividir en 0")