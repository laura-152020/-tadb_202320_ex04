# modedls/programacion_autobuses.pyclass ProgramacionAutobuses:
from bson.objectid import ObjectId


class ProgramacionAutobuses:
    def __init__(self, autobus_id, horario_id):
        self._id = None  # El _id se generará automáticamente en MongoDB
        self.autobus_id = autobus_id
        self.horario_id = horario_id

    def to_dict(self):
        return {
            "_id": str(self._id),  # Convertimos el ObjectId a una cadena
            "autobus_id": self.autobus_id,
            "horario_id": self.horario_id
        }

    @classmethod
    def from_dict(cls, data):
        programacion = cls(data.get("autobus_id"), data.get("horario_id"))
        if "_id" in data:
            # Convertimos la cadena ObjectId a ObjectId
            programacion._id = ObjectId(data["_id"])
        return programacion
