import mysql.connector
from conexion import conexion
import csv

def cargar_alumnos():
    ruta = input("Ruta del fichero CSV: ")

    try:
        with open(ruta, encoding="utf-8") as fichero:
            lector = csv.reader(fichero)
            next(lector)  # saltamos la cabecera

            cursor = conexion.cursor()
            errores = []

            for fila in lector:
                try:
                    alumno = fila[0].split(",")
                    apellidos = alumno[0].strip().replace('"', '')
                    nombre = alumno[1].strip().replace('"', '')
                    nie = fila[1].strip().replace('"', '')
                    tipo_beca = fila[17].strip().replace('"', '')

                    if tipo_beca == "I":
                        tramo = "I"
                    elif tipo_beca == "II":
                        tramo = "II"
                    else:
                        tramo = "0"

                    cursor.execute(
                        "INSERT INTO alumnos (nie, nombre, apellidos, tramo, bilingue) VALUES (%s, %s, %s, %s, %s)",
                        (nie, nombre, apellidos, tramo, 0)
                    )
                except Exception as e:
                    errores.append(f"Error en fila {fila}: {e}")

            conexion.commit()

            if len(errores) > 0:
                print("Se han producido los siguientes errores:")
                for error in errores:
                    print(error)
            else:
                print("Alumnos cargados correctamente")

    except FileNotFoundError:
        print("Fichero no encontrado")
    except mysql.connector.Error as e:
        print(f"Error al cargar los alumnos: {e}")