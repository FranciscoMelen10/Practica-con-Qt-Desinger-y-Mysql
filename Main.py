from Datos import Conexion
from PyQt5 import QtWidgets,uic
from Datos import dt_estudiante


def guardarEstudiantes(estu):
    print(dt_estudiante.Dt_Estudiantes.listarEstudiantes())




#gGestiona todas las interacciones con la interfaz gráfica de usuario
aplicacion = QtWidgets.QApplication([])

#ventana del PyQt5
ventana = uic.loadUi("Interfaz.ui")

#Asignarle un titulo a la ventana
ventana.setWindowTitle("Estudiantes")

#Obtener texto de los Line edits
h = ventana.Line_Id.text()
print(h)

#Interaccion con el boton
ventana.BT_Guardar.clicked.connect(guardarEstudiantes)


#Ejecutar ventana de PyQt5
if __name__ == '__main__':

    #Muestra la ventana
    ventana.show()
    #Mantiene en ejecución la interfaz
    aplicacion.exec()





