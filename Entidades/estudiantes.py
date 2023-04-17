
class Estudiantes:

    def __init__(self ,idestudiantes ,nombre ,apellido ,grado):
        self.idestudiantes = idestudiantes
        self.nombre = nombre
        self.apellido = apellido
        self.grado = grado

    def __str__(self):
        return f'''
        idestudiantes: {self.idestudiantes}
        nombre: {self.nombre} 
        apellido: {self.apellido}
        grado: {self.grado}
        '''

    def setId(self,idestudiantes):
        self.id = idestudiantes

    def getId(self):
        return self.idestudiantes


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

