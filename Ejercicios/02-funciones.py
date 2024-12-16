def es_palindromo(texto):
    # Convertimos todo el texto a minúsculas y eliminamos espacios
    texto_sin_espacios = texto.lower().replace(" ", "")
    
    # Invertimos el texto
    texto_invertido = texto_sin_espacios[::-1]

    # Verificamos si el texto es igual a su reverso
    if texto_invertido == texto_sin_espacios:
        return "es un palíndromo"
    else:
        return "no es un palíndromo"

# Pruebas
print("Abba:", es_palindromo("Abba"))
print("Reconocer:", es_palindromo("reconocer"))
print("Hola mundo:", es_palindromo("Hola mundo"))
