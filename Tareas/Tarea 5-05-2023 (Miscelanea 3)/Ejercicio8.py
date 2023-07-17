def suma_pares_promedio_impares(conjunto):
    suma_pares = 0
    contador_impares = 0
    suma_impares = 0
    
    for elemento in conjunto:
        if elemento % 2 == 0:
            suma_pares += elemento
        else:
            contador_impares += 1
            suma_impares += elemento
    
    promedio_impares = suma_impares / contador_impares if contador_impares > 0 else 0
    
    return suma_pares, promedio_impares

# Ejemplo de uso
conjunto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma_pares, promedio_impares = suma_pares_promedio_impares(conjunto)

print(f"La suma de los números pares es: {suma_pares}")
print(f"El promedio de los números impares es: {promedio_impares}")
