from pymongo import MongoClient
import pymongo
from datetime import datetime
from bson.objectid import ObjectId


# Configuración de la conexión a la base de datos MongoDB
MONGO_HOST = "localhost"  # Reemplaza con la dirección de tu servidor MongoDB
MONGO_PUERTO = 27017  # Reemplaza con el puerto de MongoDB
MONGO_BASE_DATOS = "nombre_de_tu_base_de_datos"


# Configurar la conexión a MongoDB
# Reemplaza con la URL de conexión de tu MongoDB
client = MongoClient("mongodb://localhost:27017/")
# Reemplaza "nombre_de_tu_base_de_datos" con el nombre de tu base de datos
db = client["nombre_de_tu_base_de_datos"]

# Operaciones para la colección de autobuses
autobuses = db["autobuses"]

# Crear un nuevo autobús
autobus = {
    "placa": "AB123CD"
}
autobus_id = autobuses.insert_one(autobus).inserted_id

# Leer un autobús por ID
leer_autobus = autobuses.find_one({"_id": autobus_id})
print("Autobús leído:", leer_autobus)

# Actualizar un autobús
autobuses.update_one({"_id": autobus_id}, {"$set": {"placa": "XY789ZW"}})
leer_autobus_actualizado = autobuses.find_one({"_id": autobus_id})
print("Autobús actualizado:", leer_autobus_actualizado)

# Eliminar un autobús
autobuses.delete_one({"_id": autobus_id})
print("Autobús eliminado")

# Cierra la conexión a MongoDB
client.close()
