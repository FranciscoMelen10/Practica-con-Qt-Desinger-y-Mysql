import pymysql.cursors

class Conexion:
    #recolecta los datos de la BD
    _DATABASE = 'Prueba_Estudiantes'
    _USERNAME = 'francisco'
    _PASSWORD = '1234'
    _HOST = 'localhost'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):

            if cls._conexion is None:
                try:
                    cls._conexion = pymysql.connect(

                        user=cls._USERNAME,
                        password=cls._PASSWORD,
                        host=cls._HOST,
                        database=cls._DATABASE,
                        cursorclass=pymysql.cursors.DictCursor
                    )
                    print("Conectado mi shark")

                except Exception as e:
                    print(f"Error {e}")

            else:
                print("Si ya estabas conectado shark")

            return cls._conexion


    @classmethod
    def getCursor(cls):
        if cls._cursor is None:
            try:
                cls._conexion = cls.obtenerConexion().cursor()
                print(f"Tu cursos shark: {cls._conexion}")

            except Exception as e:
                print(f"Mira te salio esto mi shark:{e}")
        else:
            print("No hubo conexión a la DB")

        return cls._cursor


if __name__ == '__main__':
    print(Conexion.obtenerConexion())
