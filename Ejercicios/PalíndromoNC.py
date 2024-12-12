import unicodedata

def is_palindrome(string):
    """
    Función para verificar si una palabra o frase es un palíndromo.
    Se ignoran mayúsculas, espacios, caracteres especiales y acentos.
    """
    # Normalizar texto para eliminar acentos y caracteres especiales (NFKD)
    normalized_string = ''.join(
        char for char in unicodedata.normalize('NFKD', string) if char.isalnum()
    )
    # Convertir a minúsculas para ignorar diferencias de mayúsculas y minúsculas
    cleaned_string = normalized_string.lower()
    # Comparar el string con su reverso
    return cleaned_string == cleaned_string[::-1]

# Pruebas automáticas y ejemplo de uso
if __name__ == "__main__":
    print("Verificador de palíndromos")
    print("Ejemplos automáticos:")
    examples = [
        "Anita lava la tina",        # Palíndromo
        "Amo la pacífica paloma",   # Palíndromo
        "El cielo es azul",         # No es palíndromo
        "Dábale arroz a la zorra el abad", # Palíndromo
        "A mamá Roma le aviva el amor a mamá", # Palíndromo
        "Hola mundo"                # No es palíndromo
    ]
    
    for example in examples:
        result = "es un palíndromo" if is_palindrome(example) else "no es un palíndromo"
        print(f"'{example}' {result}.")
    
    # Entrada manual
    print("\nPrueba con tu propia frase o palabra:")
    test_string = input("Ingresa una palabra o frase: ")
    if is_palindrome(test_string):
        print(f"'{test_string}' es un palíndromo.")
    else:
        print(f"'{test_string}' no es un palíndromo.")
