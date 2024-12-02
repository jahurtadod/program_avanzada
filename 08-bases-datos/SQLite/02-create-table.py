import sqlite3

con = sqlite3.connect("08-bases-datos/app.db")
# cursor es un objeto que actúa como un intermediario entre el programa y la base de datos
cursor = con.cursor()
cursor.execute(
    """
    CREATE TABLE if not exists usuarios
    (id INTEGER primary key, nombre VARCHAR(50));
    """
)
con.commit()

con.close()
