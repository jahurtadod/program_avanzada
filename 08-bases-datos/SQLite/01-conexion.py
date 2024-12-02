import sqlite3

# Creamos la conexion
con = sqlite3.connect("08-bases-datos/app.db")
# Recuerden siempre cerrar la conexión
con.close()
