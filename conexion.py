from pymongo import MongoClient

# Reemplaza 'mongodb://localhost:27017' con la URI de tu servidor MongoDB
mongo_uri = 'mongodb://localhost:27017'
client = MongoClient(mongo_uri)

# Selecciona la base de datos que deseas utilizar en MongoDB
# Reemplaza 'nombre_de_la_base_de_datos'
db = client['nombre_de_tu_base_de_datos']

# En MongoDB, no necesitas definir una sesión como en SQLAlchemy
# Puedes interactuar directamente con la base de datos MongoDB usando la variable 'db'
