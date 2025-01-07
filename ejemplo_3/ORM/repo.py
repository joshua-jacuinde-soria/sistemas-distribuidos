from ORM.config import SessionClass
from ORM.modelos import Usuario, Compra, Foto
from sqlalchemy.orm import Session
from sqlalchemy import and_
import ORM.esquemas as esquemas

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

def actualizar_usuario(sesion:Session, id:int, usuario:esquemas.UsuarioBase):
    # actualizamos el usuario con el id proporcionado
    usuario_db = obtener_usuario(sesion, id)
    if usuario_db is not None:
        usuario_db.nombre = usuario.nombre
        usuario_db.edad = usuario.edad
        usuario_db.domicilio = usuario.domicilio
        usuario_db.email = usuario.email
        usuario_db.password = usuario.password
        sesion.commit()
        sesion.refresh(usuario_db)
        print("usuario actualizado:", usuario)
        return usuario
    else:
        return {"mensaje":"usuario no encontrado"}
    
def insertar_usuario(sesion:Session, usuario:esquemas.UsuarioBase):
    # insertamos un usuario
    usuario_db = Usuario(nombre=usuario.nombre, edad=usuario.edad, domicilio=usuario.domicilio, email=usuario.email, password=usuario.password)
    sesion.add(usuario_db)
    sesion.commit()
    sesion.refresh(usuario_db)
    print("usuario insertado:", usuario)
    return usuario_db

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

def actualizar_foto(sesion:Session, id:int, foto:esquemas.FotoBase):
    # actualizamos la foto con el id proporcionado
    foto_db = obtener_foto_id(sesion, id)
    if foto_db is not None:
        foto_db.titulo = foto.titulo
        foto_db.descripcion = foto.descripcion
        foto_db.ruta = foto.ruta
        sesion.commit()
        sesion.refresh(foto_db)
        print("foto actualizada:", foto)
        return foto
    else:
        return {"mensaje":"foto no encontrada"}   
    
def insertar_foto(sesion:Session, foto:esquemas.FotoBase, id_usuario:int):
    # insertamos una foto
    if obtener_usuario(sesion, id_usuario) is None:
        return {"mensaje":"usuario no encontrado"}
    else:
        foto_db = Foto(titulo=foto.titulo, descripcion=foto.descripcion, ruta=foto.ruta, id_usuario=id_usuario)
        sesion.add(foto_db)
        sesion.commit()
        sesion.refresh(foto_db)
        print("foto insertada:", foto)
        return foto_db 

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

def actualizar_compra(sesion:Session, id:int, compra:esquemas.CompraBase):
    # actualizamos la compra con el id proporcionado
    compra_db = obtener_compra_id(sesion, id)
    if compra_db is not None:
        compra_db.producto = compra.producto
        compra_db.precio = compra.precio
        sesion.commit()
        sesion.refresh(compra_db)
        print("compra actualizada:", compra)
        return compra
    else:
        return {"mensaje":"compra no encontrada"}
    
def insertar_compra(sesion:Session, compra:esquemas.CompraBase, id_usuario:int):
    # insertamos una compra
    if obtener_usuario(sesion, id_usuario) is None:
        return {"mensaje":"usuario no encontrado"}
    else:
        compra_db = Compra(producto=compra.producto, precio=compra.precio, id_usuario=id_usuario)
        sesion.add(compra_db)
        sesion.commit()
        sesion.refresh(compra_db)
        print("compra insertada:", compra)
        return compra_db