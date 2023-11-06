from pymongo import MongoClient

# Configura la conexión a MongoDB
mongo_client = MongoClient('mongodb://localhost:27017')
db = mongo_client['nombre_de_tu_base_de_datos']
cargador_collection = db['horario']


class Horario:
    def __init__(self, hora):
        self.hora = hora

    def to_dict(self):
        return {
            "hora": self.hora
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["hora"])

    def save(self):
        data = self.to_dict()
        db.horario.insert_one(data)


class ProgramacionAutobuses:
    def __init__(self, autobus_id, horario_id):
        self.autobus_id = autobus_id
        self.horario_id = horario_id

    def to_dict(self):
        return {
            "autobus_id": self.autobus_id,
            "horario_id": self.horario_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["autobus_id"], data["horario_id"])

    def save(self):
        data = self.to_dict()
        db.programacion_autobuses.insert_one(data)


class Cargador:
    def __init__(self, placa):
        self.placa = placa

    def to_dict(self):
        return {
            "placa": self.placa
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["placa"])

    def save(self):
        data = self.to_dict()
        db.cargador.insert_one(data)

# Define las funciones adicionales según tus necesidades
