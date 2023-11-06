# CREAR API CON FLASK
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
# Reemplaza 'elementos' con el nombre de tu colección en MongoDB
coleccion = db['elementos']

# Ruta para obtener todos los elementos


@app.route('/elementos', methods=['GET'])
def obtener_elementos():
    elementos = list(coleccion.find())
    return jsonify(elementos)

# Ruta para obtener un elemento por su ID


@app.route('/elementos/<string:elemento_id>', methods=['GET'])
def obtener_elemento_por_id(elemento_id):
    elemento = coleccion.find_one({"_id": ObjectId(elemento_id)})
    if elemento:
        return jsonify(elemento)
    else:
        return jsonify({'error': 'Elemento no encontrado'}), 404

# Ruta para crear un nuevo elemento


@app.route('/elementos', methods=['POST'])
def crear_elemento():
    nuevo_elemento = request.get_json()
    resultado = coleccion.insert_one(nuevo_elemento)
    return jsonify({'mensaje': 'Elemento creado correctamente', 'id': str(resultado.inserted_id)}), 201

# Ruta para actualizar un elemento existente


@app.route('/elementos/<string:elemento_id>', methods=['PUT'])
def actualizar_elemento(elemento_id):
    datos_actualizados = request.get_json()
    resultado = coleccion.update_one({"_id": ObjectId(elemento_id)}, {
                                     "$set": datos_actualizados})
    if resultado.modified_count > 0:
        return jsonify({'mensaje': 'Elemento actualizado correctamente'})
    else:
        return jsonify({'error': 'Elemento no encontrado'}), 404

# Ruta para eliminar un elemento existente


@app.route('/elementos/<string:elemento_id>', methods=['DELETE'])
def eliminar_elemento(elemento_id):
    resultado = coleccion.delete_one({"_id": ObjectId(elemento_id)})
    if resultado.deleted_count > 0:
        return jsonify({'mensaje': 'Elemento eliminado correctamente'})
    else:
        return jsonify({'error': 'Elemento no encontrado'}), 404


if __name__ == "__main__":
    app.run(debug=True)
