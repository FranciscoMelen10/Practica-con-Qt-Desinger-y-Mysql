from Datos import Conexion

class Dt_Estudiantes:


    @classmethod
    def listarEstudiantes(cls):
        cursor = Conexion.obtenerConexion().cursor()
        cursor.execute("SELECT * FROM estudiantes")
        querys = cursor.fetchall()
        print(querys)
        return querys




    @classmethod
    def agregarEstudiante(cls, estu):
        try:
            cursor = cls.obtenerConexion().cursor()
            sql = (f"INSERT INTO estudiantes ( idestudiantes, nombre, apellido, grado) VALUES ('4', 'mario', 'simon', '2')")
            cursor.execute(sql)
            cursor.connection.commit()
            print("Registrado")

        except Exception as ex:
            print("Error: " + ex)


