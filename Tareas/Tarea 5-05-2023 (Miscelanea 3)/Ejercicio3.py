def fibonacci(n):
    # Manejar casos especiales para n = 0 y n = 1
    if n == 0:
        return []
    elif n == 1:
        return [0]
    
    # Inicializar los primeros dos elementos de la serie
    fib = [0, 1]
    
    # Calcular los siguientes elementos de la serie hasta llegar a n
    while len(fib) < n:
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)
    
    return fib

# Pedir al usuario la cantidad de dígitos para la serie de Fibonacci
num_digitos = int(input("Ingrese la cantidad de dígitos para la serie de Fibonacci: "))

# Obtener la serie de Fibonacci con la cantidad de dígitos indicada
serie = fibonacci(num_digitos)

# Imprimir la serie de Fibonacci
print(serie)
