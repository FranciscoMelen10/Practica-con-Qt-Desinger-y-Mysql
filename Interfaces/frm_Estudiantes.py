import sys

from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from Datos import dt_estudiante


from Datos import dt_estudiante


class Form_Estudiante(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Form_Estudiante,self).__init__(parent)
        loadUi(".\Interfaz.ui",self)
        self.BT_Guardar.clicked.connect(self.guardarEstudiantes)

    def guardarEstudiantes(self):
        dt_estudiante.Dt_Estudiantes.agregarEstudiante(int(self.Line_Id.text()), self.Line_Nombre.text(),
                                                       self.Line_Apellido.text(), int(self.Line_Grado.text()))

    def abrirVentana(self):
        app = QtWidgets.QApplication(sys.argv)
        aplicacion = Form_Estudiante()
        aplicacion.show()
        app.exec()

def main():
    Form_Estudiante.abrirVentana("")


main()