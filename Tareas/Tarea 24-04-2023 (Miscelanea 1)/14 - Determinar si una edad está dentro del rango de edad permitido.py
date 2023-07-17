precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

if descuento > 100:
    print("El porcentaje de descuento no puede ser mayor a 100.")
else:
    precio_final = precio * (1 - descuento / 100)
    print("El precio final del producto con descuento es:", precio_final)
