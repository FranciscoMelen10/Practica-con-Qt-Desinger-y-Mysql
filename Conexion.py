import pymysql.cursors

class Conexion:
    _DATABASE = 'Prueba_Estudiantes'
    _USERNAME = 'francisco'
    _PASSWORD = '1234'
    _HOST = 'localhost'
    _conexion = None
    _cursor = None

    @classmethod
    def AgregarEstudiante(cls):
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
            print("Error "+ e)

