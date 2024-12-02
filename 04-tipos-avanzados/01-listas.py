# lista de supermercado
# pan, huevos

numeros = [1, 2, 3]

letras = ["a", "b", "c"]

palabras = ["Jeanne", "Jorge"]

booleans = [True, False, True]

matriz = [[0, 1], [1, 0]]

ceros = [0] * 10

alfanumerico = numeros + letras

rango = list(range(10))

charts = list("hola mundo")

print(charts)

mascotas = ["Pelusa", "Coco", "Yiru"]
print(mascotas[0])
mascotas[0] = "Pantera Oscura"
print(mascotas[0])
print(mascotas[0:3])
# operador de "slicing" ([::]) con tres parámetros opcionales: [inicio:fin:paso]
print(mascotas[::-1])

numeros = list(range(21))
print(numeros[1::2])

numeros = list(range(1, 21))
print(numeros[::2])
