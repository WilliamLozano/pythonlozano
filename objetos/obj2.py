# class Stack:
#     def __init__(self):
#         self.__stk = []

#     def push(self, val):
#         self.__stk.append(val)

#     def pop(self):
#         val = self.__stk[-1]
#         del self.__stk[-1]
#         return val


# class CountingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sumpop = 0

#     def get_counter(self):
#         return f"la suma de los de los pop es: {self.__sumpop}"
        

#     def pop(self):
#         self.__sumpop+=1
#         Stack.pop(self)
	

# stk = CountingStack()
# for i in range(100):
#     stk.push(i)
#     stk.pop()
# print(stk.get_counter())


class persona():
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
        self.__cursos=[]

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre=nombre 
    
    def getDocumento(self):
        return self.__documento
    
    def setDocumento(self, documento):
        self.__documento=documento
    
    # def getDatos(self, nombre, documento):
    #     return self.__nombre and self.__documento
    
    


p1=persona("Ana", 123)

p1.setNombre("Pedro")
print(p1.getNombre())

p1.setDocumento(321)
print(p1.getDocumento())

#//////////////////////////////////////////////////

p2=persona("Carlos", 987)

p2.setNombre("Juan")
print(p2.getNombre())

p2.setDocumento(687)
print(p2.getDocumento())




#crear un metodo que muestre todos los datos del objeto 
#agregar un atributo estudiante y ese estudiante agregarle una lista llamada curso
#crear un metodo que sirva para insertar cursos 
#crear un metodo que sirva para consultar los cursos
#crear un metodo que sirva para eliminar un curso, con remove o no
#crear un método que sirva para modificar un curso
