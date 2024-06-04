import csv
import pymongo
from pymongo import MongoClient

# Configurar la conexión a MongoDB
MONGO_HOST = "localhost"
MONGO_PUERTO="27017"
MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"

# Leer el archivo CSV y cargar los datos en MongoDB
with open('atp_tennis.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        collection.insert_one(row)

print("Datos insertados correctamente en la colección 'atp_tennis'.")

# Realizar una consulta en MongoDB
consulta_resultados = collection.find().limit(5)
print("Primeros 5 documentos en la colección 'atp_tennis':")
for documento in consulta_resultados:
    print(documento)

