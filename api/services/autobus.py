from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

# Configuración de la conexión a MongoDB
MONGO_HOST = "localhost"  # Reemplaza con la dirección de tu servidor MongoDB
MONGO_PUERTO = 27017  # Reemplaza con el puerto de MongoDB
MONGO_BASE_DATOS = "nombre_de_tu_base_de_datos"

# Inicializar la aplicación Flask
app = Flask(__name__)

# Configura la conexión a MongoDB
mongo_client = MongoClient(MONGO_HOST, MONGO_PUERTO)
db = mongo_client[MONGO_BASE_DATOS]
autobus_collection = db['autobus']

# Función para obtener todos los autobuses registrados


@app.route('/autobuses', methods=['GET'])
def obtener_autobuses():
    try:
        autobuses = list(autobus_collection.find())
        return jsonify(autobuses)
    except Exception as e:
        return jsonify({'error': 'Error al obtener la lista de autobuses'})

# Función para obtener un autobús por su Id


@app.route('/autobuses/<string:autobus_id>', methods=['GET'])
def obtener_autobus_por_id(autobus_id):
    try:
        autobus = autobus_collection.find_one({"_id": ObjectId(autobus_id)})
        if autobus:
            return jsonify(autobus)
        else:
            return jsonify({'error': 'Autobús no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': 'Error al obtener el autobús'})

# Función para crear un nuevo autobús


@app.route('/autobuses', methods=['POST'])
def crear_autobus():
    nuevo_autobus = request.get_json()
    placa = nuevo_autobus.get('placa')
    marca = nuevo_autobus.get('marca')
    # Agregar validaciones de campos necesarios y únicos aquí

    try:
        autobus = {
            "placa": placa,
            "marca": marca,
        }
        result = autobus_collection.insert_one(autobus)
        return jsonify({'mensaje': 'Autobús creado correctamente', 'id': str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({'error': 'Error al crear el autobús'})

# Función para actualizar un autobús existente


@app.route('/autobuses/<string:autobus_id>', methods=['PUT'])
def actualizar_autobus(autobus_id):
    datos_actualizados = request.get_json()
    placa = datos_actualizados.get('placa')
    marca = datos_actualizados.get('marca')
    # Agregar validaciones de campos necesarios y únicos aquí

    try:
        autobus_collection.update_one({"_id": ObjectId(autobus_id)}, {"$set": {
            "placa": placa,
            "marca": marca
        }})
        return jsonify({'mensaje': 'Autobús actualizado correctamente'})
    except Exception as e:
        return jsonify({'error': 'Error al actualizar el autobús'})

# Función para eliminar un autobús existente


@app.route('/autobuses/<string:autobus_id>', methods=['DELETE'])
def eliminar_autobus(autobus_id):
    try:
        autobus_collection.delete_one({"_id": ObjectId(autobus_id)})
        return jsonify({'mensaje': 'Autobús eliminado correctamente'})
    except Exception as e:
        return jsonify({'error': 'Error al eliminar el autobús'})

# Agregar aquí las rutas y funciones para registrar, actualizar y eliminar la utilización de cargadores y operaciones por hora del día.


if __name__ == '__main__':
    app.run(debug=True)
