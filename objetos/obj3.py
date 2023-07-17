class empleado():
    def __init__(self, nombre, cargo, salario):
        self.__nombre = nombre 
        self.__cargo = cargo
        self.__salario = salario
    
    def getNombre(self):
        return  self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre 

#////////////////////////////////////////////////////

    def getCargo(self):
        return self.__cargo
    
    def setCargo(self, cargo):
        self.__salario = cargo

#/////////////////////////////////////////////////////

    def getSalario(self):
        return self.__salario
    
    def setSalario(self, salario):
        self.__salario = salario

#///////////////////////////////////////////////////// 

    def getDatos(self):
        return f"{self.__nombre, self.__cargo, self.__salario}"
    
#/////////////////////////////////////////////////////

    #def calcSalario(self):
        #A
        
        

#Datos de prueba

a1 = empleado("Pedro", "Programador Junior", 1000000)
a2 = empleado("William", "Programador Semi Senior", 1200000)
a3 = empleado("Felipe", "Programador Senior", 1600000)

print(a1.getDatos())
print(a2.getDatos())
print(a3.getDatos())
