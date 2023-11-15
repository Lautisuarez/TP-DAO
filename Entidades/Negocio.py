

from datetime import datetime
import sqlite3
from Cruds.crudLibro import actualizar_libro, obtener_libros_by_codigo
from Entidades.Libro import Libro
from Entidades.Prestamo import Prestamo


class negocio:

    def prestar_libro(self, codigo_libro , dni_socio, dias_pactados):
        #Cuando un socio solicite un libro el software debe verificar que el socio no posea más de tres libros prestados 
        # (aunque todavía se encuentre dentro del plazo del préstamo) y que no posea ningún libro con demora en su devolución

        if(self.contar_libros_prestados_por_socio(dni_socio) > 3 or self.socio_tiene_libros_con_demora(dni_socio) == True):
            return f"El socio no puede solicitar el libro"
        # Cada vez que un libro es prestado se registra el socio que lo solicita y la cantidad de días pactados para su devolución.
        elif (not self.libro_disponible(codigo_libro)):
            print(f"El libro no esta disponible")
            return f"El libro no esta disponible"
        else:
            nuevoPrestamo = Prestamo(self.ultimo_id_prestamos(), codigo_libro, dni_socio,datetime.now(), dias_pactados, None, None)
            # agrega la prestacion a la BD
            self.agregar_prestacion(nuevoPrestamo)
            # cambia el estado dle libro en la BD
            self.cambiar_estado_libro(codigo_libro, "prestado")
            
        
    def devolver_libro(self, codigo_libro):
        # Actualiza la fecha de devolución y la demora al momento de la devolución
        for prestamo in self.obtener_pretaciones():
            if prestamo.get_codigo_libro() == codigo_libro:
                
                prestamo.set_fecha_devolucion(datetime.now())
                
                # obtengo la demora de la prestacion
                demora = self.calcular_demora(prestamo)
                
                # si hay demora lo guardo sino queda en None o Null
                if demora > 0:
                    prestamo.set_demora(demora)
                
                # actualizar en BD el prestamo
                self.actualizar_prestamo(prestamo)
                
                # cambiar le estado del libro en BD
                self.cambiar_estado_libro(codigo_libro, "disponible")
    
    # proceso para guardar en BD la prestacion
    def agregar_prestacion(self, prestamo: Prestamo):
        with sqlite3.connect('bd.db') as conexion:
                    cursor = conexion.cursor()
                    
                    cursor.execute('''
                        INSERT INTO prestamos (id, codigo_libro, codigo_socio, dias_pactados, fecha_prestamo)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (prestamo.get_id(),
                          prestamo.get_codigo_libro(),
                          prestamo.get_dni_socio(),
                          prestamo.get_dias_pactados(),
                          prestamo.get_fecha_prestamo()))
                    conexion.commit()      
    
    # obtiene le ultimo id de la tabla prestamos
    def ultimo_id_prestamos(self):
        with sqlite3.connect('bd.db') as conexion:
                    cursor = conexion.cursor()
                    cursor.execute('''SELECT COALESCE(MAX(id), 0) FROM prestamos''')
                    response = cursor.fetchone()
                    return response[0] + 1
        
    # cuenta cantidad de libros prestados por socios
    def contar_libros_prestados_por_socio(self,dni_socio):
        contador = 0
        for prestamo in self.obtener_pretaciones():
            if prestamo.get_dni_socio() == dni_socio:
                contador += 1
        return contador
    
    # Verifica si el socio tiene libros con demora en la devolución
    def socio_tiene_libros_con_demora(self, dni_socio):
        for prestamo in self.obtener_pretaciones():
            if prestamo.get_dni_socio() == dni_socio:
               if self.calcular_demora(prestamo) > 0:
                   return True
        return False
    
    # este metodo podria estar en la entidad Prestamos
    # calcula la demora entre la fecha actual y la fecha que se presto el libro mas los dias pactados
    def calcular_demora(self, prestamo: Prestamo):           
        formato_cadena = "%Y-%m-%d %H:%M:%S.%f"
        fecha_prestamo = datetime.strptime(prestamo.get_fecha_prestamo(), formato_cadena)
        dias_transcurridos_prestamo = datetime.now().day - fecha_prestamo.day
        return  dias_transcurridos_prestamo - prestamo.get_dias_pactados()  # si es negativo es porque no hay demora
        
    # obtiene de la BD el libro, le cambia el estado y lo vuelve a guardar en la BD
    def cambiar_estado_libro(self, codigo_libro: int, estado):
        libro:Libro = obtener_libros_by_codigo(codigo_libro)
        libro.set_estado(estado)
        actualizar_libro(libro)
    
    # Obiente los prestamos no devueltos que superen los 30 dias de demora
    def obtener_extraviados(self):
        listaExtraviados = []
        for prestacion in self.obtener_pretaciones():
            if self.calcular_demora(prestacion) > 30:
                listaExtraviados.append(prestacion)
                #self.cambiar_estado_libro(prestacion.get_codigo_libro(), "extraviado")
        return listaExtraviados
    
    # devuelve los prestamos que no han sido finalizados es decir q los libros ya se hayan devuelto
    def obtener_pretaciones(self):
        with sqlite3.connect('bd.db') as conexion:
            cursor = conexion.cursor()
            cursor.execute('''
                SELECT * FROM prestamos WHERE fecha_devolucion ISNULL
            ''')
            lista_bd = cursor.fetchall()
            # mapeo de la base de datos a una lista de objetos prestamos
            prestaciones = [Prestamo(*prestamo) for prestamo in lista_bd]
            return prestaciones
    
    
    # valida si el libro a pedir esta con el estado disponible
    def libro_disponible(self, codigo_libro):
        libro: Libro = obtener_libros_by_codigo(codigo_libro)
        return libro.get_estado() == "disponible"


    # guarda en la base de datos la devolucion de un libro, solo con fecha y demora 
    def actualizar_prestamo(self, prestamo:Prestamo):
        with sqlite3.connect('bd.db') as conexion:
            cursor = conexion.cursor()
            cursor.execute('''
                UPDATE prestamos
                SET fecha_devolucion = ?, demora = ?
                WHERE id = ?
            ''',(prestamo.get_fecha_devolucion(), prestamo.get_demora(), prestamo.get_id()))
            conexion.commit()