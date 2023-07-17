from math import sqrt

while True:
        try:
            a= int(input("ingresar numero :"))
            b= int(input("ingresar numero :"))
            c= int(input("ingresar numero :"))
        except ValueError:    
            print("Se deben que ingresar numeros y deben que ser positivos")
        try:    
            cuadratica1= (b**2)-(4*a*c)
            cuadratica2= (-b)
            cuadratica3=(2*a)
            raiz=sqrt(cuadratica1)
        
            suma=((cuadratica2 + raiz)/cuadratica3)
            resta=((cuadratica2 - raiz)/cuadratica3)
            print(f"el resultado de la resta es: {resta} y el resultado de la suma es : {suma} ")
        except ValueError:
            ("Tiene que ser mayor que 0")

        except ZeroDivisionError:
            print("Los numeros Ingresados deben que ser mayor o igual que 0")
