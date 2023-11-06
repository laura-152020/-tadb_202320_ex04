from flask import Blueprint, request, jsonify
from pymongo import MongoClient
import requests

autobus_controller = Blueprint('autobus_controller', __name__)

# Configuración de la conexión a MongoDB
# Reemplaza con la URL de tu base de datos MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['nombre_de_tu_base_de_datos']  # Nombre de la base de datos
autobus_collection = db['autobus']  # Nombre de la colección

# Obtener todos los autobuses


@autobus_controller.route('/autobus', methods=['GET'])
def get_all_autobuses():
    autobuses = list(autobus_collection.find({}))
    return jsonify(autobuses), 200

# Obtener información de un autobus por ID


@autobus_controller.route('/autobus/<int:autobus_id>', methods=['GET'])
def get_autobus(autobus_id):
    autobus_data = autobus_collection.find_one({'autobus_id': autobus_id})
    if autobus_data:
        return jsonify(autobus_data), 200
    else:
        return 'Autobus no encontrado', 404

# Crear un nuevo autobus


@autobus_controller.route('/autobus', methods=['POST'])
def create_autobus():
    data = request.get_json()
    placa = data['placa']

    new_autobus = {'placa': placa}
    result = autobus_collection.insert_one(new_autobus)

    if result.inserted_id:
        return 'Autobus creado correctamente', 201
    else:
        return 'Error al crear el autobus', 500

# Actualizar un autobus por ID


@autobus_controller.route('/autobus/<int:autobus_id>', methods=['PUT'])
def update_autobus(autobus_id):
    data = request.get_json()
    placa = data['placa']

    result = autobus_collection.update_one(
        {'autobus_id': autobus_id},
        {'$set': {'placa': placa}}
    )

    if result.modified_count > 0:
        return 'Autobus actualizado correctamente', 200
    else:
        return 'Autobus no encontrado o no se pudo actualizar', 404

# Eliminar un autobus por ID


@autobus_controller.route('/autobus/<int:autobus_id>', methods=['DELETE'])
def delete_autobus(autobus_id):
    result = autobus_collection.delete_one({'autobus_id': autobus_id})
    if result.deleted_count > 0:
        return 'Autobus eliminado correctamente', 200
    else:
        return 'Autobus no encontrado o no se pudo eliminar', 404
