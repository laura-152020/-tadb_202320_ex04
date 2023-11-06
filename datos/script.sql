db.createCollection("autobuses", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["placa", "marca"],
            properties: {
                placa: {
                    bsonType: "string",
                    description: "Placa del autobús"
                },
                marca: {
                    bsonType: "string",
                    description: "Marca del autobús"
                }
            }
        }
    }
})

db.createCollection("cargadores", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["nombre", "ubicacion", "estado"],
            properties: {
                nombre: {
                    bsonType: "string",
                    description: "Nombre o identificación del cargador"
                },
                ubicacion: {
                    bsonType: "string",
                    description: "Ubicación del cargador"
                },
                estado: {
                    bsonType: "string",
                    description: "Estado del cargador"
                }
            }
        }
    }
})

db.createCollection("horarios", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["hora"],
            properties: {
                hora: {
                    bsonType: "string",
                    description: "Hora del horario"
                }
               
               
            }
        }
    }
})

db.createCollection("programacion_autobuses", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["autobus_id", "horario"],
            properties: {
                autobus_id: {
                    bsonType: "objectId",
                    description: "ID del autobús"
                },
                horario: {
                    bsonType: "string",
                    description: "Hora del horario"
                }
             
            }
        }
    }
})

db.createCollection("programacion_cargadores", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["cargador_id", "horario"],
            properties: {
                cargador_id: {
                    bsonType: "objectId",
                    description: "ID del cargador"
                },
                horario: {
                    bsonType: "string",
                    description: "Hora del horario"
                }
              
            }
        }
    }
})
