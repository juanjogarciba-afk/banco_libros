import mysql.connector
from conexion import conexion
from datetime import date

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