from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.db1
coleccion = db.usuarios

lista = [
    {"nombre": "José", "apellido": "Medina", "nacionalidad": "ecuatoriana",
     "numero_publicaciones": 90},
    {"nombre": "María", "apellido": "Velez", "nacionalidad": "peruana",
     "numero_publicaciones": 80},
    {"nombre": "Jorge", "sexo": "Masculino"}
]

coleccion.find_one()
