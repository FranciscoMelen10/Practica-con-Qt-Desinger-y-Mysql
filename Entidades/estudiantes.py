
class Estudiantes:

    def __init__(self ,nombre ,apellido ,grado):
        self.nombre = nombre
        self.apellido = apellido
        self.grado = grado

    def __str__(self):
        return f'''
        nombre : {self.nombre} 
        
        '''


    def getName(self):
        return self.nombre

    def setName(self, name):
        self.name = name

    def getApellido(self):
        return self.apellido

    def setApellido(self, apellido):
        self.apellido = apellido

    def getGrado(self):
        return self.grado

    def setGrado(self, grado):
        self.grado = grado

