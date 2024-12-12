"""Ejercicio Calculadora NC con historial y logaritmo"""
import math

# Definición de funciones para operaciones
# Tomar en cuenta las buenas practicas

def sumar(x, y):
    """Se suma"""
    return x + y


def restar(x, y):
    return x - y


def multiplicar(x, y):
    return x * y


def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: División por cero"


def potencia(x, y):
    return x ** y


def modulo(x, y):
    return x % y


def seno(x):
    return math.sin(math.radians(x))


def coseno(x):
    return math.cos(math.radians(x))


def tangente(x):
    return math.tan(math.radians(x))


def logaritmo(x):
    if x > 0:
        return math.log(x)
    else:
        return "Error: El logaritmo solo está definido para números positivos"


# Lista para almacenar el historial de operaciones
historial = []

# Función principal de la calculadora


def calculadora_avanzada():
    print("Bienvenido a la calculadora de NC")
    print("Opciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Módulo")
    print("7. Seno")
    print("8. Coseno")
    print("9. Tangente")
    print("10. Ver Historial")
    print("11. Logaritmo")
    print("12. Salir")

    while True:
        opcion = input("Selecciona una operación (1-12): ")

        if opcion == "12":
            print("Gracias por usar la calculadora avanzada. ¡Adiós!")
            break

        # Operaciones binarias (requieren dos números)
        if opcion in ["1", "2", "3", "4", "5", "6"]:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Error: Ingresa valores numéricos válidos.")
                continue
# guardar en otro lugar el historial, ahorar una linea de codigo en cada if
            if opcion == "1":
                resultado = sumar(num1, num2)
                print("Resultado:", resultado)
                historial.append(f"Suma: {num1} + {num2} = {resultado}")
            elif opcion == "2":
                resultado = restar(num1, num2)
                print("Resultado:", resultado)
                historial.append(f"Resta: {num1} - {num2} = {resultado}")
            elif opcion == "3":
                resultado = multiplicar(num1, num2)
                print("Resultado:", resultado)
                historial.append(f"Multiplicación: {
                                 num1} * {num2} = {resultado}")
            elif opcion == "4":
                resultado = dividir(num1, num2)
                print("Resultado:", resultado)
                historial.append(f"División: {num1} / {num2} = {resultado}")
            elif opcion == "5":
                resultado = potencia(num1, num2)
                print("Resultado:", resultado)
                historial.append(f"Potencia: {num1} ** {num2} = {resultado}")
            elif opcion == "6":
                resultado = modulo(num1, num2)
                print("Resultado:", resultado)
                historial.append(f"Módulo: {num1} % {num2} = {resultado}")

        # Operaciones unarias (requieren solo un número)
        elif opcion in ["7", "8", "9", "11"]:
            try:
                if opcion == "11":
                    num = float(input("Ingresa el número para el logaritmo: "))
                else:
                    num = float(input("Ingresa el ángulo en grados: "))
            except ValueError:
                print("Error: Ingresa un valor numérico válido.")
                continue

            if opcion == "7":
                resultado = seno(num)
                print("Resultado (seno):", resultado)
                historial.append(f"Seno: sin({num}) = {resultado}")
            elif opcion == "8":
                resultado = coseno(num)
                print("Resultado (coseno):", resultado)
                historial.append(f"Coseno: cos({num}) = {resultado}")
            elif opcion == "9":
                resultado = tangente(num)
                print("Resultado (tangente):", resultado)
                historial.append(f"Tangente: tan({num}) = {resultado}")
            elif opcion == "11":
                resultado = logaritmo(num)
                print("Resultado (logaritmo):", resultado)
                historial.append(f"Logaritmo: log({num}) = {resultado}")

        # Ver historial de operaciones
        elif opcion == "10":
            print("Historial de operaciones:")
            for operacion in historial:
                print(operacion)

        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 12.")


# Ejecutar la calculadora
calculadora_avanzada()
