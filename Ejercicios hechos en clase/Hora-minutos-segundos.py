import datetime

# Obtener la hora actual
hora_actual = datetime.datetime.now().time()

# Obtener la entrada del usuario para hora, minutos y segundos
hora = int(input("Ingrese la hora (formato 24 horas): "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))

# Crear un objeto de tiempo con los valores ingresados por el usuario
hora_ingresada = datetime.time(hora, minutos, segundos)

# Calcular la diferencia de tiempo entre la hora actual y la hora ingresada por el usuario
diferencia_tiempo = datetime.datetime.combine(datetime.date.today(), hora_ingresada) - datetime.datetime.combine(datetime.date.today(), hora_actual)

# Calcular la cantidad de segundos faltantes para la próxima hora completa
segundos_faltantes = diferencia_tiempo.total_seconds()

# Calcular la cantidad de minutos faltantes para el próximo minuto completo
minutos_faltantes = segundos_faltantes // 60

# Calcular la cantidad de segundos faltantes para el próximo segundo completo
segundos_faltantes %= 60

# Imprimir el resultado
print("Faltan {} horas, {} minutos y {} segundos para el próximo tiempo completo.".format(diferencia_tiempo.seconds // 3600, minutos_faltantes, segundos_faltantes))
