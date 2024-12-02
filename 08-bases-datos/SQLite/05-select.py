import sqlite3

with sqlite3.connect("08-bases-datos/app.db") as con:
    cursor = con.cursor()
    cursor.execute("select * from usuarios")
    # print(cursor.fetchone())
    print(cursor.fetchall())
