import sqlite3
from Entidades.Socio import Socio
from bd import connection_bd

conexion = sqlite3.connect('bd.db')

def agregar_socio(socio: Socio):
    with sqlite3.connect('bd.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO socios (codigo, nombre, libros_prestados)
            VALUES (?, ?, ?)
        ''', (socio.get_codigo(), socio.get_nombre(), socio.get_libros_prestados()))

def obtener_socios():
    with sqlite3.connect('bd.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            SELECT * FROM socios
        ''')
        socios = cursor.fetchall()
        return Socio

def actualizar_socio(socio: Socio):
    with sqlite3.connect('bd.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            UPDATE socios
            SET nombre = ?, libros_prestados = ?
            WHERE codigo = ?
        ''', (socio.get_nombre(), socio.get_libros_prestados(), socio.get_codigo()))

def eliminar_socio(codigo: int):
    with sqlite3.connect('bd.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            DELETE FROM socios
            WHERE codigo = ?
        ''', (codigo,))
