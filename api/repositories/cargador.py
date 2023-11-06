from pymongo import MongoClient

# Configura la conexión a MongoDB
mongo_client = MongoClient('mongodb://localhost:27017')
db = mongo_client['nombre_de_tu_base_de_datos']
cargador_collection = db['cargador']


class Cargador:
    def __init__(self, placa):
        self.placa = placa
        self._id = None  # No establezcas _id aquí, se generará automáticamente en MongoDB

    def to_dict(self):
        data = {
            "placa": self.placa
        }
        if self._id:
            data["_id"] = self._id
        return data

    @classmethod
    def from_dict(cls, data):
        cargador = cls(data.get("placa"))
        if "_id" in data:
            cargador._id = data["_id"]
        return cargador

    def save(self):
        data = self.to_dict()
        if self._id:
            cargador_collection.update_one({"_id": self._id}, {"$set": data})
        else:
            result = cargador_collection.insert_one(data)
            self._id = result.inserted_id

    @classmethod
    def obtener_cargadores(cls):
        cargadores = cargador_collection.find()
        return [cls.from_dict(c) for c in cargadores]

    @classmethod
    def leer_cargador_por_id(cls, id_cargador):
        cargador_data = cargador_collection.find_one({"_id": id_cargador})
        if cargador_data:
            return cls.from_dict(cargador_data)
        return None

    @classmethod
    def actualizar_cargador(cls, id_cargador, nueva_placa):
        cargador_data = cargador_collection.find_one({"_id": id_cargador})
        if cargador_data:
            cargador = cls.from_dict(cargador_data)
            cargador.placa = nueva_placa
            cargador.save()
            return "Cargador actualizado con éxito"
        return "Cargador no encontrado"

    @classmethod
    def eliminar_cargador(cls, id_cargador):
        result = cargador_collection.delete_one({"_id": id_cargador})
        if result.deleted_count > 0:
            return "Cargador eliminado con éxito"
        return "Cargador no encontrado"
