import sqlite3

with sqlite3.connect("08-bases-datos/app.db") as con:
    cursor = con.cursor()
    # SQL injection
    cursor.execute(
        "insert into usuarios values(?, ?)",
        (1, "Jorge Hurtado"),  # Turpla
    )

# Hacer un insert multiple
with sqlite3.connect("08-bases-datos/app.db") as con:
    cursor = con.cursor()
    usuarios = [
        (2, "Jeanne D'Arc"),
        (3, "Gintoki Sakata"),
    ]
    cursor.executemany(
        "insert into usuarios values(?, ?)",
        usuarios,
    )
