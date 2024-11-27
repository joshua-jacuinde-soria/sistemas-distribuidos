from ORM.config import SessionClass
from ORM.modelos import Usuario, Compra, Foto
from sqlalchemy.orm import Session
from sqlalchemy import and_

# Esta funcion es llamda por el api.py para atender el Get '/usuarios/{id}'

def obtener_usuario(sesion:Session, id:int):
    # obtenemos el usuario con el id proporcionado
    return sesion.query(Usuario).filter(Usuario.id == id).first()

def obtener_compra_id(sesion:Session, id:int):
    # obtenemos la compra con el id proporcionado
    return sesion.query(Compra).filter(Compra.id == id).first()

def obtener_foto_id(sesion:Session, id:int):
    # obtenemos la foto con el id proporcionado
    return sesion.query(Foto).filter(Foto.id == id).first()

def obtener_todos_los_usuarios(sesion:Session):
    # obtenemos todos los usuarios
    return sesion.query(Usuario).all()

def obtener_todas_las_compras(sesion:Session):
    # obtenemos todas las compras
    return sesion.query(Compra).all()

def obtener_todas_las_fotos(sesion:Session):
    # obtenemos todas las fotos
    return sesion.query(Foto).all()

def compras_por_usuario(sesion:Session, id_usuario:int):
    # obtenemos todas las compras de un usuario
    return sesion.query(Compra).filter(Compra.id_usuario == id_usuario).all()

def compras_por_usuarios_mayores_a(sesion:Session, precio:int, id_usuario:int):
    # obtenemos todas las compras de un usuario mayores a un precio
    return sesion.query(Compra).filter(Compra.id_usuario == id_usuario, Compra.precio > precio).all()