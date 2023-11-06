# models/cargador.py
from bson.objectid import ObjectId


class Cargador:
    def __init__(self, nombre, disponibilidad):
        self._id = None  # El _id se generará automáticamente en MongoDB
        self.nombre = nombre
        self.disponibilidad = disponibilidad

    def to_dict(self):
        return {
            "_id": str(self._id),  # Convertimos el ObjectId a una cadena
            "nombre": self.nombre,
            "disponibilidad": self.disponibilidad
        }

    @classmethod
    def from_dict(cls, data):
        cargador = cls(data.get("nombre"), data.get("disponibilidad"))
        if "_id" in data:
            # Convertimos la cadena ObjectId a ObjectId
            cargador._id = ObjectId(data["_id"])
        return cargador
