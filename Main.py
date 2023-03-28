from Datos import Conexion
from PyQt5 import QtWidgets,uic
from Datos import dt_estudiante

def llenarTabla(): #En testeo
    datos = dt_estudiante.Dt_Estudiantes.listarEstudiantes()
    ventana.TB_Estudiantes.setRowCount(len(datos))
    tablerow = 0

    for row in datos:
        #ventana.TB_Estudiantes.insertRow(tablarows)
        ventana.TB_Estudiantes.setItem(tablerow,0,QtWidgets.QTableWidgetItem)
        ventana.TB_Estudiantes.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
        ventana.TB_Estudiantes.setItem(tablerow,2 ,QtWidgets.QTableWidgetItem(row[3]))
        ventana.TB_Estudiantes.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
        tablerow += 1

def guardarEstudiantes():
    dt_estudiante.Dt_Estudiantes.agregarEstudiante(int(ventana.Line_Id.text()), ventana.Line_Nombre.text(), ventana.Line_Apellido.text(), int(ventana.Line_Grado.text()) )




#gGestiona todas las interacciones con la interfaz gráfica de usuario
aplicacion = QtWidgets.QApplication([])

#ventana del PyQt5
ventana = uic.loadUi("Interfaz.ui")

#Asignarle un titulo a la ventana
ventana.setWindowTitle("Estudiantes")

#Obtener texto de los Line edits
#h = ventana.Line_Id.text()
#print(h)

#Interaccion con el boton
ventana.BT_Guardar.clicked.connect(guardarEstudiantes)
#ventana.BT_Editar.clicked.connect(llenarTabla())


#Ejecutar ventana de PyQt5
if __name__ == '__main__':

    #Muestra la ventana
    ventana.show()

    #Mantiene en ejecución la interfaz
    aplicacion.exec()





