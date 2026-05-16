import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="banco_libros"
)
print("Conexion exitosa")