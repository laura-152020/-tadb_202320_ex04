from pymongo import MongoClient

mongo_client = MongoClient('mongodb://localhost:27017')
db = mongo_client['nombre_de_tu_base_de_datos']
autobus_collection = db['autobus']


class Autobus:
    def __init__(self, placa):
        self.placa = placa
        self._id = None  # No establezcas _id aquí, se generará automáticamente

    def to_dict(self):
        data = {
            "placa": self.placa
        }
        if self._id:
            data["_id"] = self._id
        return data

    @classmethod
    def from_dict(cls, data):
        autobus = cls(data.get("placa"))
        if "_id" in data:
            autobus._id = data["_id"]
        return autobus

    def save(self):
        data = self.to_dict()
        if self._id:
            autobus_collection.update_one({"_id": self._id}, {"$set": data})
        else:
            result = autobus_collection.insert_one(data)
            self._id = result.inserted_id

    # ...
