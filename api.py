from fastapi import FastAPI
from bd_biblioteca import libros
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
@app.delete('/libros/{id}')
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

run(app, host='localhost', port=8000)
