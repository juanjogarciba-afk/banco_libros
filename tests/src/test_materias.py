import unittest
import sys
sys.path.append('../..')
from conexion import conexion

class TestMaterias(unittest.TestCase):

    def test_materia_existe(self):
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO materias (nombre, departamento) VALUES ('Materia Test', 'Depto Test')")
        conexion.commit()
        cursor.execute("SELECT * FROM materias WHERE nombre = 'Materia Test'")
        materia = cursor.fetchone()
        self.assertIsNotNone(materia)
        cursor.execute("DELETE FROM materias WHERE nombre = 'Materia Test'")
        conexion.commit()

    def test_materia_no_existe(self):
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM materias WHERE nombre = 'Materia Inexistente'")
        materia = cursor.fetchone()
        self.assertIsNone(materia)

if __name__ == "__main__":
    unittest.main()