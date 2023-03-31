import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from Datos import dt_estudiante


class Form_Estudiante(QtWidgets.QMainWindow):
    def __init__(self):
        self.indicador = 0

        super(Form_Estudiante,self).__init__()
        loadUi(".\Interfaz.ui",self)
        self.BT_Guardar.clicked.connect(self.guardarEstudiantes)

    def guardarEstudiantes(self):
        if not self.Line_Nombre.text()== "" and not self.Line_Apellido.text()== "" and not self.Line_Grado.text()== "":
            self.indicador = 1
            dt_estudiante.Dt_Estudiantes.agregarEstudiante(self.Line_Nombre.text(),self.Line_Apellido.text(), int(self.Line_Grado.text()))
            self.mensaje(self.indicador)
            self.indicador = 0
            return self.indicador

        else:
            self.mensaje(self.indicador)
            indicador = 0
            return indicador

    def mensaje(self,indicador):
        if indicador == 1:
            QMessageBox.about(self, "Registrado", "Datos registrados correctamente")

        else:
            QMessageBox.about(self, "Error", "Error de registros de datos")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    aplicacion = Form_Estudiante()
    aplicacion.show()
    app.exec()

