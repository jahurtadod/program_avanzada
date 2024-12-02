mensaje = "Hola mundo"

print(type(mensaje))

# Clase: es el plano de construcción
# Objeto: una instancia de una clase


class Perro:
    # creamos un constructor
    # self es un valor cambiante para referirse a una insstancia
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        # esto es un metodo
        print(f"{self.nombre} Guau!")


mi_perro = Perro("Coco", 2)
print(mi_perro.nombre)
# print(type(mi_perro))

mi_perro.habla()
# print(isinstance(mi_perro, Perro))
