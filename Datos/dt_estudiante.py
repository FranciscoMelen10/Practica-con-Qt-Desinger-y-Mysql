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
                print("Guardado")

            except Exception as ex:
                print(f"Error: {ex}")

        @classmethod
        def editarEstudiante(cls,id ,nombre, apellido, grado):
            try:
                cursor = Conexion.Conexion.obtenerConexion().cursor()
                sql = (f'''UPDATE estudiantes SET nombre = "{nombre}" , apellido = "{apellido}" , grado = "{grado}" WHERE idestudiantes = {id}''')
                cursor.execute(sql)
                cursor.connection.commit()
                cursor.close()
                print("Editado")

            except Exception as ex:
                print(f"Error: {ex}")


        @classmethod
        def eliminarEstudiante(cls,id):
            try:
                cursor = Conexion.Conexion.obtenerConexion().cursor()
                sql = (f'''DELETE FROM estudiantes WHERE idestudiantes = {id}''')
                cursor.execute(sql)
                cursor.connection.commit()
                cursor.close()
                print("Eliminado")

            except Exception as ex:
                print(f"Error: {ex}")