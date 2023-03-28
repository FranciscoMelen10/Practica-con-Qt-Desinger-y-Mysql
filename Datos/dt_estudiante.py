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
        def agregarEstudiante(cls, id, nombre, apellido, grado):
            try:
                cursor = Conexion.Conexion.obtenerConexion().cursor()
                sql = (f'''INSERT INTO estudiantes ( idestudiantes, nombre, apellido, grado) VALUES ('{id}','{nombre}','{apellido}','{grado}')''')
                cursor.execute(sql)
                cursor.connection.commit()
                cursor.close()
                print("Registrado")

            except Exception as ex:
                print(f"Error: {ex}")


