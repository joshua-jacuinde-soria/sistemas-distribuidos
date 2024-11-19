create table libros(
	id_libro serial primary key , 
	titulo varchar(100), 
	unidades int, 
	autor varchar(100), 
	unidades_disponibles boolean);

insert into libros(titulo, unidades, autor, unidades_disponibles) values
	('La Nausea', 10, 'Jean Paul Sartre', true),
   	('Una habitación propia', 8, 'Virginia Wolf', false),
   	('El pájaro espino', 2, 'Colleen McCullough', true),
   	('El primer hombre', 12, 'Albert Camus', false);

 create table usuarios( 
	 id_usuario serial primary key,
	 nombre varchar(100), 
	 direccion varchar(100));

 insert into usuarios(nombre, direccion) values
	('Flor Juárez', 'Av. Vasco de Quiroga S/N'),
   	('Juan Pérez', 'Av. Constituyentes #1200'),
   	('Itzel Martínez', 'Calle 13 #66');

drop table libros;

create table prestamos(
	id_prestamo serial primary key,
	id_usuario int,
	id_libro int,
	foreign key(id_usuario) references usuarios(id_usuario),
	foreign key (id_libro) references libros(id_libro));

insert into prestamos(id_usuario, id_libro) values
	(1, 1),
	(2, 2), 
	(1, 4),
	(2, 3),
	(3, 2);

select * from prestamos;