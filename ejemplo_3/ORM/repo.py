from ORM.config import SessionClass
from ORM.modelos import Usuario, Compra, Foto
from sqlalchemy.orm import Session
from sqlalchemy import and_

# Esta funcion es llamda por el api.py para atender el Get '/usuarios/{id}'

def obtener_usuario(sesion:Session, id:int):
    # obtenemos el usuario con el id proporcionado
    return sesion.query(Usuario).filter(Usuario.id == id).first()

def obtener_todos_los_usuarios(sesion:Session):
    # obtenemos todos los usuarios
    return sesion.query(Usuario).all()

def obtener_usuarios_rango_edad(sesion:Session, edad_ini:int, edad_fin:int):
    # obtenemos todos los usuarios en un rango de edad
    return sesion.query(Usuario).filter(and_(Usuario.edad >= edad_ini, Usuario.edad <= edad_fin)).all()

def borrar_usuario(sesion:Session, id:int):
    # borramos el usuario con el id proporcionado
    usuario = obtener_usuario(sesion, id)
    if usuario is not None:
        borrar_compra_id_usuario(sesion, id)
        borrar_foto_id_usuario(sesion, id)
        sesion.delete(usuario)
        sesion.commit()
    return True

def obtener_todas_las_fotos(sesion:Session):
    # obtenemos todas las fotos
    return sesion.query(Foto).all()

def obtener_foto_id(sesion:Session, id:int):
    # obtenemos la foto con el id proporcionado
    return sesion.query(Foto).filter(Foto.id == id).first()

def obtener_fotos_id_usuario(sesion:Session, id_usuario:int):
    # obtenemos todas las fotos de un usuario
    return sesion.query(Foto).filter(Foto.id_usuario == id_usuario).all()

def borrar_foto_id_usuario(sesion:Session, id_usuario:int):
    # borramos todas las fotos de un usuario
    fotos = obtener_fotos_id_usuario(sesion, id_usuario)
    if fotos is not None:
        for foto in fotos:
            sesion.delete(foto)
        sesion.commit()
    return True        

def obtener_compra_id(sesion:Session, id:int):
    # obtenemos la compra con el id proporcionado
    return sesion.query(Compra).filter(Compra.id == id).first()

def obtener_todas_las_compras(sesion:Session):
    # obtenemos todas las compras
    return sesion.query(Compra).all()

def compras_por_usuario(sesion:Session, id_usuario:int):
    # obtenemos todas las compras de un usuario
    return sesion.query(Compra).filter(Compra.id_usuario == id_usuario).all()

# Se tiene que hacer con parametros de consulta
def compras_por_usuarios_precio(sesion:Session, precio:float, id_usuario:int):
    # obtenemos todas las compras de un usuario mayores a un precio
    return sesion.query(Compra).filter(and_(Compra.id_usuario == id_usuario, Compra.precio >= precio)).all()

def obtener_compras_id_usuario(sesion:Session, id_usuario:int):
    # obtenemos todas las compras de un usuario
    return sesion.query(Compra).filter(Compra.id_usuario == id_usuario).all()

def borrar_compra_id_usuario(sesion:Session, id_usuario:int):
    # borramos todas las compras de un usuario
    compras = obtener_compras_id_usuario(sesion, id_usuario)
    if compras is not None:
        for compra in compras:
            sesion.delete(compra)
        sesion.commit()
    return True