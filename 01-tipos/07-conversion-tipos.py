#Sistema mejorado por Nicole Calvas
# Solicitar entrada al usuario
x = input("Ingresa un valor: ")

# Validar y convertir el valor a diferentes tipos de datos
try:
    # Intentar convertir el string a un número entero
    numero_entero = int(x)
except ValueError:
    # Si no es un número entero, asignar None
    numero_entero = None

try:
    # Intentar convertir el string a un número flotante
    numero_flotante = float(x)
except ValueError:
    # Si no es un número flotante, asignar None
    numero_flotante = None

# Convertir el valor a un string (esto siempre es válido)
texto = str(x)

# Evaluar el valor booleano de la entrada
# Nota: bool(x) es True para cualquier entrada no vacía, excepto valores como "" o 0
valor_booleano = bool(x)

# Mostrar los resultados al usuario
print(f"\nEntrada original: '{x}'")
if numero_entero is not None:
    print(f"Como entero: {numero_entero}")
else:
    print("Como entero: No válido (no es un número entero)")

if numero_flotante is not None:
    print(f"Como flotante: {numero_flotante}")
else:
    print("Como flotante: No válido (no es un número flotante)")

print(f"Como string: '{texto}'")
print(f"Como booleano: {valor_booleano}")

# Explicación adicional sobre valores booleanos en Python
print("\nEjemplos de evaluación booleana:")
print(f"bool(''): {bool('')}  # Cadena vacía -> False")
print(f"bool('0'): {bool('0')}  # Cadena con '0' -> True (cadena no vacía)")
print(f"bool(None): {bool(None)}  # None -> False")
print(f"bool(' '): {bool(' ')}  # Espacio en blanco -> True (cadena no vacía)")
print(f"bool(0): {bool(0)}  # Cero -> False (valor numérico Falsy)")

# Proporcionar una salida clara para usuarios que no conozcan los conceptos técnicos
print("\nNotas:")
print("- Un string vacío ('') se evalúa como False en booleanos.")
print("- Cualquier string no vacío (incluido '0' o ' ') se evalúa como True.")
print("- El número 0 se evalúa como False, mientras que otros números son True.")
