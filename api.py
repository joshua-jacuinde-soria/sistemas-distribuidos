from fastapi import FastAPI
from bd_biblioteca import libros, usuarios
from uvicorn import run

app = FastAPI()

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
def lista_libros():
    print("Atendiendo GET '/libros'")
    respuesta = libros
    return respuesta

#Metodo GET
#URL '/libros/{id}'
#devuelve un json
#parametro de ruta id
@app.get('/libros/{id}')
def informacion_libro(id:int):
    print("Atendiendo GET /libros/",id)
    if id >=0 and id <=len(libros)-1:
        respuesta = libros[id]
    else:
        respuesta = {
            "mensaje":"El libro no existe"
        }
    return respuesta

#Método DELETE
#URL '/libros/{id}'
#devuelve un mensaje
@app.delete('/libros_borrar/{id}')
def eliminar_libro(id:int):
    print("Atendiendo DELETE /libros/",id)
    if id >=0 and id <=len(libros)-1:
        respuesta = {
            "mensaje": "El libro ha sido eliminado"
        }
        del libros[id]
    else:
        respuesta = {
            "mensaje": "El libro no existe"
        }
    return respuesta

#Método Get a usuarios
#URL '/usuarios'
#devuelve la lista de usuarios
@app.get('/usuarios')
def lista_usuarios():
    print("Atendiendo GET '/usuarios'")
    respuesta = usuarios
    return respuesta

#Método Get a un solo usuario
#URL '/usuarios/{id}'
#devuelve un json
@app.get('/usuarios/{id}')
def informacion_usuario(id:int):
    print("Atendiendo GET /usuarios/",id)
    if id >=0 and id <=len(usuarios)-1:
        respuesta = usuarios[id]
    else:
        respuesta = {
            "mensaje":"El usuario no existe"
        }
    return respuesta

#Método DELETE a un usuario
#URL '/usuarios/{id}'
#devuelve un mensaje
@app.delete('/usuariosbo/{id}')
def eliminar_usuario(id:int):
    print("Atendiendo DELETE /usuarios/",id)
    if id >=0 and id <=len(usuarios)-1:
        respuesta = {
            "mensaje": "El usuario ha sido eliminado"
        }
        del usuarios[id]
    else:
        respuesta = {
            "mensaje": "El usuario no existe"
        }
    return respuesta


run(app, host='localhost', port=8000)
