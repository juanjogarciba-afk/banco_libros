import mysql.connector
from conexion import conexion

def listar_materias():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, departamento FROM materias")
        materias = cursor.fetchall()

        if len(materias) == 0:
            print("No hay materias en la base de datos")
            return

        for i, materia in enumerate(materias, 1):
            print(f"{i}. {materia[1]} - {materia[2]}")
    except mysql.connector.Error as e:
        print(f"Error al obtener las materias: {e}")


def crear_materia():
    nombre = input("Nombre de la materia: ")
    departamento = input("Departamento: ")

    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO materias (nombre, departamento) VALUES (%s, %s)",
            (nombre, departamento)
        )
        conexion.commit()
        print("Materia creada correctamente")
    except mysql.connector.Error as e:
        print(f"Error al crear la materia: {e}")


def modificar_materia():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM materias")
        materias = cursor.fetchall()

        if len(materias) == 0:
            print("No hay materias en la base de datos")
            return

        listar_materias()
        numero = int(input("Numero de la materia a modificar: "))
        materia = materias[numero - 1]

        nombre = input("Nuevo nombre: ")
        departamento = input("Nuevo departamento: ")

        cursor.execute(
            "UPDATE materias SET nombre = %s, departamento = %s WHERE id = %s",
            (nombre, departamento, materia[0])
        )
        conexion.commit()
        print("Materia modificada correctamente")
    except mysql.connector.Error as e:
        print(f"Error al modificar la materia: {e}")


def eliminar_materia():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM materias")
        materias = cursor.fetchall()

        if len(materias) == 0:
            print("No hay materias en la base de datos")
            return

        listar_materias()
        numero = int(input("Numero de la materia a eliminar: "))
        materia = materias[numero - 1]

        confirmar = input(f"Seguro que quieres eliminar {materia[1]}? (s/n): ")
        if confirmar.lower() != "s":
            print("Operacion cancelada")
            return

        cursor.execute("DELETE FROM materias WHERE id = %s", (materia[0],))
        conexion.commit()
        print("Materia eliminada correctamente")
    except mysql.connector.Error as e:
        print(f"Error al eliminar la materia: {e}")