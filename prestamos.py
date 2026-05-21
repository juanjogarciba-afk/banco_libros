import mysql.connector
from conexion import conexion
from datetime import date

def asignar_libros():
    try:
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM alumnos")
        alumnos = cursor.fetchall()

        if len(alumnos) == 0:
            print("No hay alumnos en la base de datos")
            return

        i = 1
        for alumno in alumnos:
            print(f"{i}. {alumno[2]}, {alumno[1]}")
            i += 1
        numero_alumno = int(input("Elige un alumno: "))
        alumno = alumnos[numero_alumno - 1]

        cursor.execute("SELECT * FROM cursos")
        cursos = cursor.fetchall()

        if len(cursos) == 0:
            print("No hay cursos en la base de datos")
            return

        i = 1
        for curso in cursos:
            print(f"{i}. {curso[1]} - {curso[0]}")
            i += 1
        numero_curso = int(input("Elige el curso del alumno: "))
        curso = cursos[numero_curso - 1]

        cursor.execute("SELECT * FROM libros WHERE id_curso = %s", (curso[0],))
        libros = cursor.fetchall()

        if len(libros) == 0:
            print("No hay libros para este curso")
            return

        print("Libros del curso:")
        i = 1
        for libro in libros:
            print(f"{i}. {libro[1]} - {libro[2]}")
            i += 1

        seleccion = input("Elige los libros a prestar (ej: 1,2,3): ")
        indices = seleccion.split(",")

        for indice in indices:
            libro = libros[int(indice) - 1]
            cursor.execute(
                "INSERT INTO alumnoscursoslibros (nie, curso, isbn, fecha_entrega, fecha_devolucion, estado) VALUES (%s, %s, %s, %s, %s, %s)",
                (alumno[0], curso[0], libro[0], date.today(), None, "P")
            )

        conexion.commit()
        print("Libros asignados correctamente")
    except mysql.connector.Error as e:
        print(f"Error al asignar libros: {e}")
def ver_prestamos():
    try:
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM alumnos")
        alumnos = cursor.fetchall()

        if len(alumnos) == 0:
            print("No hay alumnos en la base de datos")
            return

        i = 1
        for alumno in alumnos:
            print(f"{i}. {alumno[2]}, {alumno[1]}")
            i += 1
        numero_alumno = int(input("Elige un alumno: "))
        alumno = alumnos[numero_alumno - 1]

        cursor.execute(
            "SELECT acl.isbn, l.titulo, acl.fecha_entrega, acl.estado FROM alumnoscursoslibros acl JOIN libros l ON acl.isbn = l.isbn WHERE acl.nie = %s",
            (alumno[0],)
        )
        prestamos = cursor.fetchall()

        if len(prestamos) == 0:
            print("Este alumno no tiene prestamos")
            return

        i = 1
        for prestamo in prestamos:
            estado = "Prestado" if prestamo[3] == "P" else "Devuelto"
            print(f"{i}. {prestamo[1]} - Entregado: {prestamo[2]} - Estado: {estado}")
            i += 1

    except mysql.connector.Error as e:
        print(f"Error al ver prestamos: {e}")


def registrar_devolucion():
    try:
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM alumnos")
        alumnos = cursor.fetchall()

        if len(alumnos) == 0:
            print("No hay alumnos en la base de datos")
            return

        i = 1
        for alumno in alumnos:
            print(f"{i}. {alumno[2]}, {alumno[1]}")
            i += 1
        numero_alumno = int(input("Elige un alumno: "))
        alumno = alumnos[numero_alumno - 1]

        cursor.execute(
            "SELECT acl.isbn, l.titulo, acl.curso FROM alumnoscursoslibros acl JOIN libros l ON acl.isbn = l.isbn WHERE acl.nie = %s AND acl.estado = 'P'",
            (alumno[0],)
        )
        prestamos = cursor.fetchall()

        if len(prestamos) == 0:
            print("Este alumno no tiene prestamos pendientes")
            return

        i = 1
        for prestamo in prestamos:
            print(f"{i}. {prestamo[1]}")
            i += 1

        numero_prestamo = int(input("Elige el libro devuelto: "))
        prestamo = prestamos[numero_prestamo - 1]

        cursor.execute(
            "UPDATE alumnoscursoslibros SET estado = 'D', fecha_devolucion = %s WHERE nie = %s AND isbn = %s AND curso = %s",
            (date.today(), alumno[0], prestamo[0], prestamo[2])
        )
        conexion.commit()
        print("Devolucion registrada correctamente")

    except mysql.connector.Error as e:
        print(f"Error al registrar devolucion: {e}")

def buscar_prestamos():
    print("1. Buscar por alumno")
    print("2. Buscar por curso")
    print("3. Buscar por estado")
    print("4. Buscar por libro")
    sub = input("Elige un filtro: ")

    try:
        cursor = conexion.cursor()

        if sub == "1":
            texto = input("Nombre o apellidos del alumno: ")
            cursor.execute(
                "SELECT a.nombre, a.apellidos, l.titulo, acl.fecha_entrega, acl.estado FROM alumnoscursoslibros acl JOIN alumnos a ON acl.nie = a.nie JOIN libros l ON acl.isbn = l.isbn WHERE a.nombre LIKE %s OR a.apellidos LIKE %s",
                (f"%{texto}%", f"%{texto}%")
            )
        elif sub == "2":
            cursor.execute("SELECT * FROM cursos")
            cursos = cursor.fetchall()
            i = 1
            for curso in cursos:
                print(f"{i}. {curso[1]} - {curso[0]}")
                i += 1
            numero = int(input("Elige un curso: "))
            curso = cursos[numero - 1]
            cursor.execute(
                "SELECT a.nombre, a.apellidos, l.titulo, acl.fecha_entrega, acl.estado FROM alumnoscursoslibros acl JOIN alumnos a ON acl.nie = a.nie JOIN libros l ON acl.isbn = l.isbn WHERE acl.curso = %s",
                (curso[0],)
            )
        elif sub == "3":
            estado = input("Estado (P: Prestado, D: Devuelto): ")
            cursor.execute(
                "SELECT a.nombre, a.apellidos, l.titulo, acl.fecha_entrega, acl.estado FROM alumnoscursoslibros acl JOIN alumnos a ON acl.nie = a.nie JOIN libros l ON acl.isbn = l.isbn WHERE acl.estado = %s",
                (estado,)
            )
        elif sub == "4":
            texto = input("Titulo del libro: ")
            cursor.execute(
                "SELECT a.nombre, a.apellidos, l.titulo, acl.fecha_entrega, acl.estado FROM alumnoscursoslibros acl JOIN alumnos a ON acl.nie = a.nie JOIN libros l ON acl.isbn = l.isbn WHERE l.titulo LIKE %s",
                (f"%{texto}%",)
            )
        else:
            print("Opcion no valida")
            return

        prestamos = cursor.fetchall()

        if len(prestamos) == 0:
            print("No se han encontrado prestamos")
            return

        i = 1
        for prestamo in prestamos:
            estado = "Prestado" if prestamo[4] == "P" else "Devuelto"
            print(f"{i}. {prestamo[1]}, {prestamo[0]} - {prestamo[2]} - Entregado: {prestamo[3]} - Estado: {estado}")
            i += 1

    except mysql.connector.Error as e:
        print(f"Error al buscar prestamos: {e}")