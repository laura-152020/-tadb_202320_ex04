import pymongo
from datetime import datetime
from bson.objectid import ObjectId

# Configuración de la conexión a la base de datos MongoDB
MONGO_HOST = "localhost"  # Reemplaza con la dirección de tu servidor MongoDB
MONGO_PUERTO = 27017  # Reemplaza con el puerto de MongoDB
MONGO_BASE_DATOS = "nombre_de_tu_base_de_datos"

# Función para conectar a MongoDB


def conectar():
    """Conectar a la base de datos MongoDB"""
    try:
        cliente = pymongo.MongoClient(MONGO_HOST, MONGO_PUERTO)
        db = cliente[MONGO_BASE_DATOS]
        return cliente, db
    except pymongo.errors.ConnectionFailure as e:
        print(f"Error de conexión a MongoDB: {e}")
        return None, None

# Función para verificar si es horario pico


def es_horario_pico():
    ahora = datetime.now().time()
    hora_actual = ahora.hour

    # Define los límites del horario pico
    HORARIO_PICO_MANANA = (7, 10)
    HORARIO_PICO_TARDE = (16, 19)

    return (HORARIO_PICO_MANANA[0] <= hora_actual <= HORARIO_PICO_MANANA[1]) or \
           (HORARIO_PICO_TARDE[0] <= hora_actual <= HORARIO_PICO_TARDE[1])

# Función para obtener una programación de autobús por ID


def obtener_programacion_autobus_por_id(id_programacion):
    cliente, db = conectar()
    if db is not None:
        try:
            collection = db['programacion_autobuses']
            programacion = collection.find_one(
                {'_id': ObjectId(id_programacion)})
            return programacion
        except pymongo.errors.ConnectionFailure as e:
            print(
                f'Error al obtener programación de autobús por ID de MongoDB: {e}')
        finally:
            cliente.close()
    return None


# Función para crear una nueva programación de autobús
def crear_programacion_autobus(id_autobus, id_horario, fecha):
    if not es_horario_pico():
        cliente, db = conectar()
        if db is not None:  # Corregido aquí
            try:
                collection = db['programacion_autobuses']
                programacion = {
                    'id_autobus': id_autobus,
                    'id_horario': id_horario,
                    'fecha': fecha
                }
                result = collection.insert_one(programacion)
                return str(result.inserted_id)
            except pymongo.errors.ConnectionFailure as e:
                print(
                    f'Error al crear programación de autobús en MongoDB: {e}')
            finally:
                cliente.close()
        else:
            print("Error: No se pudo conectar a la base de datos MongoDB.")
    else:
        print("No se puede programar un autobús durante el horario pico.")
    return None


# Función para actualizar una programación de autobús por ID
def actualizar_programacion_autobus(id_programacion, nuevo_id_autobus, nuevo_id_horario, nueva_fecha):
    if not es_horario_pico():
        cliente, db = conectar()
        if db is not None:  # Corregido aquí
            try:
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
                print("Programación de autobús actualizada exitosamente.")
            except pymongo.errors.ConnectionFailure as e:
                print(
                    f'Error al actualizar programación de autobús en MongoDB: {e}')
            finally:
                cliente.close()
        else:
            print("Error: No se pudo conectar a la base de datos MongoDB.")
    else:
        print("No se puede actualizar la programación durante el horario pico.")


# Función para eliminar una programación de autobús por ID
def eliminar_programacion_autobus(id_programacion):
    if not es_horario_pico():
        cliente, db = conectar()
        if db is not None:  # Corregido aquí
            try:
                collection = db['programacion_autobuses']
                filtro = {'_id': ObjectId(id_programacion)}
                collection.delete_one(filtro)
                print("Programación de autobús eliminada exitosamente.")
            except pymongo.errors.ConnectionFailure as e:
                print(
                    f'Error al eliminar programación de autobús en MongoDB: {e}')
            finally:
                cliente.close()
        else:
            print("Error: No se pudo conectar a la base de datos MongoDB.")
    else:
        print("No se puede eliminar la programación durante el horario pico.")


# Ejemplo de uso para obtener una programación de autobús por ID
id_valido = ObjectId('5ec1c012a34d3d2e09df72f4')
programacion = obtener_programacion_autobus_por_id(id_valido)
if programacion:
    print(programacion)
else:
    print("No se encontró la programación de autobús.")

# Ejemplo de uso para crear una nueva programación de autobús
nuevo_id = crear_programacion_autobus("ID_AUTOBUS", "ID_HORARIO", "2023-11-04")
if nuevo_id:
    print("ID Insertado:", nuevo_id)

# Ejemplo de uso para actualizar una programación de autobús
actualizar_programacion_autobus(
    id_valido, "NUEVO_ID_AUTOBUS", "NUEVO_ID_HORARIO", "NUEVA_FECHA")

# Ejemplo de uso para eliminar una programación de autobús
eliminar_programacion_autobus(id_valido)
