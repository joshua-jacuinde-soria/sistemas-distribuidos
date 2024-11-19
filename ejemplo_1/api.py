from fastapi import FastAPI
from bd_biblioteca import libros, usuarios
from uvicorn import run
from pydantic import BaseModel
from asyncpg import connect
from typing import Optional


app = FastAPI()

#conexion a la base de datos de postgresql
DB_NAME = "sistemas_distribuidos"
DB_USER = "postgres"
DB_PASS = "JoshuaSoria1"
DB_HOST = "localhost"
DB_PORT = "5432"

async def connect_db():
    return await connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )

#Metodo: GET
#URL; '/'
@app.get('/')
def bienvenida():
    print("Atendiendo GET / ")
    respuesta = {"mensaje": "Bienvenido"}
    return respuesta

#Metodo Get
#URL '/libros'
#devuelva la lista de libros
@app.get('/libros')
async def lista_libros(pagina:int, lote:int, orden:Optional[str]=None):
    print("Atendiendo GET '/libros'")
    conn = await connect_db()
    try:
        query = "SELECT * FROM libros;"
        rows = await conn.fetch(query)
        items = [dict(row) for row in rows]
        return items
    finally:
        await conn.close()


#Metodo GET
#URL '/libros/{id}'
#devuelve un json
#parametro de ruta id
@app.get('/libros/{id}')
async def informacion_libro(id:int):
    print("Atendiendo GET /libros/",id)
    conn = await connect_db()
    try:
        query = f"SELECT * FROM libros WHERE id_libro = {id};"
        rows = await conn.fetch(query)
        if len(rows) > 0:
            libro = dict(rows[0])
        else:
            libro = {"mensaje": "El libro no existe"}
        return libro
    finally:
        await conn.close()
    

#Método DELETE
#URL '/libros/{id}'
#devuelve un mensaje
@app.delete('/libros/{id}')
async def eliminar_libro(id:int):
    print("Atendiendo DELETE /libros/",id)
    conn = await connect_db()
    try:
        query = f"DELETE FROM libros WHERE id_libro = {id};"
        await conn.execute(query)
        respuesta = {"mensaje": "Libro eliminado"}
        return respuesta
    finally:
        await conn.close()

#Método Get a usuarios
#URL '/usuarios'
#devuelve la lista de usuarios
@app.get('/usuarios')
async def lista_usuarios():
    print("Atendiendo GET /usuarios")
    conn = await connect_db()
    try:
        query = "SELECT * FROM usuarios;"
        rows = await conn.fetch(query)
        items = [dict(row) for row in rows]
        return items
    finally:
        await conn.close()

#Método Get a un solo usuario
#URL '/usuarios/{id}'
#devuelve un json
@app.get('/usuarios/{id}')
async def informacion_usuario(id:int):
    print("Atendiendo GET /usuarios/",id)
    conn = await connect_db()
    try:
        query = f"SELECT * FROM usuarios WHERE id_usuario = {id};"
        rows = await conn.fetch(query)
        if len(rows) > 0:
            usuario = dict(rows[0])
        else:
            usuario = {"mensaje": "El usuario no existe"}
        return usuario
    finally:
        await conn.close()

#Método DELETE a un usuario
#URL '/usuarios/{id}'
#devuelve un mensaje
@app.delete('/usuarios/{id}') 
async def eliminar_usuario(id:int):
    print("Atendiendo DELETE /usuarios/",id)
    conn = await connect_db()
    try:
        query = f"DELETE FROM usuarios WHERE id_usuario = {id};"
        await conn.execute(query)
        respuesta = {"mensaje": "Usuario eliminado"}
        return respuesta
    finally:
        await conn.close()

class LibroBase(BaseModel):
    titulo: str
    unidades: int=1             #valor por defecto
    autor: str
    unidades_disponibles: bool=True     #valor por defecto
    
class Prestamo(BaseModel):
    id_usuario: int
    id_libro: int
    
class UsuarioBase(BaseModel):
    nombre: str
    direccion: str
    
#Método POST a libros
#URL '/libros'
@app.post('/libros')
async def agregar_libro(libro: LibroBase):
    print("Atendiendo POST /libros")
    conn = await connect_db()
    try:
        query = f"INSERT INTO libros (titulo, unidades, autor, unidades_disponibles) VALUES ('{libro.titulo}', {libro.unidades}, '{libro.autor}', {libro.unidades_disponibles});"
        await conn.execute(query)
        respuesta = {
            "mensaje": "Libro agregado",
            "libro": libro
        }
        return respuesta
    finally:
        await conn.close()

# Put '/libros/{id}'
# orden de parametros: primero los de ruta y luego los de cuerpo
@app.put('/libros/{id}')
async def actualizar_disponibilidad_libro(id:int, libro:LibroBase):
    print("Atendiendo PUT /libros/",id)
    conn = await connect_db()
    try:
        query = f"UPDATE libros SET unidades_disponibles = {libro.unidades_disponibles} WHERE id_libro = {id};"
        await conn.execute(query)
        respuesta = {
            "mensaje": "Libro actualizado",
            "libro": libro
        }
        return respuesta
    finally:
        await conn.close()    

run(app, host='localhost', port=5000)