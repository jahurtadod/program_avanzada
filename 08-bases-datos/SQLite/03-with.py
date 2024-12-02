import sqlite3

with sqlite3.connect("08-bases-datos/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE if not exists usuarios
        (id INTEGER primary key, nombre VARCHAR(50));
        """
    )
