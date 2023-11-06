from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

programacion_cargador_controller = Blueprint(
    'programacion_cargador_controller', __name__)

# Configuración de la conexión a MongoDB
mongo_client = MongoClient('mongodb://localhost:27017')
# Nombre de la base de datos de MongoDB
db = mongo_client['nombre_de_tu_base_de_datos']
# Nombre de la colección en MongoDB
programacion_cargador_collection = db['programacion_cargador']

# Obtener información de todas las programaciones de cargador


@programacion_cargador_controller.route('/programacion_cargador', methods=['GET'])
def obtener_todas_las_programaciones_cargador():
    programaciones_cargador = list(programacion_cargador_collection.find({}))
    return jsonify(programaciones_cargador), 200

# Crear una nueva programación de cargador


@programacion_cargador_controller.route('/programacion_cargador', methods=['POST'])
def crear_programacion_cargador():
    data = request.json
    placa = data['placa']
    hora = data['hora']
    autobus_id = data['autobus_id']

    nueva_programacion_cargador = {
        'placa': placa,
        'hora': hora,
        'autobus_id': autobus_id
    }

    result = programacion_cargador_collection.insert_one(
        nueva_programacion_cargador)

    if result.inserted_id:
        return "Programación de cargador creada con éxito", 201
    else:
        return "Error al crear la programación de cargador", 500

# Actualizar la programación de cargador por ID


@programacion_cargador_controller.route('/programacion_cargador/<id>', methods=['PUT'])
def actualizar_programacion_cargador(id):
    data = request.json
    placa = data['placa']
    hora = data['hora']
    autobus_id = data['autobus_id']

    result = programacion_cargador_collection.update_one(
        {'_id': ObjectId(id)},
        {'$set': {'placa': placa, 'hora': hora, 'autobus_id': autobus_id}}
    )

    if result.modified_count > 0:
        return "Programación de cargador actualizada con éxito", 200
    else:
        return "Programación de cargador no encontrada o no se pudo actualizar", 404

# Elimina una programación de cargador por ID


@programacion_cargador_controller.route('/programacion_cargador/<id>', methods=['DELETE'])
def eliminar_programacion_cargador(id):
    result = programacion_cargador_collection.delete_one({'_id': ObjectId(id)})

    if result.deleted_count > 0:
        return "Programación de cargador eliminada con éxito", 200
    else:
        return "Programación de cargador no encontrada o no se pudo eliminar", 404
