from pymongo import MongoClient

# Configura la conexión a MongoDB
mongo_client = MongoClient('mongodb://localhost:27017')
# Reemplaza 'nombre_de_tu_base_de_datos' con el nombre correcto
db = mongo_client['nombre_de_tu_base_de_datos']
# Nombre de la colección
programacion_autobus_collection = db['programacion_autobuses']


class ProgramacionAutobus:
    def __init__(self, autobus_id, horario_id):
        self.autobus_id = autobus_id
        self.horario_id = horario_id
        self._id = None

    def to_dict(self):
        data = {
            "autobus_id": self.autobus_id,
            "horario_id": self.horario_id
        }
        if self._id:
            data["_id"] = self._id
        return data

    @classmethod
    def from_dict(cls, data):
        programacion_autobus = cls(data["autobus_id"], data["horario_id"])
        if "_id" in data:
            programacion_autobus._id = data["_id"]
        return programacion_autobus

    def save(self):
        data = self.to_dict()
        if self._id:
            programacion_autobus_collection.update_one(
                {"_id": self._id}, {"$set": data})
        else:
            result = programacion_autobus_collection.insert_one(data)
            self._id = result.inserted_id

    @classmethod
    def obtener_programacion_autobus_por_id(cls, programacion_id):
        programacion_autobus_data = programacion_autobus_collection.find_one(
            {"_id": programacion_id})
        if programacion_autobus_data:
            return cls.from_dict(programacion_autobus_data)
        return None

    @classmethod
    def actualizar_programacion_autobus(cls, programacion_id, nuevo_autobus_id, nuevo_horario_id):
        programacion_autobus_data = programacion_autobus_collection.find_one(
            {"_id": programacion_id})
        if programacion_autobus_data:
            programacion_autobus = cls.from_dict(programacion_autobus_data)
            programacion_autobus.autobus_id = nuevo_autobus_id
            programacion_autobus.horario_id = nuevo_horario_id
            programacion_autobus.save()
            return "Programación de autobús actualizada con éxito"
        return "Programación de autobús no encontrada"

    @classmethod
    def eliminar_programacion_autobus(cls, programacion_id):
        programacion_autobus_data = programacion_autobus_collection.find_one(
            {"_id": programacion_id})
        if programacion_autobus_data:
            programacion_autobus = cls.from_dict(programacion_autobus_data)
            programacion_autobus_collection.delete_one(
                {"_id": programacion_id})
            return "Programación de autobús eliminada con éxito"
        return "Programación de autobús no encontrada"
