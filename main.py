from alumnos import listar_alumnos, crear_alumno, modificar_alumno, eliminar_alumno
from libros import listar_libros, crear_libro, modificar_libro, eliminar_libro

def mostrar_menu():
    print("Banco de Libros")
    print("1. Gestion de alumnos")
    print("2. Gestion de libros")
    print("3. Gestion de prestamos")
    print("4. Listados")
    print("5. Salir")

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
            print("Gestion de prestamos")
        elif opcion == "4":
            print("Listados")
        elif opcion == "5":
            print("Salir")
            break
        else:
            print("Opcion no valida")

main()