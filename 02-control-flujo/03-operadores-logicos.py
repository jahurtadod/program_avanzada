#Sistema mejorado por Nicole Calvas

# Definición de las variables
gas = False       # Variable que indica si hay gasolina
encendido = True  # Variable que indica si el motor está encendido
edad = 17         # Edad del usuario

# Validación de entrada para asegurarse de que los valores sean correctos
# En este caso, las variables están definidas como booleanos o números, por lo que no es necesario solicitarlas al usuario.
# Sin embargo, si se permitiera ingreso dinámico, habría que validar los tipos de datos.

# Ejemplo con el operador 'and' (Y)
# La condición se cumple solo si todas las subcondiciones son verdaderas
if gas and encendido and edad > 17:
    print("Todas las condiciones son verdaderas: Se puede conducir con seguridad.")
else:
    print("No se cumplen todas las condiciones necesarias para conducir con seguridad.")

# Ejemplo con el operador 'not' (NO) y 'or' (O)
# 'not gas' significa que queremos que no haya gasolina, y 'encendido or edad > 17' significa que cualquiera de las dos condiciones debe cumplirse
if not gas and (encendido or edad > 17):
    print("No hay gasolina, pero el motor está encendido o la edad es suficiente para otras acciones.")
else:
    print("La combinación de condiciones no es válida para este escenario.")

# Ejemplo con el operador 'or' (O)
# La condición se cumple si al menos una de las subcondiciones es verdadera
if gas or encendido:
    print("El vehículo tiene gasolina o el motor está encendido, puede funcionar.")
else:
    print("El vehículo no tiene gasolina ni el motor está encendido, no puede funcionar.")

# Explicación sobre corto-circuito en operadores lógicos
# En 'and', si la primera condición es falsa, las siguientes no se evalúan porque el resultado será siempre falso.
# En 'or', si la primera condición es verdadera, las siguientes no se evalúan porque el resultado será siempre verdadero.

# Operación de corto-circuito con 'and'
if gas and encendido:  # 'gas' es False, por lo que no se evalúa 'encendido'
    print("Este mensaje no se mostrará porque 'gas' es False.")
else:
    print("'gas' es False, por lo que no se evalúa el resto de la condición con 'and'.")

# Operación de corto-circuito con 'or'
if encendido or edad > 18:  # 'encendido' es True, por lo que no se evalúa 'edad > 18'
    print("'encendido' es True, por lo que no es necesario evaluar 'edad > 18'.")
else:
    print("Ni 'encendido' es True ni 'edad > 18', por lo que este mensaje se ejecutaría.")

# Resumen de conceptos:
print("\nNotas sobre los operadores lógicos:")
print("- 'and' devuelve True solo si todas las condiciones son verdaderas.")
print("- 'or' devuelve True si al menos una condición es verdadera.")
print("- 'not' invierte el valor booleano de una condición (True a False y viceversa).")
print("- Los operadores lógicos en Python tienen corto-circuito:")
print("  * En 'and', si una condición es False, las siguientes no se evalúan.")
print("  * En 'or', si una condición es True, las siguientes no se evalúan.")

