import mysql.connector
from conexion import conexion
from datetime import date
import json
import csv

def copia_seguridad():
    try:
        cursor = conexion.cursor()
        nombre_fichero = f"copia_{date.today()}.sql"

        with open(nombre_fichero, "w") as fichero:

            cursor.execute("SELECT * FROM materias")
            for fila in cursor.fetchall():
                fichero.write(f"INSERT INTO materias (id, nombre, departamento) VALUES ('{fila[0]}', '{fila[1]}', '{fila[2]}');\n")

            cursor.execute("SELECT * FROM cursos")
            for fila in cursor.fetchall():
                fichero.write(f"INSERT INTO cursos (curso, nivel) VALUES ('{fila[0]}', '{fila[1]}');\n")

            cursor.execute("SELECT * FROM alumnos")
            for fila in cursor.fetchall():
                fichero.write(f"INSERT INTO alumnos (nie, nombre, apellidos, tramo, bilingue) VALUES ('{fila[0]}', '{fila[1]}', '{fila[2]}', '{fila[3]}', '{fila[4]}');\n")

            cursor.execute("SELECT * FROM libros")
            for fila in cursor.fetchall():
                fichero.write(f"INSERT INTO libros (isbn, titulo, autor, numero_ejemplares, id_materia, id_curso) VALUES ('{fila[0]}', '{fila[1]}', '{fila[2]}', '{fila[3]}', '{fila[4]}', '{fila[5]}');\n")

            cursor.execute("SELECT * FROM alumnoscursoslibros")
            for fila in cursor.fetchall():
                fichero.write(f"INSERT INTO alumnoscursoslibros (nie, curso, isbn, fecha_entrega, fecha_devolucion, estado) VALUES ('{fila[0]}', '{fila[1]}', '{fila[2]}', '{fila[3]}', '{fila[4]}', '{fila[5]}');\n")

        print(f"Copia de seguridad guardada en {nombre_fichero}")

    except mysql.connector.Error as e:
        print(f"Error al hacer la copia de seguridad: {e}")

def exportar_datos():
    print("1. Exportar en JSON")
    print("2. Exportar en CSV")
    print("3. Exportar en SQL")
    sub = input("Elige un formato: ")

    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT nie, nombre, apellidos, tramo, bilingue FROM alumnos")
        alumnos = cursor.fetchall()

        cursor.execute("SELECT curso, nivel FROM cursos")
        cursos = cursor.fetchall()

        if sub == "1":
            datos = {
                "alumnos": [{"nie": a[0], "nombre": a[1], "apellidos": a[2], "tramo": a[3], "bilingue": a[4]} for a in alumnos],
                "cursos": [{"curso": c[0], "nivel": c[1]} for c in cursos]
            }
            with open("exportacion.json", "w") as fichero:
                json.dump(datos, fichero, indent=4, default=str)
            print("Datos exportados en exportacion.json")

        elif sub == "2":
            with open("exportacion_alumnos.csv", "w", newline="") as fichero:
                writer = csv.writer(fichero)
                writer.writerow(["nie", "nombre", "apellidos", "tramo", "bilingue"])
                for alumno in alumnos:
                    writer.writerow(alumno)
            with open("exportacion_cursos.csv", "w", newline="") as fichero:
                writer = csv.writer(fichero)
                writer.writerow(["curso", "nivel"])
                for curso in cursos:
                    writer.writerow(curso)
            print("Datos exportados en exportacion_alumnos.csv y exportacion_cursos.csv")

        elif sub == "3":
            with open("exportacion.sql", "w") as fichero:
                for alumno in alumnos:
                    fichero.write(f"INSERT INTO alumnos (nie, nombre, apellidos, tramo, bilingue) VALUES ('{alumno[0]}', '{alumno[1]}', '{alumno[2]}', '{alumno[3]}', '{alumno[4]}');\n")
                for curso in cursos:
                    fichero.write(f"INSERT INTO cursos (curso, nivel) VALUES ('{curso[0]}', '{curso[1]}');\n")
            print("Datos exportados en exportacion.sql")

        else:
            print("Opcion no valida")

    except mysql.connector.Error as e:
        print(f"Error al exportar los datos: {e}")