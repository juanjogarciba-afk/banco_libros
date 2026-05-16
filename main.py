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
            print("Gestion de alumnos ")
        elif opcion == "2":
            print("Gestion de prestamos ")
        elif opcion == "3":
            print("Listados")
        elif opcion == "4":
            print("Salir")
            break
        else:
            print("Opcion no valida")

main()