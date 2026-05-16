from conexion import conexion

def listar_alumnos():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT nie, nombre, apellidos, tramo, bilingue FROM alumnos")
        alumnos = cursor.fetchall()

        if len(alumnos) == 0:
            print("No hay alumnos en la base de datos")
            return

        for alumno in alumnos:
            print(f"{alumno[0]} - {alumno[2]}, {alumno[1]} - Tramo: {alumno[3]} - Bilingue: {alumno[4]}")
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