import random

# Generar lista de calificaciones aleatorias
num_aprendices = random.randint(20, 30)
calificaciones = [round(random.uniform(0, 5), 1) for _ in range(num_aprendices)]

# 1. Generar listas de aprobados y reprobados
aprobados = [calificacion for calificacion in calificaciones if calificacion >= 3]
reprobados = [calificacion for calificacion in calificaciones if calificacion < 3]

# 2. Generar listas por cada unidad
unidades = []
for i in range(6):
    rango_inferior = i
    rango_superior = i + 1
    unidad = [calificacion for calificacion in calificaciones if rango_inferior <= calificacion < rango_superior]
    unidades.append(unidad)

# 3. Calcular promedios de aprobados y reprobados
promedio_aprobados = sum(aprobados) / len(aprobados) if aprobados else 0
promedio_reprobados = sum(reprobados) / len(reprobados) if reprobados else 0

# Imprimir resultados
print("Calificaciones de los aprendices:", calificaciones)
print("Aprobados:", aprobados)
print("Reprobados:", reprobados)
print("Unidades:")
for i, unidad in enumerate(unidades):
    print(f"Unidad {i+1}: {unidad}")
print("Promedio de aprobados:", promedio_aprobados)
print("Promedio de reprobados:", promedio_reprobados)
