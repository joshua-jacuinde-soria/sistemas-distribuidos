from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#confirgurar la conexión a la base de datos
#servidorBD://usuario:password@host:puerto/nombreBD
# SQLALCHEMY_DATABASE_URL = "Joshua_ESC://Joshua_Group:12345@localhost:5432/Sistemas_Distribuidos"
SQLALCHEMY_DATABASE_URL = "postgresql://Joshua_Group:12345@localhost:5432/Sistemas_Distribuidos"

#conectarse mediante esquema app                    esto es parte de la conexión por esquema
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"options": "-csearch_path=app"})

#obtenemos la clase que nos permite crear objetos de sesión
SessionClass = sessionmaker(engine)
#crea una funcion para obtener onjetos de la clase session
def generador_session():
    session = SessionClass()
    try:
        yield session   #devuelve la sesión
    finally:
        session.close()

#obtener la clase base para mapear las tablas
BaseClass = declarative_base()
