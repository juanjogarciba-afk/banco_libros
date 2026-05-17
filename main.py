from alumnos import listar_alumnos, crear_alumno, modificar_alumno, eliminar_alumno
from libros import listar_libros, crear_libro, modificar_libro, eliminar_libro
from materias import listar_materias, crear_materia, modificar_materia, eliminar_materia
from cursos import listar_cursos, crear_curso, modificar_curso, eliminar_curso
from prestamos import asignar_libros, ver_prestamos, registrar_devolucion

def mostrar_menu():
    print("Banco de Libros")
    print("1. Gestion de alumnos")
    print("2. Gestion de libros")
    print("3. Gestion de materias")
    print("4. Gestion de cursos")
    print("5. Gestion de prestamos")
    print("7. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Escoge: ")

        if opcion == "1":
            print("1. Listar alumnos")
            print("2. Crear alumno")
            print("3. Modificar alumno")
            print("4. Eliminar alumno")
            sub = input("Elige una opcion: ")
            if sub == "1":
                listar_alumnos()
            elif sub == "2":
                crear_alumno()
            elif sub == "3":
                modificar_alumno()
            elif sub == "4":
                eliminar_alumno()
        elif opcion == "2":
            print("1. Listar libros")
            print("2. Crear libro")
            print("3. Modificar libro")
            print("4. Eliminar libro")
            sub = input("Elige una opcion: ")
            if sub == "1":
                listar_libros()
            elif sub == "2":
                crear_libro()
            elif sub == "3":
                modificar_libro()
            elif sub == "4":
                eliminar_libro()
        elif opcion == "3":
            print("1. Listar materias")
            print("2. Crear materia")
            print("3. Modificar materia")
            print("4. Eliminar materia")
            sub = input("Elige una opcion: ")
            if sub == "1":
                listar_materias()
            elif sub == "2":
                crear_materia()
            elif sub == "3":
                modificar_materia()
            elif sub == "4":
                eliminar_materia()
        elif opcion == "4":
            print("1. Listar cursos")
            print("2. Crear curso")
            print("3. Modificar curso")
            print("4. Eliminar curso")
            sub = input("Elige una opcion: ")
            if sub == "1":
                listar_cursos()
            elif sub == "2":
                crear_curso()
            elif sub == "3":
                modificar_curso()
            elif sub == "4":
                eliminar_curso()
        elif opcion == "5":
            print("1. Asignar libros")
            print("2. Ver prestamos")
            print("3. Registrar devolucion")
            sub = input("Elige una opcion: ")
            if sub == "1":
                 asignar_libros()
            elif sub == "2":
                ver_prestamos()
            elif sub == "3":
                registrar_devolucion()
        elif opcion == "6":
            print("Listados (en construccion)")
        elif opcion == "7":
            print("Salir")
            break
        else:
            print("Opcion no valida")

main()