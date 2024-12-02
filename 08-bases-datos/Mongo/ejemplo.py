from pymongo import MongoClient

# Conexión a la base de datos MongoDB


def connect_to_mongo():
    # Cambiar si es necesario
    client = MongoClient("mongodb://localhost:27017/")
    db = client["empresa"]
    return db["empleados"]

# Función para agregar un empleado


def agregar_empleado(collection):
    print("\nAgregar un nuevo empleado:")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    while True:
        try:
            edad = int(input("Edad: "))
            if edad < 0:
                raise ValueError("La edad debe ser positiva.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}")

    while True:
        try:
            sueldo = float(input("Sueldo: "))
            if sueldo < 0:
                raise ValueError("El sueldo debe ser positivo.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}")

    empleado = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "sueldo": sueldo
    }

    collection.insert_one(empleado)
    print("Empleado agregado exitosamente.\n")

# Función para listar todos los empleados


def listar_empleados(collection):
    print("\nLista de empleados:")
    empleados = collection.find()
    for emp in empleados:
        print(
            f"- {emp['nombre']} {emp['apellido']}, {emp['edad']} años, ${emp['sueldo']:.2f}")
    print()

# Función principal del programa


def main():
    collection = connect_to_mongo()

    while True:
        print("Menú:")
        print("1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Salir")
        empleados = collection.find()
        for emp in empleados:
            print(
                f"- {emp['nombre']} {emp['apellido']}, {emp['edad']} años, ${emp['sueldo']:.2f}")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_empleado(collection)
        elif opcion == "2":
            listar_empleados(collection)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")


if __name__ == "__main__":
    main()
