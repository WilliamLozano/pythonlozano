cadena = "Hola mundo"
letra = "o"
contador = 0

for c in cadena:
    if c == letra:
        contador += 1

print(f"La letra '{letra}' aparece {contador} veces en la cadena.")
