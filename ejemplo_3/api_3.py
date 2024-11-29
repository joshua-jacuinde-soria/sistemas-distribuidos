from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import os
import uuid
from ORM import repo
from sqlalchemy.orm import Session
from ORM.config import generador_session

# creación del servidor
app = FastAPI()

#definición de la base del usuario
class UsuarioBase(BaseModel):
    nombre:Optional[str]=None
    edad:int
    domicilio:str    
    
usuarios = [{
    "id": 0,
    "nombre": "Homero Simpson",
    "edad": 40,
    "domicilio": "Av. Simpre Viva"
}, {
    "id": 1,
    "nombre": "Marge Simpson",
    "edad": 38,
    "domicilio": "Av. Simpre Viva"
}, {
    "id": 2,
    "nombre": "Lisa Simpson",
    "edad": 8,
    "domicilio": "Av. Simpre Viva"
}, {
    "id": 3,
    "nombre": "Bart Simpson",
    "edad": 10,
    "domicilio": "Av. Simpre Viva"
}]


# decorator
@app.get("/")
def hola_mundo():
    print("invocando a ruta /")
    respuesta = {
        "mensaje": "hola mundo!"
    }

    return respuesta
        
@app.get("/usuarios")
def lista_usuarios(edad_ini:int=0, edad_fin:int =0, sesion: Session = Depends(generador_session)):
    if edad_ini == 0 and edad_fin == 0:
        return repo.obtener_todos_los_usuarios(sesion)
    else:
        return repo.obtener_usuarios_rango_edad(sesion, edad_ini, edad_fin)

@app.get("/usuarios/{id}")
def usuario_por_id(id: int, sesion: Session = Depends(generador_session)):
    print("buscando usuario con id:", id)
    # simulamos la consulta
    return repo.obtener_usuario(sesion, id)

@app.post("/usuarios")
def guardar_usuario(usuario:UsuarioBase, parametro1:str):
    print("usuario a guardar:", usuario, ", parametro1:", parametro1)
    #simulamos guardado en la base.
    
    usr_nuevo = {}
    usr_nuevo["id"] = len(usuarios)
    usr_nuevo["nombre"] = usuario.nombre
    usr_nuevo["edad"] = usuario.edad
    usr_nuevo["domicilio"] = usuario.domicilio

    usuarios.append(usuario)

    return usr_nuevo

@app.put("/usuario/{id}")
def actualizar_usuario(id:int, usuario:UsuarioBase):
    #simulamos consulta
    usr_act = usuarios[id]
    #simulamos la actualización
    usr_act["nombre"] = usuario.nombre
    usr_act["edad"] = usuario.edad
    usr_act["domicilio"] = usuario.domicilio    

    return usr_act
    
@app.delete("/usuario/{id}")
def borrar_usuario(id:int, sesion: Session = Depends(generador_session)):
    print("borrando usuario con id:", id)
    #simulamos la eliminación
    repo.borrar_usuario(sesion, id)
    return {"mensaje":"usuario eliminado"}
    

@app.post("/fotos")
async def guardar_foto(titulo:str=Form(None), descripcion:str=Form(...), foto:UploadFile=File(...)):
    print("titulo:", titulo)
    print("descripcion:", descripcion)

    home_usuario=os.path.expanduser("~")
    nombre_archivo=uuid.uuid4().hex  #generamos nombre único en formato hexadecimal
    extension = os.path.splitext(foto.filename)[1]
    ruta_imagen=f'{home_usuario}/fotos-ejemplo/{nombre_archivo}{extension}'
    print("guardando imagen en ruta:", ruta_imagen)

    with open(ruta_imagen,"wb") as imagen:
        contenido = await foto.read() #read funciona de manera asyncrona
        imagen.write(contenido)

    return {"titulo":titulo, "descripcion":descripcion, "foto":foto.filename}

@app.get("/fotos/{id}")
def obtener_foto_id(id: int, sesion: Session = Depends(generador_session)):
    print("buscando foto con id:", id)
    return repo.obtener_foto_id(sesion, id)

@app.get("/fotos")
def obtener_todas_las_fotos(sesion: Session = Depends(generador_session)):
    print("obteniendo todas las fotos")
    return repo.obtener_todas_las_fotos(sesion)

@app.get("/compras/{id}")
def obtener_compra_id(id: int, sesion: Session = Depends(generador_session)):
    print("buscando compra con id:", id)
    # simulamos la consulta
    return repo.obtener_compra_id(sesion, id)

@app.get("/compras")
def compras_usuario_por_id(id:int = 0, precio:float = 0, session: Session = Depends(generador_session)):
    if precio <= 0:
        return repo.obtener_todas_las_compras(session)
    else:
        return repo.compras_por_usuarios_precio(session, precio, id)

