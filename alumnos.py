from conexion import conexion

def listar_alumnos():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT nie, nombre, apellidos, tramo, bilingue FROM alumnos")
        alumnos = cursor.fetchall()

        if len(alumnos) == 0:
            print("No hay alumnos en la base de datos")
            return

        for i, alumno in enumerate(alumnos, 1):
            print(f"{i}. {alumno[2]}, {alumno[1]} - Tramo: {alumno[3]} - Bilingue: {alumno[4]}")
    except mysql.connector.Error as e:
        print(f"Error al obtener los alumnos: {e}")

def crear_alumno():
    nie = input("NIE del alumno: ")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    tramo = input("Tramo (0, I, II): ")
    bilingue = input("Bilingue (s/n): ")

    bilingue_valor = 1 if bilingue.lower() == "s" else 0

    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO alumnos (nie, nombre, apellidos, tramo, bilingue) VALUES (%s, %s, %s, %s, %s)",
            (nie, nombre, apellidos, tramo, bilingue_valor)
        )
        conexion.commit()
        print("Alumno creado correctamente")
    except mysql.connector.Error as e:
        print(f"Error al crear el alumno: {e}")


def modificar_alumno():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM alumnos")
        alumnos = cursor.fetchall()

        if len(alumnos) == 0:
            print("No hay alumnos en la base de datos")
            return

        listar_alumnos()
        numero = int(input("Numero del alumno a modificar: "))
        alumno = alumnos[numero - 1]

        nombre = input("Nuevo nombre: ")
        apellidos = input("Nuevos apellidos: ")
        tramo = input("Nuevo tramo (0, I, II): ")
        bilingue = input("Bilingue (s/n): ")
        bilingue_valor = 1 if bilingue.lower() == "s" else 0

        cursor.execute(
            "UPDATE alumnos SET nombre = %s, apellidos = %s, tramo = %s, bilingue = %s WHERE nie = %s",
            (nombre, apellidos, tramo, bilingue_valor, alumno[0])
        )
        conexion.commit()
        print("Alumno modificado correctamente")
    except mysql.connector.Error as e:
        print(f"Error al modificar el alumno: {e}")


def eliminar_alumno():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM alumnos")
        alumnos = cursor.fetchall()

        if len(alumnos) == 0:
            print("No hay alumnos en la base de datos")
            return

        listar_alumnos()
        numero = int(input("Numero del alumno a eliminar: "))
        alumno = alumnos[numero - 1]

        confirmar = input(f"Seguro que quieres eliminar a {alumno[2]}, {alumno[1]}? (s/n): ")
        if confirmar.lower() != "s":
            print("Operacion cancelada")
            return

        cursor.execute("DELETE FROM alumnos WHERE nie = %s", (alumno[0],))
        conexion.commit()
        print("Alumno eliminado correctamente")
    except mysql.connector.Error as e:
        print(f"Error al eliminar el alumno: {e}")