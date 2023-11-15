# TP DAO

## Alumnos:
- Lucas Gastiaburu
- Rocio Rodriguez
- Ivan Casatti
- Lautaro Suárez


Una biblioteca necesita un software que le permita registrar los datos de los libros que posee y de sus préstamos. De cada libro conoce como mínimo su código, título, precio de reposición (para el caso de extravíos o daños) y estado (disponible, prestado o extraviado).

Por otro lado, cada vez que un libro es prestado se registra el socio que lo solicita y la cantidad de días pactados para su devolución. Cuando un libro es devuelto debe calcularse si fue devuelto en fecha o con demora, registrando si corresponde la cantidad de días de retraso.

Todo libro prestado y que posea más de 30 días de demora en su devolución se considera extraviado, por lo tanto el software debe poder listar aquellos que se encuentren en tal condición para ofrecer al usuario el cambio de estado.

Cuando un socio solicite un libro el software debe verificar que el socio no posea más de tres libros prestados (aunque todavía se encuentre dentro del plazo del préstamo) y que no posea ningún libro con demora en su devolución.

## La biblioteca requiere que el software ofrezca como mínimo las funcionalidades de:

- Administración de socios
- Administración de libros
- Registración de préstamos y devoluciones
- Registración de libros extraviados
## Reportes:
- Cantidad de libros en cada estado (tres totales)
- Sumatoria del precio de reposición de todos los libros extraviados
- Nombre de todos los solicitantes de un libro en particular identificado por su título
- Listado de préstamos de un socio identificado por su número de socio
- Listado de préstamos demorados
## Condiciones de entrega:

Los datos deben ser almacenados en una base de datos sqlite cuyo diseño y creación es responsabilidad del grupo.
La interfaz de usuario debe ser una interfaz gráfica con ventanas usando tkinter.
Todos los datos ingresados por el usuario deben ser correctamente validados.
La entrega se realiza mediante el módulo de tareas de la UV de un único archivo comprimido que incluya únicamente los archivos de código fuente, el archivo de la base de datos y el diagrama de entidad-relación.