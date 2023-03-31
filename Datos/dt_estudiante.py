from Datos import Conexion

class Dt_Estudiantes:

        @classmethod
        def listarEstudiantes(cls):
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            cursor.execute("SELECT * FROM estudiantes")
            querys = cursor.fetchall()
            cursor.close()
            return querys




        @classmethod
        def agregarEstudiante(cls, nombre, apellido, grado):
            try:
                cursor = Conexion.Conexion.obtenerConexion().cursor()
                sql = (f'''INSERT INTO estudiantes ( nombre, apellido, grado) VALUES ('{nombre}','{apellido}','{grado}')''')
                cursor.execute(sql)
                cursor.connection.commit()
                cursor.close()
                print("Registrado")

            except Exception as ex:
                print(f"Error: {ex}")