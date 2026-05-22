import mysql.connector
from conexion import conexion

def listar_cursos():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT curso, nivel FROM cursos")
        cursos = cursor.fetchall()

        if len(cursos) == 0:
            print("No hay cursos en la base de datos")
            return

        for i, curso in enumerate(cursos, 1):
            print(f"{i}. {curso[1]} - {curso[0]}")
    except mysql.connector.Error as e:
        print(f"Error al obtener los cursos: {e}")


def crear_curso():
    curso = input("Codigo del curso (ej: 1A): ")
    nivel = input("Nivel (ej: 1eso): ")

    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO cursos (curso, nivel) VALUES (%s, %s)",
            (curso, nivel)
        )
        conexion.commit()
        print("Curso creado correctamente")
    except mysql.connector.Error as e:
        print(f"Error al crear el curso: {e}")


def modificar_curso():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM cursos")
        cursos = cursor.fetchall()

        if len(cursos) == 0:
            print("No hay cursos en la base de datos")
            return

        listar_cursos()
        numero = int(input("Numero del curso a modificar: "))
        curso = cursos[numero - 1]

        nivel = input("Nuevo nivel: ")

        cursor.execute(
            "UPDATE cursos SET nivel = %s WHERE curso = %s",
            (nivel, curso[0])
        )
        conexion.commit()
        print("Curso modificado correctamente")
    except mysql.connector.Error as e:
        print(f"Error al modificar el curso: {e}")


def eliminar_curso():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM cursos")
        cursos = cursor.fetchall()

        if len(cursos) == 0:
            print("No hay cursos en la base de datos")
            return

        listar_cursos()
        numero = int(input("Numero del curso a eliminar: "))
        curso = cursos[numero - 1]

        confirmar = input(f"Seguro que quieres eliminar {curso[1]}? (s/n): ")
        if confirmar.lower() != "s":
            print("Operacion cancelada")
            return

        cursor.execute("DELETE FROM cursos WHERE curso = %s", (curso[0],))
        conexion.commit()
        print("Curso eliminado correctamente")
    except mysql.connector.Error as e:
        print(f"Error al eliminar el curso: {e}")