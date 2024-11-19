create table libros( id_libro int, titulo varchar(100), unidades int, autor varchar(100), unidades_disponibles boolean);
insert into libros values(0, 'La Nausea', 10, 'Jean Paul Sartre', true),
   (1, 'Una habitación propia', 8, 'Virginia Wolf', false),
   (2, 'El pájaro espino', 2, 'Colleen McCullough', true),
   (3, 'El primer hombre', 12, 'Albert Camus', false);

 create table usuarios( id_usuario int, nombre varchar(100), direccion varchar(100));
 insert into usuarios values(0, 'Flor Juárez', 'Av. Vasco de Quiroga S/N'),
   (1, 'Juan Pérez', 'Av. Constituyentes #1200'),
   (2, 'Itzel Martínez', 'Calle 13 #66');

create table prestamos( id_prestamo int, id_usuario int, id_libro int);
insert into prestamos values(0, 0, 0), (1, 1, 1), (2, 0, 3), (3, 1, 2), (4, 2, 1);