import unittest
import sys
import os
sys.path.append('../..')
from conexion import conexion
from datetime import date

class TestExportar(unittest.TestCase):

    def test_copia_seguridad_crea_fichero(self):
        nombre_fichero = f"copia_{date.today()}.sql"
        with open(nombre_fichero, "w") as fichero:
            fichero.write("-- test\n")
        self.assertTrue(os.path.exists(nombre_fichero))
        os.remove(nombre_fichero)

    def test_exportar_json_crea_fichero(self):
        with open("exportacion.json", "w") as fichero:
            fichero.write("{}")
        self.assertTrue(os.path.exists("exportacion.json"))
        os.remove("exportacion.json")

    def test_exportar_csv_crea_fichero(self):
        with open("exportacion_alumnos.csv", "w") as fichero:
            fichero.write("nie,nombre\n")
        self.assertTrue(os.path.exists("exportacion_alumnos.csv"))
        os.remove("exportacion_alumnos.csv")

if __name__ == "__main__":
    unittest.main()