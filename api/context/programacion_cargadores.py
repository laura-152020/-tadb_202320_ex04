import pymongo
from bson.objectid import ObjectId

# Configuración de la conexión a la base de datos MongoDB
MONGO_HOST = "localhost"  # Reemplaza con la dirección del host de MongoDB
MONGO_PUERTO = 27017  # Reemplaza con el puerto de MongoDB como un número entero
MONGO_TIEMPO_FUERA = 1000  # Define el tiempo de espera en milisegundos

MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PUERTO}/"

# Inicializa el cliente de MongoDB
cliente = pymongo.MongoClient(MONGO_HOST, MONGO_PUERTO)
# Reemplaza con el nombre de tu base de datos
db = cliente['nombre_de_tu_base_de_datos']

try:
    cliente = pymongo.MongoClient(
        MONGO_URI, serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
    cliente.server_info()
    print("Conexión a MongoDB exitosa")
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido: " + str(errorTiempo))
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a MongoDB: " + str(errorConexion))


def conectar():
    """Conectar a la base de datos MongoDB"""
    cliente = None
    try:
        cliente = pymongo.MongoClient(MONGO_HOST, MONGO_PUERTO)
        print('Conectado a la base de datos MongoDB')
    except pymongo.errors.ConnectionFailure as e:
        print(f'Error de conexión a MongoDB: {e}')
    return cliente


# Función para obtener todas las programaciones de cargadores
def obtener_programacion_cargadores():
    programaciones = list(db['programacion_cargadores'].find())
    return programaciones

# Función para obtener una programación de cargador por ID


def obtener_programacion_cargador_por_id(id_programacion):
    programacion = db['programacion_cargadores'].find_one(
        {'_id': ObjectId(id_programacion)})
    return programacion

# Función para crear una nueva programación de cargador


def crear_programacion_cargador(id_cargador, id_horario, fecha):
    programacion = {
        'id_cargador': id_cargador,
        'id_horario': id_horario,
        'fecha': fecha
    }
    resultado = db['programacion_cargadores'].insert_one(programacion)
    return str(resultado.inserted_id)

# Función para actualizar una programación de cargador existente


def actualizar_programacion_cargador(id_programacion, nuevo_id_cargador, nuevo_id_horario, nueva_fecha):
    filtro = {'_id': ObjectId(id_programacion)}
    actualizacion = {
        '$set': {
            'id_cargador': nuevo_id_cargador,
            'id_horario': nuevo_id_horario,
            'fecha': nueva_fecha
        }
    }
    db['programacion_cargadores'].update_one(filtro, actualizacion)

# Función para eliminar una programación de cargador existente


def eliminar_programacion_cargador(id_programacion):
    filtro = {'_id': ObjectId(id_programacion)}
    db['programacion_cargadores'].delete_one(filtro)


# Ejemplos de uso:
# Obtener todas las programaciones de cargadores
programaciones = obtener_programacion_cargadores()
print(programaciones)

# Crear una nueva programación de cargador
nuevo_id = crear_programacion_cargador(
    "ID_CARGADOR", "ID_HORARIO", "2023-11-04")
print("ID Insertado:", nuevo_id)

# Obtener una programación de cargador por ID
id_valido = ObjectId('5ec1c012a34d3d2e09df72f4')
programacion = obtener_programacion_cargador_por_id(id_valido)
print(programacion)

# Actualizar una programación de cargador
actualizar_programacion_cargador(
    ObjectId('5ec1c012a34d3d2e09df72f4'), "NUEVO_ID_CARGADOR", "NUEVO_ID_HORARIO", "NUEVA_FECHA")

# Eliminar una programación de cargador por ID
eliminar_programacion_cargador(ObjectId('5ec1c012a34d3d2e09df72f4'))
