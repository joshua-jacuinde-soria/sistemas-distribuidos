libros = [
    {
    "id_libro": 0,
    "titulo": "La Nausea",
    "unidades": 10,
    "autor": "Jean Paul Sartre",
    "unidades_disponibles":True},
{
    "id_libro": 1,
    "titulo": "Una habitación propia",
    "unidades": 8,
    "autor": "Virginia Wolf",
    "unidades_disponibles":False},
{
    "id_libro": 2,
    "titulo": "El pájaro espino",
    "unidades": 2,
    "autor": "Colleen McCullough",
    "unidades_disponibles": True},
{
    "id_libro": 3,
    "titulo": "El primer hombre",
    "unidades": 12,
    "autor": "Albert Camus",
    "unidades_disponibles": False}
]

prestamos = [
    {
        "id_prestamo": 0,
        "id_usuario": 0,
        "id_libro" : 0
    },
    {
        "id_prestamo": 1,
        "id_usuario": 1,
        "id_libro" : 1
    },
    {
        "id_prestamo": 2,
        "id_usuario": 0,
        "id_libro" : 3
    },
    {
        "id_prestamo": 3,
        "id_usuario": 1,
        "id_libro" : 2
    },
    {
        "id_prestamo": 4,
        "id_usuario": 2,
        "id_libro" : 1
    }
]

usuarios = [
    {
        "id_usuario": 0,
        "nombre": "Flor Juárez",
        "direccion": "Av. Vasco de Quiroga S/N"
    },
    {
        "id_usuario": 1,
        "nombre": "Juan Pérez",
        "direccion": "Av. Constituyentes #1200"
    },
    {
        "id_usuario": 2,
        "nombre": "Itzel Martínez",
        "direccion": "Calle 13 #66"
    }
]

# conversion a query 

#create table libros( id_libro int, titulo varchar(100), unidades int, autor varchar(100), unidades_disponibles boolean);
#insert into libros values(0, 'La Nausea', 10, 'Jean Paul Sartre', true),
#   (1, 'Una habitación propia', 8, 'Virginia Wolf', false),
#   (2, 'El pájaro espino', 2, 'Colleen McCullough', true),
#   (3, 'El primer hombre', 12, 'Albert Camus', false);

# create table usuarios( id_usuario int, nombre varchar(100), direccion varchar(100));
# insert into usuarios values(0, 'Flor Juárez', 'Av. Vasco de Quiroga S/N'),
#   (1, 'Juan Pérez', 'Av. Constituyentes #1200'),
#   (2, 'Itzel Martínez', 'Calle 13 #66');

# create table prestamos( id_prestamo int, id_usuario int, id_libro int);
# insert into prestamos values(0, 0, 0), (1, 1, 1), (2, 0, 3), (3, 1, 2), (4, 2, 1);


