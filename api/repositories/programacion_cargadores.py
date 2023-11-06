from pymongo import MongoClient
from datetime import datetime

# Configura la conexión a MongoDB
mongo_client = MongoClient('mongodb://localhost:27017')
# Reemplaza 'nombre_de_tu_base_de_datos' con el nombre correcto
db = mongo_client['nombre_de_tu_base_de_datos']
# Nombre de la colección
programacion_cargador_collection = db['programacion_cargador']


class ProgramacionCargador:
    def __init__(self, placa, hora, autobus_id):
        self.placa = placa
        self.hora = hora
        self.autobus_id = autobus_id
        self._id = None

    def to_dict(self):
        data = {
            "placa": self.placa,
            "hora": self.hora,
            "autobus_id": self.autobus_id
        }
        if self._id:
            data["_id"] = self._id
        return data

    @classmethod
    def from_dict(cls, data):
        programacion_cargador = cls(
            data["placa"], data["hora"], data["autobus_id"])
        if "_id" in data:
            programacion_cargador._id = data["_id"]
        return programacion_cargador

    def save(self):
        data = self.to_dict()
        if self._id:
            programacion_cargador_collection.update_one(
                {"_id": self._id}, {"$set": data})
        else:
            result = programacion_cargador_collection.insert_one(data)
            self._id = result.inserted_id

    @classmethod
    def obtener_programacion_cargador(cls, placa, hora, autobus_id):
        programacion_cargador_data = programacion_cargador_collection.find_one(
            {"placa": placa, "hora": hora, "autobus_id": autobus_id})
        if programacion_cargador_data:
            return cls.from_dict(programacion_cargador_data)
        return None

    @classmethod
    def actualizar_programacion_cargador(cls, placa, hora, autobus_id, nueva_placa, nueva_hora, nuevo_autobus_id):
        programacion_cargador_data = programacion_cargador_collection.find_one(
            {"placa": placa, "hora": hora, "autobus_id": autobus_id})
        if programacion_cargador_data:
            programacion_cargador = cls.from_dict(programacion_cargador_data)
            programacion_cargador.placa = nueva_placa
            programacion_cargador.hora = nueva_hora
            programacion_cargador.autobus_id = nuevo_autobus_id
            programacion_cargador.save()
            return "Programación de cargador actualizada con éxito"
        return "Programación de cargador no encontrada"

    @classmethod
    def eliminar_programacion_cargador(cls, placa, hora, autobus_id):
        programacion_cargador_data = programacion_cargador_collection.find_one(
            {"placa": placa, "hora": hora, "autobus_id": autobus_id})
        if programacion_cargador_data:
            programacion_cargador = cls.from_dict(programacion_cargador_data)
            programacion_cargador_collection.delete_one(
                programacion_cargador_data)
            return "Programación de cargador eliminada con éxito"
        return "Programación de cargador no encontrada"
