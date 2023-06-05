

    
class curso():
    def __init__ (self,estudiante, clase, curso):
        self.__clase = clase
        self.__estudiante = estudiante
        self.__curso = [curso]

    def getEstudiante(self):
        return self.__estudiante
    
    def getClase(self):
        return self.__clase
    
    def getCurso(self):
        return self.__curso
    
    def getD2(self):
        return f"{self.__estudiante, self.__clase, self.__curso}"
    
    def setCurso(self, curso):
        self.__curso=curso

    def eliCurso(self,curso):
        self.curso = curso
        for i in (self.__curso):
            if curso == i:
                return self.__curso.remove (curso)

a1 = curso("pedro", "B12", "sexto")

print(a1.getEstudiante())
print(a1.getClase())
print(a1.getCurso())
print("//////////////////////")
print (a1.getCurso())
print (a1.eliCurso("sexto"))
print (a1.getCurso())

#crear un metodo que muestre todos los datos del objeto  x
#agregar un atributo estudiante y ese estudiante agregarle una lista llamada curso x
#crear un metodo que sirva para insertar cursos x
#crear un metodo que sirva para consultar los cursos x
#crear un metodo que sirva para eliminar un curso, con remove o no
#crear un método que sirva para
# 
#  modificar un curso X 
