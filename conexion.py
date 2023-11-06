from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Reemplaza 'DATABASE_URI' con la URL de conexión a tu base de datos
engine = create_engine('mysql://root:@Laura1502@@127.0.0.1/examen_3')

# Crea una sesión
Session = sessionmaker(bind=engine)
session = Session()
