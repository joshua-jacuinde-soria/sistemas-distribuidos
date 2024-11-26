# los modelos representan el mapeo de las tablas de la base de datos
# la clase base de las clases modelos es BaseClass

from ORM.config import BaseClass

# Importamos de sqlalchemy los tipos de datos que  usan las tablas
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
# importamos la clase datetime para obtener la fecha y hora actual
from datetime import datetime

class Usuario(BaseClass):
    # Nombre de la tabla
    __tablename__ = 'usuarios'
    # Columnas de la tabla
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    edad = Column(Integer)
    domicilio = Column(String(100))
    email = Column('email',String(100))
    password = Column(String(50))
    fecha_registro = Column(DateTime(timezone=True), default=datetime.now)
    
class Compra(BaseClass):
    # Nombre de la tabla
    __tablename__ = 'compras'
    # Columnas de la tabla
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey(Usuario.id))
    producto = Column(String(100))
    precio = Column(Float)
    
class Foto(BaseClass):
    # Nombre de la tabla
    __tablename__ = 'fotos'
    # Columnas de la tabla
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey(Usuario.id))
    titulo = Column(String(100))
    descripcion = Column(String(200))
    ruta = Column(String(100))


