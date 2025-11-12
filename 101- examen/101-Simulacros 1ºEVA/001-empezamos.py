import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="Admin",
    password="Contrasena123$",
    database="portafolio_simulacro"
)

cursor = conexion.cursor()
