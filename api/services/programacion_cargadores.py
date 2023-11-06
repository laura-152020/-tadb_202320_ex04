from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

# Configuración de la conexión a MongoDB
MONGO_HOST = "localhost"  # Reemplaza con la dirección de tu servidor MongoDB
MONGO_PUERTO = 27017  # Reemplaza con el puerto de MongoDB
MONGO_BASE_DATOS = "nombre_de_tu_base_de_datos"

# Inicializar la aplicación Flask
app = Flask(__name__)

# Configura la conexión a MongoDB
mongo_client = MongoClient(MONGO_HOST, MONGO_PUERTO)
db = mongo_client[MONGO_BASE_DATOS]
programacion_autobuses_collection = db['programacion_cargadores']


# Configuración de la conexión a MongoDB
MONGO_HOST = "localhost"  # Reemplaza con la dirección de tu servidor MongoDB
MONGO_PUERTO = 27017  # Reemplaza con el puerto de MongoDB
MONGO_BASE_DATOS = "nombre_de_tu_base_de_datos"

# Inicializar la aplicación Flask
app = Flask(__name__)

# Configura la conexión a MongoDB
mongo_client = MongoClient(MONGO_HOST, MONGO_PUERTO)
db = mongo_client[MONGO_BASE_DATOS]
programacion_autobuses_collection = db['programacion_autobuses']

# Función para obtener todas las programaciones de autobuses


@app.route('/programacion_autobuses', methods=['GET'])
def obtener_programacion_autobuses():
    try:
        programaciones = list(programacion_autobuses_collection.find())
        return jsonify(programaciones)
    except Exception as e:
        return jsonify({'error': 'Error al obtener la lista de programaciones de autobuses'})

# Función para obtener una programación de autobuses por su ID


@app.route('/programacion_autobuses/<string:programacion_id>', methods=['GET'])
def obtener_programacion_autobuses_por_id(programacion_id):
    try:
        programacion = programacion_autobuses_collection.find_one(
            {"_id": ObjectId(programacion_id)})
        if programacion:
            return jsonify(programacion)
        else:
            return jsonify({'error': 'Programación de autobuses no encontrada'}), 404
    except Exception as e:
        return jsonify({'error': 'Error al obtener la programación de autobuses'})

# Función para crear una nueva programación de autobuses


@app.route('/programacion_autobuses', methods=['POST'])
def crear_programacion_autobuses():
    nueva_programacion = request.get_json()
    autobus_id = nueva_programacion.get('autobus_id')
    horario = nueva_programacion.get('horario')
    # Agregar validaciones de campos necesarios aquí

    try:
        programacion_autobuses_collection.insert_one({
            "autobus_id": autobus_id,
            "horario": horario
        })
        return jsonify({'mensaje': 'Programación de autobuses creada correctamente'}), 201
    except Exception as e:
        return jsonify({'error': 'Error al crear la programación de autobuses'})

# Función para actualizar una programación de autobuses existente


@app.route('/programacion_autobuses/<string:programacion_id>', methods=['PUT'])
def actualizar_programacion_autobuses(programacion_id):
    datos_actualizados = request.get_json()
    autobus_id = datos_actualizados.get('autobus_id')
    horario = datos_actualizados.get('horario')
    # Agregar validaciones de campos necesarios aquí

    try:
        programacion_autobuses_collection.update_one({"_id": ObjectId(programacion_id)}, {"$set": {
            "autobus_id": autobus_id,
            "horario": horario
        }})
        return jsonify({'mensaje': 'Programación de autobuses actualizada correctamente'})
    except Exception as e:
        return jsonify({'error': 'Error al actualizar la programación de autobuses'})

# Función para eliminar una programación de autobuses existente


@app.route('/programacion_autobuses/<string:programacion_id>', methods=['DELETE'])
def eliminar_programacion_autobuses(programacion_id):
    try:
        programacion_autobuses_collection.delete_one(
            {"_id": ObjectId(programacion_id)})
        return jsonify({'mensaje': 'Programación de autobuses eliminada correctamente'})
    except Exception as e:
        return jsonify({'error': 'Error al eliminar la programación de autobuses'})


if __name__ == '__main__':
    app.run(debug=True)
