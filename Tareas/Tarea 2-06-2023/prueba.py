from paquetes.listasm1 import *
from paquetes.modulosdc import *

#Ejemplo de importación funciones para listas

mi_lista = [1, 2, 3, 4, 5]

print(sumar_elementos(mi_lista))
print(obtener_elemento_mayor(mi_lista))
print(obtener_elemento_menor(mi_lista))
print(eliminar_duplicados(mi_lista))
print(invertir_lista(mi_lista))

#Ejemplo de la importación para diccionarios

from modulo_diccionarios import *

mi_diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

print(obtener_claves(mi_diccionario))
print(obtener_valores(mi_diccionario))
print(obtener_elemento(mi_diccionario, "nombre"))
agregar_elemento(mi_diccionario, "ocupacion", "estudiante")
print(mi_diccionario)
eliminar_elemento(mi_diccionario, "ciudad")
print(mi_diccionario)
