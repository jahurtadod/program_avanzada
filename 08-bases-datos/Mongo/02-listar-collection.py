from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

# db = client.ejemploMongo001
db = client.db1

colecciones = db.list_collection_names()

print(colecciones)
