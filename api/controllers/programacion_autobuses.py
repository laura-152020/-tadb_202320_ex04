from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

programacion_autobus_controller = Blueprint(
    'programacion_autobus_controller', __name__)

# Configuración de la conexión a MongoDB
mongo_client = MongoClient('mongodb://localhost:27017')
# Nombre de la base de datos de MongoDB
db = mongo_client['nombre_de_tu_base_de_datos']
# Nombre de la colección en MongoDB
programacion_autobus_collection = db['programacion_autobus']

# Obtener información de todas las programaciones de autobús


@programacion_autobus_controller.route('/programacion_autobus', methods=['GET'])
def get_all_programaciones_autobus():
    programaciones_autobus = list(programacion_autobus_collection.find({}))
    return jsonify(programaciones_autobus), 200

# Crear una nueva programación de autobús


@programacion_autobus_controller.route('/programacion_autobus', methods=['POST'])
def create_programacion_autobus():
    data = request.json
    autobus_id = data['autobus_id']
    horario_id = data['horario_id']

    nueva_programacion_autobus = {
        'autobus_id': autobus_id,
        'horario_id': horario_id
    }

    result = programacion_autobus_collection.insert_one(
        nueva_programacion_autobus)

    if result.inserted_id:
        return "Programación de autobús creada con éxito", 201
    else:
        return "Error al crear la programación de autobús", 500

# Actualizar una programación de autobús por ID


@programacion_autobus_controller.route('/programacion_autobus/<id>', methods=['PUT'])
def update_programacion_autobus(id):
    data = request.json
    autobus_id = data['autobus_id']
    horario_id = data['horario_id']

    result = programacion_autobus_collection.update_one(
        {'_id': ObjectId(id)},
        {'$set': {'autobus_id': autobus_id, 'horario_id': horario_id}}
    )

    if result.modified_count > 0:
        return "Programación de autobús actualizada con éxito", 200
    else:
        return "Programación de autobús no encontrada o no se pudo actualizar", 404

# Eliminar una programación de autobús por ID


@programacion_autobus_controller.route('/programacion_autobus/<id>', methods=['DELETE'])
def delete_programacion_autobus(id):
    result = programacion_autobus_collection.delete_one({'_id': ObjectId(id)})

    if result.deleted_count > 0:
        return "Programación de autobús eliminada con éxito", 200
    else:
        return "Programación de autobús no encontrada o no se pudo eliminar", 404
