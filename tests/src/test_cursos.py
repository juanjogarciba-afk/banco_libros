import unittest
import sys
sys.path.append('../..')
from conexion import conexion

class TestCursos(unittest.TestCase):

    def test_curso_existe(self):
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO cursos VALUES ('9Z', 'test')")
        conexion.commit()
        cursor.execute("SELECT * FROM cursos WHERE curso = '9Z'")
        curso = cursor.fetchone()
        self.assertIsNotNone(curso)
        cursor.execute("DELETE FROM cursos WHERE curso = '9Z'")
        conexion.commit()

    def test_curso_no_existe(self):
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM cursos WHERE curso = '9X'")
        curso = cursor.fetchone()
        self.assertIsNone(curso)

    def test_curso_duplicado(self):
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO cursos VALUES ('9Z', 'test')")
        conexion.commit()
        error = False
        try:
            cursor.execute("INSERT INTO cursos VALUES ('9Z', 'test2')")
            conexion.commit()
        except:
            error = True
            conexion.rollback()
        self.assertTrue(error)
        cursor.execute("DELETE FROM cursos WHERE curso = '9Z'")
        conexion.commit()

if __name__ == "__main__":
    unittest.main()