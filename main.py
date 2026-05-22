from src.alumnos import listar_alumnos, crear_alumno, modificar_alumno, buscar_alumnos, eliminar_alumno
from src.libros import listar_libros, crear_libro, modificar_libro, eliminar_libro, buscar_libros
from src.materias import listar_materias, crear_materia, modificar_materia, eliminar_materia
from src.cursos import listar_cursos, crear_curso, modificar_curso, eliminar_curso
from src.prestamos import asignar_libros, cerrar_prestamo, generar_contrato, registrar_devolucion, buscar_prestamos, cambiar_estado_libro, ver_prestamos
from src.carga import cargar_alumnos, vaciar_bbdd
from src.exportar import copia_seguridad, exportar_datos, exportar_listados

USUARIO = "admin"
PASSWORD = "1234"

def login():
    print("=== Banco de Libros ===")
    usuario = input("Usuario: ")
    password = input("Contrasena: ")

    if usuario == USUARIO and password == PASSWORD:
        print("Acceso correcto")
        return True
    else:
        print("Usuario o contrasena incorrectos")
        return False

def mostrar_menu():
    print("Banco de Libros")
    print("1. Gestion de alumnos")
    print("2. Gestion de libros")
    print("3. Gestion de materias")
    print("4. Gestion de cursos")
    print("5. Gestion de prestamos")
    print("6. Carga de datos")
    print("7. Copia de seguridad")
    print("8. Exportar datos")
    print("9. Cerrar sesion")
    print("10. Salir")

def main():
    while True:
        if not login():
            continue

        while True:
            mostrar_menu()
            opcion = input("Escoge: ")

            if opcion == "1":
                print("1. Listar alumnos")
                print("2. Crear alumno")
                print("3. Modificar alumno")
                print("4. Eliminar alumno")
                print("5. Buscar alumnos")
                print("0. Volver")
                sub = input("Elige una opcion: ")
                if sub == "1":
                    listar_alumnos()
                elif sub == "2":
                    crear_alumno()
                elif sub == "3":
                    modificar_alumno()
                elif sub == "4":
                    eliminar_alumno()
                elif sub == "5":
                    buscar_alumnos()
            elif opcion == "2":
                print("1. Listar libros")
                print("2. Crear libro")
                print("3. Modificar libro")
                print("4. Eliminar libro")
                print("5. Buscar libros")
                print("0. Volver")
                sub = input("Elige una opcion: ")
                if sub == "1":
                    listar_libros()
                elif sub == "2":
                    crear_libro()
                elif sub == "3":
                    modificar_libro()
                elif sub == "4":
                    eliminar_libro()
                elif sub == "5":
                    buscar_libros()
            elif opcion == "3":
                print("1. Listar materias")
                print("2. Crear materia")
                print("3. Modificar materia")
                print("4. Eliminar materia")
                print("0. Volver")
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
                print("0. Volver")
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
                print("4. Buscar prestamos")
                print("5. Cambiar estado de libro")
                print("6. Generar contrato")
                print("7. Cerrar prestamo")
                print("0. Volver")
                sub = input("Elige una opcion: ")
                if sub == "1":
                    asignar_libros()
                elif sub == "2":
                    ver_prestamos()
                elif sub == "3":
                    registrar_devolucion()
                elif sub == "4":
                    buscar_prestamos()
                elif sub == "5":
                    cambiar_estado_libro()
                elif sub == "6":
                    generar_contrato()
                elif sub == "7":
                    cerrar_prestamo()
            elif opcion == "6":
                print("1. Cargar alumnos desde CSV")
                print("2. Vaciar BBDD")
                print("0. Volver")
                sub = input("Elige una opcion: ")
                if sub == "1":
                    cargar_alumnos()
                elif sub == "2":
                    vaciar_bbdd()
            elif opcion == "7":
                copia_seguridad()
            elif opcion == "8":
                print("1. Exportar datos para curso siguiente")
                print("2. Exportar listados")
                print("0. Volver")
                sub = input("Elige una opcion: ")
                if sub == "1":
                    exportar_datos()
                elif sub == "2":
                    exportar_listados()
            elif opcion == "9":
                print("Sesion cerrada")
                break
            elif opcion == "10":
                print("Salir")
                return
            else:
                print("Opcion no valida")

main()