from ORM.config import SessionClass
from ORM.modelos import Usuario, Compra, Foto
from sqlalchemy.orm import Session

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