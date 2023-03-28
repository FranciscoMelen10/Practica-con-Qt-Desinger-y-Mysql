
class Estudiantes:

    def __init__(self ,id ,nombre ,apellido ,grado):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.grado = grado

    def __str__(self):
        return f'''
        id: {self.id}
        nombre: {self.nombre} 
        apellido: {self.apellido}
        grado: {self.grado}
        '''

    def setId(self,id):
        self.id = id

    def getId(self):
        return self.id


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

