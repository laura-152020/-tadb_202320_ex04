import pymongo
from bson import ObjectId

# Configuración de la conexión a la base de datos MongoDB
MONGO_HOST = "localhost"  # Corregir la dirección del host
MONGO_PUERTO = 27017  # Corregir el puerto como un número entero

# Establece la conexión a MongoDB
cliente = pymongo.MongoClient(MONGO_HOST, MONGO_PUERTO)
db = cliente['nombre_de_tu_base_de_datos']

# Modelo Autobus en MongoDB


class Autobus:
    def __init__(self, placa):
        self.placa = placa
        self.programaciones = []

    def save(self):
        collection = db['autobus']
        result = collection.insert_one(self.__dict__)
        return result.inserted_id

# Modelo Cargador en MongoDB


class Cargador:
    def __init__(self, placa):
        self.placa = placa
        self.programaciones = []

    def save(self):
        collection = db['cargador']
        result = collection.insert_one(self.__dict__)
        return result.inserted_id

# Modelo Horario en MongoDB


class Horario:
    def __init__(self, hora):
        self.hora = hora

    def save(self):
        collection = db['horario']
        result = collection.insert_one(self.__dict__)
        return result.inserted_id

# Modelo ProgramacionAutobuses en MongoDB


class ProgramacionAutobuses:
    def __init__(self, autobus_id, horario_id):
        self.autobus_id = autobus_id
        self.horario_id = horario_id

    def save(self):
        collection = db['programacion_autobuses']
        result = collection.insert_one(self.__dict__)
        return result.inserted_id

# Modelo ProgramacionCargadores en MongoDB


class ProgramacionCargadores:
    def __init__(self, placa, horario_id):
        self.placa = placa
        self.horario_id = horario_id

    def save(self):
        collection = db['programacion_cargadores']
        result = collection.insert_one(self.__dict__)
        return result.inserted_id


# Ejemplo de uso:
autobus = Autobus("ABC123")
autobus_id = autobus.save()
