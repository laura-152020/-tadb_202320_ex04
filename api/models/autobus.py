from bson.objectid import ObjectId


class Autobus:
    def __init__(self, placa, _id=None):
        self._id = _id
        self.placa = placa

    def to_dict(self):
        return {
            "_id": str(self._id),
            "placa": self.placa
        }

    @classmethod
    def from_dict(cls, data):
        autobus = cls(data.get("placa"), data.get("_id"))
        return autobus

    def to_mongo_dict(self):
        return {
            "placa": self.placa
        }

    @classmethod
    def from_mongo_dict(cls, data):
        autobus = cls(data.get("placa"), data.get("_id"))
        return autobus

    def get_id(self):
        return str(self._id)
