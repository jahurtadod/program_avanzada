# 01-Calculadora-avanzada.py
# Calculadora Avanzada y Mejorada por stefany sancho 

print("Bienvenido a la calculadora mejorada")

def mostrar_menu():
    print("\n=== Calculadora Avanzada y Mejorada ===")
    print("Operaciones disponibles: + -  *  /")
    print("Escribe 'salir' en cualquier momento para terminar\n")

 
# Mejoras Función para pedir un número al usuario, con manejo de excepciones
def obtener_numero(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.lower() == "salir":
            return "salir"
        
        # Validar si la entrada es un número 
        # Se usa try/except para que la aplicación no se rompa si el usuario pone letras 
        try:
            return float(entrada)
        except ValueError:
            print(" Error: Ingrese un número válido.")

     # Mejoras Función para una operación válida
def obtener_operacion(operaciones):
    while True:
        oper = input("Ingresa la operación (+, -, *, /): ")
        if oper.lower() == "salir":
            return "salir"
        if oper in operaciones:
            return oper
        else:
            print(" Operación no válida. Usa solo: +, -, *, /")

  # Mejoras Función para calcular el resultado 
  # incluye validación de división entre cero

def calcular(n1, n2, oper):
    try:
        operaciones = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b if b != 0 else "Error: División por cero"
        }
        resultado = operaciones[oper](n1, n2)
        return resultado
    except Exception as e:
        return f"Error inesperado: {e}"
    
# Mejoras realizadas usa funciones y control de bucles
         
def main():
    mostrar_menu()
    operaciones_validas = ("+", "-", "*", "/")  

    while True:
        n1 = obtener_numero("Ingresa el número 1: ")
        if n1 == "salir":
            break

        oper = obtener_operacion(operaciones_validas)
        if oper == "salir":
            break

        n2 = obtener_numero("Ingresa el número 2: ")
        if n2 == "salir":
            break

        resultado = calcular(n1, n2, oper)
        print(f" Resultado de {n1} {oper} {n2} = {resultado}")

    print("\nGracias por usar la calculadora. ¡Hasta pronto!")


if __name__ == "__main__":
    main()
