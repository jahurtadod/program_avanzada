def es_numero_valido(entrada):
    try:
        return float(entrada)
    except ValueError:
        return None

def obtener_operacion():
    operaciones = ["+", "-", "*", "/"]
    while True:
        oper = input("Ingresa la operación (+, -, *, /) o escribe 'salir' para terminar: ")
        if oper.lower() == "salir":
            return None
        if oper in operaciones:
            return oper
        print("Operación no válida. Intenta con +, -, * o /.")

def calculadora():
    print("Bienvenido a la calculadora")

    while True:
        n1 = input("Ingresa el número 1 (o escribe 'salir' para terminar): ")
        if n1.lower() == "salir":
            print("Programa terminado.")
            break

        n1 = es_numero_valido(n1)
        if n1 is None:
            print("Por favor, ingresa un número válido.")
            continue

        oper = obtener_operacion()
        if oper is None:
            print("Programa terminado.")
            break

        n2 = input("Ingresa el número 2 (o escribe 'salir' para terminar): ")
        if n2.lower() == "salir":
            print("Programa terminado.")
            break

        n2 = es_numero_valido(n2)
        if n2 is None:
            print("Por favor, ingresa un número válido.")
            continue

        if oper == '/' and n2 == 0:
            print("Error: no se puede dividir entre cero.")
            continue

        resultado = eval(f"{n1} {oper} {n2}")
        print(f"El resultado de {n1} {oper} {n2} es: {resultado}")

calculadora()
