import unittest
import sys
sys.path.append('../..')
from conexion import conexion

class TestCarga(unittest.TestCase):

    def test_carga_csv(self):
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO alumnos VALUES ('99999999Z', 'Test', 'Prueba', '0', 0)")
        conexion.commit()
        cursor.execute("SELECT * FROM alumnos WHERE nie = '99999999Z'")
        alumno = cursor.fetchone()
        self.assertIsNotNone(alumno)
        cursor.execute("DELETE FROM alumnos WHERE nie = '99999999Z'")
        conexion.commit()

    def test_carga_alumno_duplicado(self):
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

if __name__ == "__main__":
    unittest.main()