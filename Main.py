import Conexion
from PyQt5 import QtWidgets,uic

Conexion.Conexion.AgregarEstudiante()

def prueba_boton():
    print("Sos tuani")

aplicacion = QtWidgets.QApplication([])

#ventana del PyQt5
ventana = uic.loadUi("Interfaz.ui")

#Obtener texto de los Line edits
h = ventana.Line_Id.text()
print(h)

#Interaccion con el boton
ventana.BT_Guardar.clicked.connect(prueba_boton)

#Ejecutar ventana de PyQt5
ventana.show()
aplicacion.exec()





