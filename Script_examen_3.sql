/*    Script Modelo de datos 
Curso de topicos Avanzados de base de datos
Laura Itzel Caycedo Jota 

todo el procesamiento almacenado esta en python, 
tambien esta el stack completo
 */
 
CREATE TABLE horario (
    id_horario INT PRIMARY KEY,
    hora TIME
);

CREATE TABLE programacion_autobuses (
    programacion_id INT PRIMARY KEY,
    autobus_id INT,
    horario TIME,
    FOREIGN KEY (autobus_id) REFERENCES autobus(autobus_id),
    FOREIGN KEY (horario) REFERENCES horario(id_horario)
);

CREATE TABLE autobus (
    autobus_id INT PRIMARY KEY,
    placa VARCHAR(255) UNIQUE NOT NULL
);

CREATE INDEX idx_autobus_placa ON autobus(placa);

CREATE TABLE cargador (
    id_cargador INT PRIMARY KEY,
    placa VARCHAR(255) UNIQUE NOT NULL
);

CREATE INDEX idx_cargador_placa ON cargador(placa);

CREATE TABLE programacion_cargadores (
    programacion_cargador INT PRIMARY KEY,
    placa VARCHAR(255) UNIQUE NOT NULL,
    hora TIME,
    autobus_id INT,
    FOREIGN KEY (autobus_id) REFERENCES autobus(autobus_id)
);

CREATE INDEX idx_programacion_cargadores_placa ON programacion_cargadores(placa);