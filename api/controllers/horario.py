from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

cargador_controller = Blueprint('cargador_controller', __name__)

# Configuración de la conexión a MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
# Nombre de la base de datos de MongoDB
db = mongo_client['nombre_de_tu_base_de_datos']
cargador_collection = db['horario']  # Nombre de la colección en MongoDB


# Configuración de la conexión a MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['examen_3']  # Nombre de la base de datos de MongoDB
horario_collection = db['horario']  # Nombre de la colección en MongoDB

# Obtener todos los horarios


@horario_controller.route('/horario', methods=['GET'])
def get_all_horarios():
    try:
        horarios = list(horario_collection.find({}))
        return jsonify(horarios), 200
    except Exception as e:
        return str(e), 500

# Obtener información de un horario por ID


@horario_controller.route('/horario/<string:horario_id>', methods=['GET'])
def get_horario(horario_id):
    try:
        horario_data = horario_collection.find_one(
            {'_id': ObjectId(horario_id)})
        if horario_data:
            return jsonify(horario_data), 200
        else:
            return 'Horario no encontrado', 404
    except Exception as e:
        return str(e), 500

# Crear un nuevo horario


@horario_controller.route('/horario', methods=['POST'])
def create_horario():
    try:
        data = request.get_json()
        hora = data['hora']
        result = horario_collection.insert_one({'hora': hora})
        if result.inserted_id:
            return 'Horario creado correctamente', 201
        else:
            return 'Error al crear el horario', 500
    except Exception as e:
        return str(e), 500

# Actualizar un horario por ID


@horario_controller.route('/horario/<string:horario_id>', methods=['PUT'])
def update_horario(horario_id):
    try:
        data = request.get_json()
        hora = data['hora']
        result = horario_collection.update_one(
            {'_id': ObjectId(horario_id)},
            {'$set': {'hora': hora}}
        )
        if result.modified_count > 0:
            return 'Horario actualizado correctamente', 200
        else:
            return 'Horario no encontrado o no se pudo actualizar', 404
    except Exception as e:
        return str(e), 500

# Eliminar un horario por ID


@horario_controller.route('/horario/<string:horario_id>', methods=['DELETE'])
def delete_horario(horario_id):
    try:
        result = horario_collection.delete_one({'_id': ObjectId(horario_id)})
        if result.deleted_count > 0:
            return 'Horario eliminado correctamente', 200
        else:
            return 'Horario no encontrado o no se pudo eliminar', 404
    except Exception as e:
        return str(e), 500
