import sqlite3
from Entidades.Socio import Socio

conexion = sqlite3.connect('bd.db')

def agregar_socio(socio: Socio):
    with sqlite3.connect('bd.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO socios (dni, nombre, apellido, libros_prestados)
            VALUES (?, ?, ?, ?)
        ''', (socio.get_dni(), socio.get_nombre(), socio.get_apellido(), socio.get_libros_prestados()))

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
            SET nombre = ?, apellido = ? libros_prestados = ?
            WHERE dni = ?
        ''', (socio.get_nombre(), socio.get_apellido(), socio.get_libros_prestados(), socio.get_dni()))

def eliminar_socio(dni: int):
    with sqlite3.connect('bd.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            DELETE FROM socios
            WHERE dni = ?
        ''', (dni,))
