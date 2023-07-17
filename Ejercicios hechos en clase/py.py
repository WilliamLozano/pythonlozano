#verificar numeros de una lista con try _- except
numeros=[4,7,6,8,9]
while True:
    try:
        nuevo=int(input('escriba un numero'))
        if not (nuevo in numeros):
            numeros.append(nuevo)
            print(f'valor aceptado:, {numeros}' )
            break
        else:   
            raise ValueError('solo numeros sin repeticion')
    except ValueError:
        print('solo puede ingresar numeros sin repetir')
        print(f'la lista no se ha actualizado, {numeros }')
    except KeyboardInterrupt:
        print('se interrumpio la ejecucion')
