import sqlite3

from Entidades.Negocio import calcular_demora
from Entidades.Prestamo import Prestamo


def cantidad_libros_por_estado():
    with sqlite3.connect('bd.db') as conexion:
            cursor = conexion.cursor()
            cursor.execute('''
                SELECT "disponible", COUNT(*) FROM libros
                WHERE estado = "disponible"
            ''')
            disponibles = cursor.fetchone()
            cursor.execute('''
                SELECT "extraviado", COUNT(*) FROM libros
                WHERE estado = "extraviado"
            ''')
            extraviados = cursor.fetchone()
            cursor.execute('''
                SELECT "prestado", COUNT(*) FROM libros
                WHERE estado = "prestado"
            ''')
            prestados = cursor.fetchone()
            resultados =  disponibles + prestados + extraviados
            return resultados
            

def precio_libros_extraviados():
    with sqlite3.connect('bd.db') as conexion:
            cursor = conexion.cursor()
            cursor.execute('''
                SELECT SUM(precio_reposicion) as suma_precio_reposicion
                FROM libros
                WHERE estado = 'extraviado'
            ''')
            resultado_suma_precio = cursor.fetchone()
            return resultado_suma_precio[0] if resultado_suma_precio[0] else 0
       
       
def nombres_solicitantes_libro(titulo):
    with sqlite3.connect('bd.db') as conexion:
        cursor = conexion.cursor()

        # Obtener el código del libro por su título
        cursor.execute('SELECT codigo FROM libros WHERE titulo = ?', (titulo,))
        codigo_libro = cursor.fetchone()
        if codigo_libro:
            # Obtener los solicitantes del libro por su código
            cursor.execute('''
                SELECT DISTINCT s.nombre
                FROM prestamos p
                JOIN socios s ON p.codigo_socio = s.dni
                WHERE p.codigo_libro = ?
            ''', (codigo_libro[0],))
            solicitantes = cursor.fetchall()
            nombres = [nombre[0] for nombre in solicitantes]
            return nombres if len(nombres) > 0 else "NO HAY SOLICITANTES"
        else:
            return "NO HAY UN LIBRO CON ESE NOMBRE"
 
def prestamos_por_socio(dni_socio):
    with sqlite3.connect('bd.db') as conexion:
        cursor = conexion.cursor()

        # Obtener los préstamos del socio por su número de socio
        cursor.execute('''
            SELECT *
            FROM prestamos 
            WHERE codigo_socio = ?
        ''', (dni_socio,))
        prestamos_socio = cursor.fetchall()
        
        prestaciones = [Prestamo(*prestamo) for prestamo in prestamos_socio]
        return prestaciones


def prestamos_demorados():
    with sqlite3.connect('bd.db') as conexion:
        cursor = conexion.cursor()

        cursor.execute('''
            SELECT *
            FROM prestamos
        ''')
        response = cursor.fetchall()
        
        demorados = []
        prestaciones = [Prestamo(*prestamo) for prestamo in response]
        for prestamo in prestaciones:
            if calcular_demora(prestamo) > 0:
                demorados.append(prestamo)
        return demorados
        