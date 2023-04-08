import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.uic import loadUi
from Datos import dt_estudiante


class Form_Estudiante(QtWidgets.QMainWindow):
    # Cuando el Indicador esta en "0" es por que el usuario no lleno los campos solitados en el formulario
    # Llenar tabla tiene la recolección de registros de la base de datos pero esos datos se manejan como un diccionario en python


    def __init__(self):
        super(Form_Estudiante,self).__init__()
        loadUi("Interfaz.ui",self)
        self.llenarTabla(dt_estudiante.Dt_Estudiantes.listarEstudiantes())

        #Acciones de los botones
        self.BT_Guardar.clicked.connect(self.guardarEstudiantes)
        self.BT_Editar.clicked.connect(self.editarEstudiantes)
        self.BT_Limpiar.clicked.connect(self.limpiarCampos)

    #Guarda los registros a la base de datos
    def guardarEstudiantes(self):
        if not self.Line_Nombre.text()== "" and not self.Line_Apellido.text()== "" and not self.Line_Grado.text()== "":

            self.indicador = 1 # Se coloca el 1 como modificador a la hora de entrar a la función de Notificación, en donde asegura que el usuario ingreso los datos correctamente

            dt_estudiante.Dt_Estudiantes.agregarEstudiante(self.Line_Nombre.text(),self.Line_Apellido.text(), int(self.Line_Grado.text())) #Recoge los datos en los "Lines" de Qt Desinger para guardarlos en la base de datos
            self.notifMensaje(self.indicador, "guardados") # Se pasa por parametro el indicador que en este caso vale "1" y el resultado es que se guardo correctamente en la base de datos
            self.limpiarCampos()
            self.llenarTabla(dt_estudiante.Dt_Estudiantes.listarEstudiantes())
        else:
            self.notifMensaje( 0, "")

    #Editar los registros de la base de datos
    def editarEstudiantes(self):
        if not self.Line_Nombre.text()== "" and not self.Line_Apellido.text()== "" and not self.Line_Grado.text()== "":
            self.indicador = 1 #Se coloca el 1 como modificador a la hora de entrar a la función de Notificación, en donde asegura que el usuario ingreso los datos correctamente
            dt_estudiante.Dt_Estudiantes.editarEstudiante(int(self.Line_Id.text()),self.Line_Nombre.text(),self.Line_Apellido.text(), int(self.Line_Grado.text()))
            self.notifMensaje(self.indicador)
            self.llenarTabla(dt_estudiante.Dt_Estudiantes.listarEstudiantes(), "Editados") # Se pasa por parametro el indicador que en este caso vale "1" y el resultado es que se edito correctamente en la base de datos

        else:
            self.notifMensaje( 0, "")

    #Mensaje a pantalla que notifica al usuario si ingreso los datos correctamente validado
    def notifMensaje(self,indicador, resultado):
        if indicador == 1:
            QMessageBox.about(self, "Registrado", "Datos "+resultado+" correctamente")

        else:
            QMessageBox.about(self, "Error", "Error de registros de datos")

    def llenarTabla(self,datos):
        print("Datos de la Tablas")
        i=len(datos)
        self.TB_Estudiantes.setRowCount(i)
        tablerow = 0

        for row in datos:
            print(row)
            print(row["idestudiantes"])
            self.TB_Estudiantes.setItem(tablerow, 0,QTableWidgetItem((row["idestudiantes"])))
            self.TB_Estudiantes.setItem(tablerow, 1,QTableWidgetItem((row["nombre"])))
            self.TB_Estudiantes.setItem(tablerow, 2, QTableWidgetItem((row["apellido"])))
            self.TB_Estudiantes.setItem(tablerow, 3, QTableWidgetItem((row["grado"])))
            tablerow = tablerow + 1

    def limpiarCampos(self): # Limpia los "Lines" de Qt Desinger
        self.Line_Nombre.clear()
        self.Line_Apellido.clear()
        self.Line_Grado.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    aplicacion = Form_Estudiante()
    aplicacion.show()
    app.exec()

