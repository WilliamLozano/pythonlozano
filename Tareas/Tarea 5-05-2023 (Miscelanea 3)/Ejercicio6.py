def comparar_con_promedio(elemento, conjunto):
    promedio = sum(conjunto) / len(conjunto)
    
    if elemento > promedio:
        return "por encima del promedio"
    elif elemento < promedio:
        return "por debajo del promedio"
    else:
        return "igual al promedio"

# Ejemplo de uso
conjunto = [4, 6, 8, 10, 12]
elemento = 10

resultado = comparar_con_promedio(elemento, conjunto)
print(f"El elemento {elemento} está {resultado}.")
