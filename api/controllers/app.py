from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Configura la conexión a la base de datos MongoDB
# URL de conexión a tu instancia de MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017'
mongo = MongoClient(app.config['MONGO_URI'])
db = mongo.mydatabase  # Reemplaza 'mydatabase' con el nombre de tu base de datos


@app.route('/get_data', methods=['GET'])
def get_data():
    # Reemplaza 'my_collection' con el nombre de tu colección en MongoDB
    collection = db.my_collection
    data = collection.find()  # Consulta para recuperar datos
    data_list = [item for item in data]
    return jsonify(data_list)


if __name__ == '__main__':
    app.run(debug=True)
