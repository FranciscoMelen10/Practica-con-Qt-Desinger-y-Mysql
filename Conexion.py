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
            print("Error " + e)

        return cls._conexion

    @classmethod
    def listarEstudiantes(cls):
            cursor = cls.obtenerConexion().cursor()
            cursor.execute("SELECT * FROM estudiantes")
            resultados = cursor.fetchall()
            print(resultados)




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




