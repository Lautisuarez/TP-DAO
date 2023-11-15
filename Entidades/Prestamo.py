from datetime import datetime
import sqlite3

class Prestamo:
    
    def __init__(self,id , codigo_libro : int, DNI_socio: int, fechaPrestamo: datetime, dias_pactados: int, fechaDevolucion: datetime, demora: int):
        self._id = id
        self._codigo_libro = codigo_libro
        self._dni_socio = DNI_socio
        self._fechaPrestamo = fechaPrestamo
        self._dias_pactados = dias_pactados
        self._fecha_devolucion = fechaDevolucion
        self._demora = demora
    
        
    def get_id(self) -> int:
            return self._id
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
        
    def get_fecha_prestamo(self) -> datetime:
        return self._fechaPrestamo
    
    def get_fecha_devolucion(self) -> int:
        return self._fecha_devolucion
    
    def set_fecha_devolucion(self, fecha_devolucion):
        self._fecha_devolucion = fecha_devolucion
        
    def set_demora(self, demora):
        self._demora = demora
        
    def get_demora(self):
        return self._demora
    
    def __str__(self):
        return f"\n ID={self.get_id()},\n CodigoLibro={self.get_codigo_libro()},\n DNISocio={self.get_dni_socio()}, " \
               f"\nFechaPrestamo={self.get_fecha_prestamo()},\n DiasPactados={self.get_dias_pactados()},\n " \
               f"FechaDevolucion={self.get_fecha_devolucion()}, \n Demora={self.get_demora()})\n"

