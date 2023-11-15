import datetime
import sqlite3

class Prestamo:
    def init(self, codigo_libro : int, DNI_socio: int, dias_pactados: int):
        self._codigo_libro = codigo_libro
        self._dni_socio = DNI_socio
        self._fechaPrestamo = datetime.now()
        self._dias_pactados = dias_pactados
        self._fecha_devolucion = self.set_fecha_devolucion(None)
        
        self._librosPrestados = self.obtener_libros_prestados()

    def get_codigo_libro(self) -> int:
        return self._codigo_libro
    
    def get_dni_socio(self) -> int:
        return self._dni_socio
    
    def set_dni_socio(self, dni_socio: int):
        self._dni_socio = dni_socio
 
    def get_dias_pactados(self) -> int:
        return self._dias_pactados 
    
    def set_dias_pactados(self, dias_pactados: int):
        self._dias_pactados = dias_pactados
        
    def get_fecha_prestamo(self):
        return self._fechaPrestamo
    
    def get_fecha_devolucion(self) -> int:
        return self._fecha_devolucion
    
    def set_fecha_devolucion(self, fecha_devolucion):
        self._fecha_devolucion = fecha_devolucion
    
    # DESDE ACA MUCHAS DUDAS #######################
        
    def prestar_libro(self, codigo_libro , dni_socio, dias_pactados):
        #Cuando un socio solicite un libro el software debe verificar que el socio no posea más de tres libros prestados 
        # (aunque todavía se encuentre dentro del plazo del préstamo) y que no posea ningún libro con demora en su devolución

        if(self.contar_libros_prestados_por_socio > 3 or self.socio_tiene_libros_con_demora(dni_socio) == True):
            return f"El socio no puede solicitar el libro"
        # Cada vez que un libro es prestado se registra el socio que lo solicita y la cantidad de días pactados para su devolución.
        else:
            nuevoPrestamo = Prestamo(codigo_libro, dni_socio, datetime.now(), dias_pactados)
            self.agregar_librosPrestados(nuevoPrestamo)
            #Libro.set_estado("prestado")
            self.cambiar_estado_libro(codigo_libro, "prestado")
            
    def devolver_libro(self, codigo_libro):
        # Actualiza la fecha de devolución y la demora al momento de la devolución
        for prestamo in self._librosPrestados:
            if prestamo.get_codigo_libro() == codigo_libro:
                prestamo.set_fecha_devolucion(datetime.now)
                # cambiar el estado de este libro --> set_estado("disponible")
                self.cambiar_estado_libro(codigo_libro, "disponible")
                

    def agregar_librosPrestados(self, prestamo):
        with sqlite3.connect('bd.db') as conexion:
                    cursor = conexion.cursor()
                    cursor.execute('''SELECT COALESCE(MAX(id), 1) FROM prestaciones''')
                    lastid = cursor.fetchone()
                    
                    cursor.execute('''
                        INSERT INTO prestaciones (id, codigo_libro, codigo_socio, dias_pactados)
                        VALUES (?, ?, ?, ?)
                    ''', (lastid, prestamo.get_codigo_libro(), prestamo.get_dni_socio(), prestamo.get_dias_pactados))
                    conexion.commit()      
        
    def contar_libros_prestados_por_socio(self,dni_socio):
        contador = 0
        for prestamo in self._librosPrestados:
            if prestamo.get_dni_socio() == dni_socio:
                contador += 1
        return contador
    
    def socio_tiene_libros_con_demora(self, dni_socio):
        # Verifica si el socio tiene libros con demora en la devolución
        demora = False
        for prestamo in self._librosPrestados:
            if prestamo.get_codigo_socio() == dni_socio:
               if self.calcular_demora(prestamo) > 0:
                   demora = True
        return demora 
    
    def calcular_demora(self, libro_prestado):           
        if libro_prestado.get_fecha_devolucion() == None:
            dias_prestamo = datetime.now().day - libro_prestado.get_fechaPrestamo().day
            #if dias_prestamo - libro_prestado.get_dias_pactados() > 30:
                # cambiarle el estado libro_prestado.set_estado("extraviado")
                 
                              
        return  dias_prestamo - self.dias_pactados  # si es negativo es porque no hay demora
    
    def cambiar_estado_libro(self, codigo_libro, estado):
        libro: Libro = obtener_libros_by_codigo(codigo_libro)
        libro.set_estado(estado)
        actualizar_libro(libro)
    
    def obtener_extraviados(self):
        listaExtraviados = []
        for prestacion in self._librosPrestados:
            if (prestacion.get_fecha_prestamo()
                + datetime.timedelta(days=prestacion.get_dias_pactados())
                - datetime.now()).day > 30:
                listaExtraviados.append(prestacion)
                ###
                #self.cambiar_estado_libro(prestacion.get_codigo_libro(), "extraviado")
                
                
    
    def obtener_libros_prestados():
        with sqlite3.connect('bd.db') as conexion:
            cursor = conexion.cursor()
            cursor.execute('''
                SELECT * FROM prestaciones
            ''')
            prestaciones = cursor.fetchall()
            return prestaciones