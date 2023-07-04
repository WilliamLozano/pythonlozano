for num in range(100, 1000):
    
    c1 = num // 100
    c2 = (num // 10) % 10
    c3 = num % 10
    
    
    suma_cubos = c1**3 + c2**3 + c3**3
    
    
    if suma_cubos == num:
        print(num)
