from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

cargador_controller = Blueprint('cargador_controller', __name__)

# Configuración de la conexión a MongoDB
# Reemplaza con la URL de tu base de datos MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['examen_3']  # Nombre de la base de datos
cargador_collection = db['cargador']  # Nombre de la colección

# Obtener todos los cargadores


@cargador_controller.route('/cargador', methods=['GET'])
def get_all_cargadores():
    cargadores = list(cargador_collection.find({}))
    return jsonify(cargadores), 200

# Obtener información de un cargador por ID


@cargador_controller.route('/cargador/<cargador_id>', methods=['GET'])
def get_cargador(cargador_id):
    cargador = cargador_collection.find_one({'_id': ObjectId(cargador_id)})
    if cargador:
        return jsonify(cargador), 200
    else:
        return 'Cargador no encontrado', 404

# Crear un nuevo cargador


@cargador_controller.route('/cargador', methods=['POST'])
def create_cargador():
    data = request.get_json()
    placa = data['placa']

    nuevo_cargador = {
        'placa': placa
    }

    result = cargador_collection.insert_one(nuevo_cargador)

    if result.inserted_id:
        return 'Cargador creado correctamente', 201
    else:
        return 'Error al crear el cargador', 500

# Actualizar un cargador por ID


@cargador_controller.route('/cargador/<cargador_id>', methods=['PUT'])
def update_cargador(cargador_id):
    data = request.get_json()
    placa = data['placa']

    result = cargador_collection.update_one(
        {'_id': ObjectId(cargador_id)}, {'$set': {'placa': placa}})

    if result.modified_count > 0:
        return 'Cargador actualizado correctamente', 200
    else:
        return 'Cargador no encontrado o no se pudo actualizar', 404

# Eliminar un cargador por ID


@cargador_controller.route('/cargador/<cargador_id>', methods=['DELETE'])
def delete_cargador(cargador_id):
    result = cargador_collection.delete_one({'_id': ObjectId(cargador_id)})
    if result.deleted_count > 0:
        return 'Cargador eliminado correctamente', 200
    else:
        return 'Cargador no encontrado o no se pudo eliminar', 404
