import pymongo
from bson.objectid import ObjectId

# Configuración de la conexión a la base de datos MongoDB
MONGO_HOST = "localhost"  # Reemplaza con la dirección del host de MongoDB
MONGO_PUERTO = 27017  # Reemplaza con el puerto de MongoDB como un número entero
MONGO_TIEMPO_FUERA = 1000  # Define el tiempo de espera en milisegundos

MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PUERTO}/"

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

# Función para obtener todas las programaciones de autobuses


def obtener_programacion_autobuses():
    programaciones = []
    try:
        cliente = conectar()
        db = cliente['nombre_de_tu_base_de_datos']
        collection = db['programacion_autobuses']
        programaciones = list(collection.find({}))
    except pymongo.errors.ConnectionFailure as e:
        print(f'Error de conexión a MongoDB: {e}')
    finally:
        cliente.close()
    return programaciones

# Función para obtener una programación de autobús por ID


def obtener_programacion_autobus_por_id(id_programacion):
    programacion = None
    try:
        cliente = conectar()
        db = cliente['nombre_de_tu_base_de_datos']
        collection = db['programacion_autobuses']
        programacion = collection.find_one({'_id': ObjectId(id_programacion)})
    except pymongo.errors.ConnectionFailure as e:
        print(f'Error de conexión a MongoDB: {e}')
    finally:
        cliente.close()
    return programacion

# Función para crear una nueva programación de autobús


def crear_programacion_autobus(id_autobus, id_horario, fecha):
    id_insertado = None
    cliente = conectar()
    if cliente is not None:
        try:
            db = cliente['nombre_de_tu_base_de_datos']
            collection = db['programacion_autobuses']
            programacion = {
                'id_autobus': id_autobus,
                'id_horario': id_horario,
                'fecha': fecha
            }
            result = collection.insert_one(programacion)
            id_insertado = str(result.inserted_id)
        except pymongo.errors.ConnectionFailure as e:
            print(f'Error de conexión a MongoDB: {e}')
        finally:
            cliente.close()
    return id_insertado

# Función para actualizar una programación de autobús existente


def actualizar_programacion_autobus(id_programacion, nuevo_id_autobus, nuevo_id_horario, nueva_fecha):
    try:
        cliente = conectar()
        db = cliente['nombre_de_tu_base_de_datos']
        collection = db['programacion_autobuses']
        filtro = {'_id': ObjectId(id_programacion)}
        actualizacion = {
            '$set': {
                'id_autobus': nuevo_id_autobus,
                'id_horario': nuevo_id_horario,
                'fecha': nueva_fecha
            }
        }
        collection.update_one(filtro, actualizacion)
    except pymongo.errors.ConnectionFailure as e:
        print(f'Error de conexión a MongoDB: {e}')

# Función para eliminar una programación de autobús existente


def eliminar_programacion_autobus(id_programacion):
    try:
        cliente = conectar()
        db = cliente['nombre_de_tu_base_de_datos']
        collection = db['programacion_autobuses']
        filtro = {'_id': ObjectId(id_programacion)}
        collection.delete_one(filtro)
    except pymongo.errors.ConnectionFailure as e:
        print(f'Error de conexión a MongoDB: {e}')


# Ejemplos de uso:
# Obtener una programación de autobús por ID (reemplaza con un ID válido)
# Define el ID válido antes de usarlo
id_valido = ObjectId('5ec1c012a34d3d2e09df72f4')

# Luego puedes utilizar id_valido en tu función obtener_programacion_autobus_por_id
programacion = obtener_programacion_autobus_por_id(id_valido)
print(programacion)

# Crear una nueva programación de autobús
nuevo_id = crear_programacion_autobus("ID_AUTOBUS", "ID_HORARIO", "2023-11-04")
print("ID Insertado:", nuevo_id)

# Actualizar una programación de autobús (reemplaza con valores válidos)
# Reemplaza 'ID_PROGRAMACION' con un ObjectId válido o una cadena hexadecimal válida
actualizar_programacion_autobus(
    ObjectId('5ec1c012a34d3d2e09df72f4'), "NUEVO_ID_AUTOBUS", "NUEVO_ID_HORARIO", "NUEVA_FECHA")


# Eliminar una programación de autobús por ID (reemplaza con un ID válido)
eliminar_programacion_autobus(ObjectId('5ec1c012a34d3d2e09df72f4'))
