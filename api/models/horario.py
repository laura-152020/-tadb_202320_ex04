# models/horario.py
from bson.objectid import ObjectId


class Horario:
    def __init__(self, hora):
        self._id = None  # El _id se generará automáticamente en MongoDB
        self.hora = hora

    def to_dict(self):
        return {
            "_id": str(self._id),  # Convertimos el ObjectId a una cadena
            "hora": self.hora
        }

    @classmethod
    def from_dict(cls, data):
        horario = cls(data.get("hora"))
        if "_id" in data:
            # Convertimos la cadena ObjectId a ObjectId
            horario._id = ObjectId(data["_id"])
        return horario
