#solicite 2 numeros al usuario. Evalue si es factor uno del otro en cualquier orden. Si no, Pida 2 numeros de nuevo.
num1 = 3
num2 = 2

while not (num1 % num2 !=0 and num2 % num1 != 0): #aca se hace uso de el ciclo while, especificamente el no el cual se utiliza en casos donde no es verdadero el while pero de todas formas hace que se pueda ingresar.
   num1 = int(input(f"Ingrese el primer numero al sistema :")) #acá se declara un imput en el cual se pide que el usuario ingrese el primer numero al sistema
   num2 = int(input(f"Ingrese el segundo numero al sistema :")) #acá se declara un imput en el cual se pide que el usuario ingrese el segundo numero al sistema
   print(f"El numero 1 se puede dividir entre el numero 2 {num1} ") #acá hago uso de un print para indicar que el numero 1 se puede dividir entre el numero 2
print(f"El numero 2 se puede dividir entre el numero 1 {num2} ") #lo mismo acá

print(f"Los dos numeros son factor uno del otro {num1} {num2}") # en este caso acá se imprime en pantalla que los 2 numeros son factores del uno al otro


print("los numeros lamentablemente no son factor entre los 2, por lo tanto le pido que ingrese 2 numeros nuevamente.") # y en este print se hace referencia que los 2 numeros no son factores entre los 2 por lo tanto tendrá que ingresar 2 nuevos numeros nuevamente.
