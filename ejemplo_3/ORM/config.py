from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ORM import modelos
from os import getenv

#confirgurar la conexión a la base de datos
#servidorBD://usuario:password@host:puerto/nombreBD
## SQLALCHEMY_DATABASE_URL = "postgresql://Joshua_Group:12345@localhost:5432/Sistemas_Distribuidos"

#conectarse mediante esquema app                    esto es parte de la conexión por esquema
##engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"options": "-csearch_path=app"})


engine = create_engine(getenv("db_uri", "sqlite://base-ejemplo.db"))
modelos.BaseClass

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
