# modulo_diccionarios.py

def obtener_claves(diccionario):
    """Devuelve una lista con todas las claves del diccionario."""
    return list(diccionario.keys())

def obtener_valores(diccionario):
    """Devuelve una lista con todos los valores del diccionario."""
    return list(diccionario.values())

def obtener_elemento(diccionario, clave):
    """Devuelve el valor asociado a una clave en el diccionario."""
    return diccionario.get(clave)

def agregar_elemento(diccionario, clave, valor):
    """Agrega un elemento al diccionario con una nueva clave y valor."""
    diccionario[clave] = valor

def eliminar_elemento(diccionario, clave):
    """Elimina un elemento del diccionario dada una clave."""
    diccionario.pop(clave, None)
