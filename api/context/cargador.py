import pymongo
from bson.objectid import ObjectId

# Configuración de la conexión a la base de datos MongoDB
MONGO_HOST = "localhost"  # Corregir la dirección del host
MONGO_PUERTO = 27017  # Corregir el puerto como un número entero
MONGO_TIEMPO_FUERA = 1000

MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PUERTO}/"

try:
    cliente = pymongo.MongoClient(
        MONGO_URI, serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
    cliente.server_info()
    print("Conexión a MongoDB exitosa")
    cliente.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido: " + str(errorTiempo))
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a MongoDB: " + str(errorConexion))


# Función para conectar a la base de datos MongoDB
def conectar():
    """Conectar a la base de datos MongoDB"""
    conexion = None
    try:
        conexion = pymongo.MongoClient(MONGO_HOST, MONGO_PUERTO)
        db = conexion['nombre_de_tu_base_de_datos']
        print('Conexión a MongoDB exitosa')
    except pymongo.errors.ConnectionFailure as e:
        print(f'Error de conexión a MongoDB: {e}')
    return db

# Función para obtener todos los cargadores registrados


def obtener_cargadores():
    cargadores = []
    db = conectar()
    if db is not None:
        try:
            collection = db['cargador']
            cargadores = list(collection.find({}))
        except Exception as e:
            print(f"Ocurrió un error: {e}")
    return cargadores

# Función para obtener un cargador por ID


def obtener_cargador_por_id(id_cargador):
    cargador = None
    db = conectar()
    if db is not None:
        try:
            collection = db['cargador']
            cargador = collection.find_one({'_id': id_cargador})
        except Exception as e:
            print(f"Ocurrió un error: {e}")
    return cargador

# Función para crear un nuevo cargador


def crear_cargador(placa):
    id_insertado = None
    db = conectar()
    if db is not None:
        try:
            collection = db['cargador']
            cargador = {"placa": placa}
            result = collection.insert_one(cargador)
            id_insertado = result.inserted_id
        except Exception as e:
            print(f"Ocurrió un error: {e}")
    return id_insertado

# Función para actualizar un cargador existente


def actualizar_cargador(id_cargador, nueva_placa):
    db = conectar()
    if db is not None:
        try:
            collection = db['cargador']
            collection.update_one({"_id": id_cargador}, {
                                  "$set": {"placa": nueva_placa}})
        except Exception as e:
            print(f"Ocurrió un error: {e}")

# Función para eliminar un cargador existente


def eliminar_cargador(id_cargador):
    db = conectar()
    if db is not None:
        try:
            collection = db['cargador']
            collection.delete_one({"_id": id_cargador})
        except Exception as e:
            print(f"Ocurrió un error: {e}")


# Ejemplo de uso para obtener todos los cargadores registrados
cargadores = obtener_cargadores()
for cargador in cargadores:
    print(cargador)

# Ejemplo de uso para obtener un cargador por ID
id_cargador_buscado = ObjectId("6546e8bef9b621a84cc37396")
cargador = obtener_cargador_por_id(id_cargador_buscado)
if cargador:
    print(cargador)
else:
    print(f"No se encontró un cargador con ID {id_cargador_buscado}")

# Ejemplo de uso para crear un nuevo cargador
placa_nueva = "XYZ123"
id_insertado = crear_cargador(placa_nueva)
if id_insertado:
    print(f"Se ha creado un nuevo cargador con ID: {id_insertado}")

# Ejemplo de uso para actualizar un cargador existente
id_cargador_a_actualizar = ObjectId("6546e8bef9b621a84cc37396")
id_cargador_a_actualizar = ObjectId("6546e8bef9b621a84cc37396")
nueva_placa = "ABC789"
actualizar_cargador(id_cargador_a_actualizar, nueva_placa)
print("Cargador actualizado exitosamente")

# Ejemplo de uso para eliminar un cargador existente
id_cargador_a_eliminar = ObjectId("6546e8bef9b621a84cc37396")
eliminar_cargador(id_cargador_a_eliminar)
print("Cargador eliminado exitosamente")
