import pymongo
from bson import ObjectId

# Configuración de la conexión a la base de datos MongoDB
MONGO_HOST = "localhost"  # Reemplaza con la dirección del host de MongoDB
MONGO_PUERTO = 27017  # Reemplaza con el puerto de MongoDB como un número entero
MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PUERTO}/"

# Nombre de la base de datos y colección (ajusta estos valores según tus necesidades)
DB_NAME = "nombre_de_tu_base_de_datos"
COLLECTION_NAME = "horarios"

# Función para obtener una conexión a MongoDB


def conectar_mongodb():
    try:
        cliente = pymongo.MongoClient(MONGO_URI)
        return cliente
    except pymongo.errors.ConnectionFailure as e:
        print(f'Error de conexión a MongoDB: {e}')
        return None

# Función para obtener todos los horarios registrados


def obtener_horarios():
    cliente = conectar_mongodb()
    if cliente is not None:
        db = cliente[DB_NAME]
        collection = db[COLLECTION_NAME]
        horarios = list(collection.find({}))
        return horarios
    return []

# Función para obtener un horario por ID


def obtener_horario_por_id(id_horario):
    cliente = conectar_mongodb()
    if cliente is not None:
        db = cliente[DB_NAME]
        collection = db[COLLECTION_NAME]
        horario = collection.find_one({'_id': id_horario})
        return horario
    return None

# Función para crear un nuevo horario


def crear_horario(hora_inicio, hora_fin):
    cliente = conectar_mongodb()
    if cliente is not None:
        db = cliente[DB_NAME]
        collection = db[COLLECTION_NAME]
        horario = {"hora_inicio": hora_inicio, "hora_fin": hora_fin}
        result = collection.insert_one(horario)
        return str(result.inserted_id)
    return None

# Función para actualizar un horario existente


def actualizar_horario(id_horario, nueva_hora_inicio, nueva_hora_fin):
    cliente = conectar_mongodb()
    if cliente is not None:
        db = cliente[DB_NAME]
        collection = db[COLLECTION_NAME]
        collection.update_one({"_id": id_horario}, {
            "$set": {"hora_inicio": nueva_hora_inicio, "hora_fin": nueva_hora_fin}})
        print("Horario actualizado exitosamente")
        return False
# Función para eliminar un horario existente


def eliminar_horario(id_horario):
    cliente = conectar_mongodb()
    if cliente is not None:
        db = cliente[DB_NAME]
        collection = db[COLLECTION_NAME]
        collection.delete_one({"_id": id_horario})
        print("Horario eliminado exitosamente")
        return True

    return False

# Función para verificar si es horario pico

    print(horario)


# Reemplaza con un ID válido
id_horario_buscado = ObjectId("5ec1c012a34d3d2e09df72f4")
horario = obtener_horario_por_id(id_horario_buscado)
if horario:
    print(horario)
else:
    print(f"No se encontró un horario con ID {id_horario_buscado}")

# Ejemplo de uso para crear un nuevo horario
hora_inicio_nueva = "08:00"
hora_fin_nueva = "10:00"
id_insertado = crear_horario(hora_inicio_nueva, hora_fin_nueva)
if id_insertado:
    print(f"Se ha creado un nuevo horario con ID: {id_insertado}")

# Ejemplo de uso para actualizar un horario existente
id_horario_a_actualizar = ObjectId(
    "5ec1c012a34d3d2e09df72f4")  # Reemplaza con un ID válido
nueva_hora_inicio = "09:00"
nueva_hora_fin = "11:00"
actualizar_horario(id_horario_a_actualizar, nueva_hora_inicio, nueva_hora_fin)

# Ejemplo de uso para eliminar un horario existente
id_horario_a_eliminar = ObjectId(
    "5ec1c012a34d3d2e09df72f4")  # Reemplaza con un ID válido
eliminar_horario(id_horario_a_eliminar)
