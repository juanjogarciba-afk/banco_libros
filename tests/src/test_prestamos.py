import unittest
import sys
sys.path.append('../..')
from conexion import conexion
from datetime import date

class TestPrestamos(unittest.TestCase):

    def test_prestamo_existe(self):
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO alumnos VALUES ('99999999Z', 'Test', 'Prueba', '0', 0)")
        cursor.execute("INSERT INTO cursos VALUES ('9Z', 'test')")
        cursor.execute("INSERT INTO materias (nombre, departamento) VALUES ('Materia Test', 'Depto Test')")
        conexion.commit()
        cursor.execute("SELECT id FROM materias WHERE nombre = 'Materia Test'")
        id_materia = cursor.fetchone()[0]
        cursor.execute("INSERT INTO libros VALUES ('000-0000000000', 'Libro Test', 'Autor Test', 5, %s, '9Z')", (id_materia,))
        cursor.execute("INSERT INTO alumnoscursoslibros VALUES ('99999999Z', '9Z', '000-0000000000', %s, NULL, 'P')", (date.today(),))
        conexion.commit()

        cursor.execute("SELECT * FROM alumnoscursoslibros WHERE nie = '99999999Z'")
        prestamo = cursor.fetchone()
        self.assertIsNotNone(prestamo)

        cursor.execute("DELETE FROM alumnoscursoslibros WHERE nie = '99999999Z'")
        cursor.execute("DELETE FROM libros WHERE isbn = '000-0000000000'")
        cursor.execute("DELETE FROM materias WHERE nombre = 'Materia Test'")
        cursor.execute("DELETE FROM cursos WHERE curso = '9Z'")
        cursor.execute("DELETE FROM alumnos WHERE nie = '99999999Z'")
        conexion.commit()

    def test_devolucion(self):
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO alumnos VALUES ('99999999Z', 'Test', 'Prueba', '0', 0)")
        cursor.execute("INSERT INTO cursos VALUES ('9Z', 'test')")
        cursor.execute("INSERT INTO materias (nombre, departamento) VALUES ('Materia Test', 'Depto Test')")
        conexion.commit()
        cursor.execute("SELECT id FROM materias WHERE nombre = 'Materia Test'")
        id_materia = cursor.fetchone()[0]
        cursor.execute("INSERT INTO libros VALUES ('000-0000000000', 'Libro Test', 'Autor Test', 5, %s, '9Z')", (id_materia,))
        cursor.execute("INSERT INTO alumnoscursoslibros VALUES ('99999999Z', '9Z', '000-0000000000', %s, NULL, 'P')", (date.today(),))
        conexion.commit()

        cursor.execute("UPDATE alumnoscursoslibros SET estado = 'D' WHERE nie = '99999999Z'")
        conexion.commit()
        cursor.execute("SELECT estado FROM alumnoscursoslibros WHERE nie = '99999999Z'")
        estado = cursor.fetchone()[0]
        self.assertEqual(estado, 'D')

        cursor.execute("DELETE FROM alumnoscursoslibros WHERE nie = '99999999Z'")
        cursor.execute("DELETE FROM libros WHERE isbn = '000-0000000000'")
        cursor.execute("DELETE FROM materias WHERE nombre = 'Materia Test'")
        cursor.execute("DELETE FROM cursos WHERE curso = '9Z'")
        cursor.execute("DELETE FROM alumnos WHERE nie = '99999999Z'")
        conexion.commit()

if __name__ == "__main__":
    unittest.main()