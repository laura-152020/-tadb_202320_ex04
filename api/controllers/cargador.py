from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

cargador_controller = Blueprint('cargador_controller', __name__)

# Configuración de la conexión a MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
# Nombre de la base de datos de MongoDB
db = mongo_client['nombre_de_tu_base_de_datos']
cargador_collection = db['cargador']  # Nombre de la colección en MongoDB

# Obtener todos los cargadores


@cargador_controller.route('/cargador', methods=['GET'])
def get_all_cargadores():
    try:
        cargadores = list(cargador_collection.find({}))
        return jsonify(cargadores), 200
    except Exception as e:
        return str(e), 500

# Obtener información de un cargador por ID


@cargador_controller.route('/cargador/<string:cargador_id>', methods=['GET'])
def get_cargador(cargador_id):
    try:
        cargador_data = cargador_collection.find_one(
            {'_id': ObjectId(cargador_id)})
        if cargador_data:
            return jsonify(cargador_data), 200
        else:
            return 'Cargador no encontrado', 404
    except Exception as e:
        return str(e), 500

# Crear un nuevo cargador


@cargador_controller.route('/cargador', methods=['POST'])
def create_cargador():
    try:
        data = request.get_json()
        placa = data['placa']
        result = cargador_collection.insert_one({'placa': placa})
        if result.inserted_id:
            return 'Cargador creado correctamente', 201
        else:
            return 'Error al crear el cargador', 500
    except Exception as e:
        return str(e), 500

# Actualizar un cargador por ID


@cargador_controller.route('/cargador/<string:cargador_id>', methods=['PUT'])
def update_cargador(cargador_id):
    try:
        data = request.get_json()
        placa = data['placa']
        result = cargador_collection.update_one(
            {'_id': ObjectId(cargador_id)},
            {'$set': {'placa': placa}}
        )
        if result.modified_count > 0:
            return 'Cargador actualizado correctamente', 200
        else:
            return 'Cargador no encontrado o no se pudo actualizar', 404
    except Exception as e:
        return str(e), 500

# Eliminar un cargador por ID


@cargador_controller.route('/cargador/<string:cargador_id>', methods=['DELETE'])
def delete_cargador(cargador_id):
    try:
        result = cargador_collection.delete_one({'_id': ObjectId(cargador_id)})
        if result.deleted_count > 0:
            return 'Cargador eliminado correctamente', 200
        else:
            return 'Cargador no encontrado o no se pudo eliminar', 404
    except Exception as e:
        return str(e), 500
