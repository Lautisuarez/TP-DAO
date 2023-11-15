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
        conexion.commit()

def obtener_socios():
    with sqlite3.connect('bd.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            SELECT * FROM socios
        ''')
        socios = cursor.fetchall()
        return socios
    
def obtener_socios_by_dni(dni):
    with sqlite3.connect('bd.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            SELECT * FROM socios where dni = ?
        ''',(dni))
        socio = cursor.fetchone()
        if not socio:
            raise ValueError(f"No se encontró el socio con dni {dni}")
            
        return socio

def actualizar_socio(socio: Socio):
    with sqlite3.connect('bd.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            UPDATE socios
            SET nombre = ?, apellido = ? libros_prestados = ?
            WHERE dni = ?
        ''', (socio.get_nombre(), socio.get_apellido(), socio.get_libros_prestados(), socio.get_dni()))
        conexion.commit()
def eliminar_socio(dni: int):
    with sqlite3.connect('bd.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            DELETE FROM socios
            WHERE dni = ?
        ''', (dni,))
        conexion.commit()
