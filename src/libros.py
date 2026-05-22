import mysql.connector
from conexion import conexion

def listar_libros():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT isbn, titulo, autor, numero_ejemplares FROM libros")
        libros = cursor.fetchall()

        if len(libros) == 0:
            print("No hay libros en la base de datos")
            return

        for i, libro in enumerate(libros, 1):
            print(f"{i}. {libro[1]} - {libro[2]} - ISBN: {libro[0]} - Ejemplares: {libro[3]}")
    except mysql.connector.Error as e:
        print(f"Error al obtener los libros: {e}")


def crear_libro():
    isbn = input("ISBN: ")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    numero_ejemplares = input("Numero de ejemplares: ")

    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre FROM materias")
        materias = cursor.fetchall()
        for i, materia in enumerate(materias, 1):
            print(f"{i}. {materia[1]}")
        num_materia = int(input("Elige la materia: "))
        id_materia = materias[num_materia - 1][0]

        cursor.execute("SELECT curso, nivel FROM cursos")
        cursos = cursor.fetchall()
        for i, curso in enumerate(cursos, 1):
            print(f"{i}. {curso[1]} - {curso[0]}")
        num_curso = int(input("Elige el curso: "))
        id_curso = cursos[num_curso - 1][0]

        cursor.execute(
            "INSERT INTO libros (isbn, titulo, autor, numero_ejemplares, id_materia, id_curso) VALUES (%s, %s, %s, %s, %s, %s)",
            (isbn, titulo, autor, numero_ejemplares, id_materia, id_curso)
        )
        conexion.commit()
        print("Libro creado correctamente")
    except mysql.connector.Error as e:
        print(f"Error al crear el libro: {e}")
def modificar_libro():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM libros")
        libros = cursor.fetchall()

        if len(libros) == 0:
            print("No hay libros en la base de datos")
            return

        listar_libros()
        numero = int(input("Numero del libro a modificar: "))
        libro = libros[numero - 1]

        titulo = input("Nuevo titulo: ")
        autor = input("Nuevo autor: ")
        numero_ejemplares = input("Nuevo numero de ejemplares: ")

        cursor.execute(
            "UPDATE libros SET titulo = %s, autor = %s, numero_ejemplares = %s WHERE isbn = %s",
            (titulo, autor, numero_ejemplares, libro[0])
        )
        conexion.commit()
        print("Libro modificado correctamente")
    except mysql.connector.Error as e:
        print(f"Error al modificar el libro: {e}")


def eliminar_libro():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM libros")
        libros = cursor.fetchall()

        if len(libros) == 0:
            print("No hay libros en la base de datos")
            return

        listar_libros()
        numero = int(input("Numero del libro a eliminar: "))
        libro = libros[numero - 1]

        confirmar = input(f"Seguro que quieres eliminar {libro[1]}? (s/n): ")
        if confirmar.lower() != "s":
            print("Operacion cancelada")
            return

        cursor.execute("DELETE FROM libros WHERE isbn = %s", (libro[0],))
        conexion.commit()
        print("Libro eliminado correctamente")
    except mysql.connector.Error as e:
        print(f"Error al eliminar el libro: {e}")

def buscar_libros():
    print("1. Buscar por titulo")
    print("2. Buscar por autor")
    print("3. Buscar por curso")
    print("4. Buscar por materia")
    sub = input("Elige un filtro: ")

    try:
        cursor = conexion.cursor()

        if sub == "1":
            titulo = input("Titulo: ")
            cursor.execute(
                "SELECT isbn, titulo, autor, numero_ejemplares FROM libros WHERE titulo LIKE %s",
                (f"%{titulo}%",)
            )
        elif sub == "2":
            autor = input("Autor: ")
            cursor.execute(
                "SELECT isbn, titulo, autor, numero_ejemplares FROM libros WHERE autor LIKE %s",
                (f"%{autor}%",)
            )
        elif sub == "3":
            cursor.execute("SELECT * FROM cursos")
            cursos = cursor.fetchall()
            i = 1
            for curso in cursos:
                print(f"{i}. {curso[1]} - {curso[0]}")
                i += 1
            numero = int(input("Elige un curso: "))
            curso = cursos[numero - 1]
            cursor.execute(
                "SELECT isbn, titulo, autor, numero_ejemplares FROM libros WHERE id_curso = %s",
                (curso[0],)
            )
        elif sub == "4":
            cursor.execute("SELECT * FROM materias")
            materias = cursor.fetchall()
            i = 1
            for materia in materias:
                print(f"{i}. {materia[1]}")
                i += 1
            numero = int(input("Elige una materia: "))
            materia = materias[numero - 1]
            cursor.execute(
                "SELECT isbn, titulo, autor, numero_ejemplares FROM libros WHERE id_materia = %s",
                (materia[0],)
            )
        else:
            print("Opcion no valida")
            return

        libros = cursor.fetchall()

        if len(libros) == 0:
            print("No se han encontrado libros")
            return

        i = 1
        for libro in libros:
            print(f"{i}. {libro[1]} - {libro[2]} - ISBN: {libro[0]} - Ejemplares: {libro[3]}")
            i += 1

    except mysql.connector.Error as e:
        print(f"Error al buscar libros: {e}")