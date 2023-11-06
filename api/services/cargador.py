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
cargador_collection = db['cargador']

# Función para obtener todos los cargadores registrados


@app.route('/cargadores', methods=['GET'])
def obtener_cargadores():
    try:
        cargadores = list(cargador_collection.find())
        return jsonify(cargadores)
    except Exception as e:
        return jsonify({'error': 'Error al obtener la lista de cargadores'})

# Función para obtener un cargador por su Id


@app.route('/cargadores/<string:cargador_id>', methods=['GET'])
def obtener_cargador_por_id(cargador_id):
    try:
        cargador = cargador_collection.find_one({"_id": ObjectId(cargador_id)})
        if cargador:
            return jsonify(cargador)
        else:
            return jsonify({'error': 'Cargador no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': 'Error al obtener el cargador'})

# Función para crear un nuevo cargador


@app.route('/cargadores', methods=['POST'])
def crear_cargador():
    nuevo_cargador = request.get_json()
    placa = nuevo_cargador.get('placa')
    marca = nuevo_cargador.get('marca')
    # Agregar validaciones de campos necesarios y únicos aquí

    try:
        cargador = {
            "placa": placa,
            "marca": marca,
        }
        result = cargador_collection.insert_one(cargador)
        return jsonify({'mensaje': 'Cargador creado correctamente', 'id': str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({'error': 'Error al crear el cargador'})

# Función para actualizar un cargador existente


@app.route('/cargadores/<string:cargador_id>', methods=['PUT'])
def actualizar_cargador(cargador_id):
    datos_actualizados = request.get_json()
    placa = datos_actualizados.get('placa')
    marca = datos_actualizados.get('marca')
    # Agregar validaciones de campos necesarios y únicos aquí

    try:
        cargador_collection.update_one({"_id": ObjectId(cargador_id)}, {"$set": {
            "placa": placa,
            "marca": marca
        }})
        return jsonify({'mensaje': 'Cargador actualizado correctamente'})
    except Exception as e:
        return jsonify({'error': 'Error al actualizar el cargador'})

# Función para eliminar un cargador existente


@app.route('/cargadores/<string:cargador_id>', methods=['DELETE'])
def eliminar_cargador(cargador_id):
    try:
        cargador_collection.delete_one({"_id": ObjectId(cargador_id)})
        return jsonify({'mensaje': 'Cargador eliminado correctamente'})
    except Exception as e:
        return jsonify({'error': 'Error al eliminar el cargador'})


if __name__ == '__main__':
    app.run(debug=True)
