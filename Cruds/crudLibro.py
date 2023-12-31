import sqlite3
from Entidades.Libro import Libro

def agregar_libro(libro : Libro):
    with sqlite3.connect('bd.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO libros (codigo, titulo, precio_reposicion, estado)
            VALUES (?, ?, ?, ?)
        ''', (libro.get_codigo(), libro.get_titulo(),libro.get_precio_reposicion(),libro.get_estado()))
        conexion.commit()
def obtener_libros():
    with sqlite3.connect('bd.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            SELECT * FROM libros
        ''')
        libros = cursor.fetchall()
        return libros

def obtener_libros_by_codigo(codigo: int):
    with sqlite3.connect('bd.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            SELECT * FROM libros WHERE codigo = ?
        ''', (codigo,))
        response = cursor.fetchone()
        
        if not response:
            raise ValueError(f"No se encontró el libro con codigo {codigo}")
        
        libro: Libro = Libro(response[0], response[1], response[2], response[3])
        
        return libro

def actualizar_libro(libro: Libro):
    with sqlite3.connect('bd.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            UPDATE libros
            SET titulo = ?, precio_reposicion = ?, estado = ?
            WHERE codigo = ?
        ''', (libro.get_titulo(), libro.get_precio_reposicion(), libro.get_estado(), libro.get_codigo()))
        conexion.commit()


def eliminar_libro(codigo: int):
    with sqlite3.connect('bd.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            DELETE FROM libros
            WHERE codigo = ?
        ''', (codigo,))
        conexion.commit()


            