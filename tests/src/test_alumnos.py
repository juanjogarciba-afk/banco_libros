import unittest
import sys
sys.path.append('../..')
from conexion import conexion

class TestAlumnos(unittest.TestCase):

    def test_alumno_existe(self):
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO alumnos VALUES ('99999999Z', 'Test', 'Prueba', '0', 0)")
        conexion.commit()
        cursor.execute("SELECT * FROM alumnos WHERE nie = '99999999Z'")
        alumno = cursor.fetchone()
        self.assertIsNotNone(alumno)
        cursor.execute("DELETE FROM alumnos WHERE nie = '99999999Z'")
        conexion.commit()

    def test_alumno_no_existe(self):
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM alumnos WHERE nie = '00000000X'")
        alumno = cursor.fetchone()
        self.assertIsNone(alumno)

    def test_nie_duplicado(self):
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO alumnos VALUES ('99999999Z', 'Test', 'Prueba', '0', 0)")
        conexion.commit()
        error = False
        try:
            cursor.execute("INSERT INTO alumnos VALUES ('99999999Z', 'Test2', 'Prueba2', '0', 0)")
            conexion.commit()
        except:
            error = True
            conexion.rollback()
        self.assertTrue(error)
        cursor.execute("DELETE FROM alumnos WHERE nie = '99999999Z'")
        conexion.commit()

    def test_buscar_por_nombre(self):
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO alumnos VALUES ('99999999Z', 'Juan', 'Garcia', '0', 0)")
        conexion.commit()
        cursor.execute("SELECT * FROM alumnos WHERE nombre LIKE %s", ("%Juan%",))
        alumnos = cursor.fetchall()
        self.assertTrue(len(alumnos) > 0)
        cursor.execute("DELETE FROM alumnos WHERE nie = '99999999Z'")
        conexion.commit()

    def test_buscar_por_tramo(self):
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO alumnos VALUES ('99999999Z', 'Juan', 'Garcia', 'I', 0)")
        conexion.commit()
        cursor.execute("SELECT * FROM alumnos WHERE tramo = %s", ("I",))
        alumnos = cursor.fetchall()
        self.assertTrue(len(alumnos) > 0)
        cursor.execute("DELETE FROM alumnos WHERE nie = '99999999Z'")
        conexion.commit()

if __name__ == "__main__":
    unittest.main()