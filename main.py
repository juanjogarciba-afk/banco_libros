from alumnos import listar_alumnos, crear_alumno, modificar_alumno, eliminar_alumno


def mostrar_menu():
    print("Banco de Libros")
    print("1. Gestion de alumnos")
    print("2. Gestion de prestamos")
    print("3. Listados")
    print("4. Salir")

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
            print("Gestion de prestamos")
        elif opcion == "3":
            print("Listados")
        elif opcion == "4":
            print("Salir")
            break
        else:
            print("Opcion no valida")

main()