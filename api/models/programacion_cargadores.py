# models/programacion_cargadores.py
from bson.objectid import ObjectId


class ProgramacionCargadores:
    def __init__(self, cargador_id, horario_id):
        self._id = None  # El _id se generará automáticamente en MongoDB
        self.cargador_id = cargador_id
        self.horario_id = horario_id

    def to_dict(self):
        return {
            "_id": str(self._id),  # Convertimos el ObjectId a una cadena
            "cargador_id": self.cargador_id,
            "horario_id": self.horario_id
        }

    @classmethod
    def from_dict(cls, data):
        programacion = cls(data.get("cargador_id"), data.get("horario_id"))
        if "_id" in data:
            # Convertimos la cadena ObjectId a ObjectId
            programacion._id = ObjectId(data["_id"])
        return programacion
