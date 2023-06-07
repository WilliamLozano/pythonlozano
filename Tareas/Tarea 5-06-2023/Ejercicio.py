class Empleado:
    suma = 0
    contador = 0
    

    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        Empleado.suma += salario
        Empleado.contador += 1

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cargo(self):
        return self.cargo

    def set_cargo(self, cargo):
        self.cargo = cargo

    def get_salario(self):
        return self.salario

    def set_salario(self, salario):
        self.salario = salario

    def calcular_salario_hora(self):
        horas_trabajo_diario = 8
        dias_trabajo_semana = 5
        salario_hora = self.salario / (horas_trabajo_diario * dias_trabajo_semana)
        return salario_hora

    def calcular_incremento_ipc(self):
        incremento = 0.03
        ipc = 13.12  
        salario_actualizado = self.salario + (self.salario * ipc)
        if self.salario == salario_minimo:
            salario_actualizado += salario_actualizado * incremento
        incremento_total = salario_actualizado - self.salario
        return incremento_total

    def calcular_salario_horas_extras(self, horas_extras):
        salario_hora = self.calcular_salario_hora()
        horas_diarias_maximas = 2
        salario_base = self.salario
        if horas_extras > 0 and horas_extras <= horas_diarias_maximas:
            salario_extras = salario_hora * horas_extras
            salario_total = salario_base + salario_extras
            return salario_total
        else:
            return "Error: Las horas extras deben estar entre 0 y 2."

    def visualizar_suma_salarios():
        return Empleado.suma

    
    def calcular_promedio_salarios():
        return Empleado.suma / Empleado.contador

salario_minimo = 1200000

# Crear un empleado
empleado1 = Empleado("Juan Perez", "Gerente", 4300000)

# Obtener el nombre del empleado
print(empleado1.get_nombre())  # Output: Juan Perez

# Obtener el salario por hora del empleado
print(empleado1.calcular_salario_hora())  # Output: 25.0

# Calcular el incremento de salario según el IPC
print(empleado1.calcular_incremento_ipc())  # Output: 150.0

# Calcular el salario con horas extras
print(empleado1.calcular_salario_horas_extras(1))  # Output: 5050.0

# Visualizar la suma de los salarios
print(Empleado.visualizar_suma_salarios())  # Output: 5000

# Calcular el promedio de los salarios
print(Empleado.calcular_promedio_salarios())  # Output: 5000.0

