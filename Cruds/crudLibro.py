import sqlite3
from Entidades.Libro import Libro
from bd import connection_bd

def agregar_libro(libro : Libro):
    with sqlite3.connect('bd.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO libros (titulo, precio_reposicion, estado)
            VALUES (?, ?, ?)
        ''', (libro.get_titulo(),libro.get_precio_reposicion(),libro.get_estado()))

def obtener_libros():
    with sqlite3.connect('bd.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            SELECT * FROM libros
        ''')
        libros = cursor.fetchall()
        return libros

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


            