import Entidades
from Datos import Conexion
from Entidades import estudiantes

class Dt_Estudiantes:


    @classmethod
    def listarEstudiantes(cls):
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        cursor.execute("SELECT * FROM estudiantes")
        querys = cursor.fetchall()
        return querys




    @classmethod
    def agregarEstudiante(cls, estu):
        try:
            cursor = Conexion.Conexion.getCursor()
            sql = (f'''INSERT INTO estudiantes ( idestudiantes, nombre, apellido, grado) VALUES ('{Entidades.estudiantes.Estudiantes.getId()}','{Entidades.estudiantes.Estudiantes.getName()}','{Entidades.estudiantes.Estudiantes.getApellido()}','{Entidades.estudiantes.Estudiantes.getGrado()}')''')
            cursor.execute(sql)
            cursor.connection.commit()
            print("Registrado")

        except Exception as ex:
            print("Error: " + ex)


