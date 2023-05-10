def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def contar_y_encontrar_primos(conjunto):
    primos = []
    contador = 0
    
    for elemento in conjunto:
        if es_primo(elemento):
            primos.append(elemento)
            contador += 1
    
    return contador, primos

# Ejemplo de uso
conjunto = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
cantidad, primos = contar_y_encontrar_primos(conjunto)

print(f"En el conjunto hay {cantidad} números primos.")
print("Los números primos son:", primos)
