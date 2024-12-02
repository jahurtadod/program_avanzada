class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        # esto es un metodo
        print("Guau!")

    @classmethod
    def factory(cls):
        return cls("Codrilo", 3)


Perro.habla()
mi_perro = Perro("Coco", 2)
mi_perro2 = Perro("Yiru", 2)
