# similares a como nos entregan las bases de datos

punto = {"x": 25, "y": 50}

print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
# print(punto, punto["w"])

if "w" in punto:
    print("encontre w", punto["w"])

print(punto.get("x"))
print(punto.get("w", 0))

# del punto["x"]
# del (punto["y"])

# print(punto)

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "Jeanne"},
    {"id": 2, "nombre": "Gintoki"},
    {"id": 3, "nombre": "Tangiro"}
]
