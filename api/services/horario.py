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
horario_collection = db['horario']
programacion_cargadores_collection = db['programacion_cargadores']
programacion_autobuses_collection = db['programacion_autobuses']

# Ruta para obtener todos los horarios registrados


@app.route('/horarios', methods=['GET'])
def obtener_horarios():
    try:
        horarios = list(horario_collection.find())
        return jsonify(horarios)
    except Exception as e:
        return jsonify({'error': 'Error al obtener la lista de horarios'})

# Ruta para obtener el informe de hora por Id


@app.route('/horarios/<string:horario_id>', methods=['GET'])
def obtener_informe_de_hora_por_id(horario_id):
    try:
        hora = horario_collection.find_one({"_id": ObjectId(horario_id)})

        if not hora:
            return jsonify({'error': 'Hora no encontrada'}), 404

        utilizacion_cargadores = programacion_cargadores_collection.count_documents(
            {"hora": hora['hora']})
        cargadores_disponibles = programacion_cargadores_collection.count_documents(
            {})  # Suponiendo que todos los cargadores están disponibles
        porcentaje_utilizacion_cargadores = (
            utilizacion_cargadores / cargadores_disponibles) * 100

        operacion_buses = programacion_autobuses_collection.count_documents(
            {"horario": hora['hora']})
        buses_disponibles = programacion_autobuses_collection.count_documents(
            {})  # Suponiendo que todos los autobuses están disponibles
        porcentaje_operacion_buses = (
            operacion_buses / buses_disponibles) * 100

        informe = {
            'hora': hora,
            'porcentaje_utilizacion_cargadores': porcentaje_utilizacion_cargadores,
            'porcentaje_operacion_buses': porcentaje_operacion_buses
        }

        return jsonify(informe)
    except Exception as e:
        return jsonify({'error': 'Error al obtener el informe de la hora'})

# Ruta para obtener el informe de utilización de cargadores por hora


@app.route('/informe_cargadores', methods=['GET'])
def obtener_informe_de_utilizacion_de_cargadores_por_hora():
    try:
        pipeline = [
            {
                '$group': {
                    '_id': '$hora',
                    'utilizacion_cargadores': {'$sum': 1}
                }
            }
        ]

        informe_cargadores = list(
            programacion_cargadores_collection.aggregate(pipeline))
        cargadores_disponibles = programacion_cargadores_collection.count_documents(
            {})  # Suponiendo que todos los cargadores están disponibles

        for hora_info in informe_cargadores:
            hora_info['porcentaje_utilizacion'] = (
                hora_info['utilizacion_cargadores'] / cargadores_disponibles) * 100

        return jsonify(informe_cargadores)
    except Exception as e:
        return jsonify({'error': 'Error al obtener el informe de utilización de cargadores por hora'})

# Ruta para obtener el informe de utilización de buses por hora


@app.route('/informe_buses', methods=['GET'])
def obtener_informe_de_utilizacion_de_buses_por_hora():
    try:
        pipeline = [
            {
                '$group': {
                    '_id': '$horario',
                    'operacion_buses': {'$sum': 1}
                }
            }
        ]

        informe_buses = list(
            programacion_autobuses_collection.aggregate(pipeline))
        buses_disponibles = programacion_autobuses_collection.count_documents(
            {})  # Suponiendo que todos los autobuses están disponibles

        for hora_info in informe_buses:
            hora_info['porcentaje_operacion'] = (
                hora_info['operacion_buses'] / buses_disponibles) * 100

        return jsonify(informe_buses)
    except Exception as e:
        return jsonify({'error': 'Error al obtener el informe de utilización de buses por hora'})


if __name__ == '__main__':
    app.run(debug=True)
