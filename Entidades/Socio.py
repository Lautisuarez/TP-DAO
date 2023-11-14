
import datetime
from Entidades import Prestamo

class Socio:
    def __init__(self, dni: int, nombre: str, apellido :str,libros_prestados):
        self._dni = dni
        self._nombre = nombre
        self.apellido = apellido
        #self._libros_prestados = []

    def get_dni(self) -> int:
        return self._dni

    def get_nombre(self) -> str:
        return self._nombre

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def get_apellido(self) -> str:
        return self._apellido
    
    def set_apellido(self, apellido: str):  
        self._apellido = apellido
        
    '''def get_libros_prestados(self):
        return self._libros_prestados

    def agregar_libro_prestado(self, prestamo):
        self._libros_prestados.append(prestamo)

    def cantidad_libros_prestados(self):
        # Retorna la cantidad de libros prestados
        return len(self._libros_prestados)
    
    def libros_con_demora(self):
        # Verifica si el socio tiene libros con demora en la devolución
        demora = False
        for libro_prestado in self._libros_prestados:
            if Prestamo.calcular_demora(libro_prestado) > 0:
                demora = True
                #if Prestamo.calcular_demora(libro_prestado) > 30:
                # cambiarle el estado libro_prestado.set_estado("extraviado")  #como cambio el estado del libro???
        return demora '''

    
    
    """def libros_prestados(self):                  es para mostrar la lista
        # Retorna la lista de libros prestados por el socio
        for libro in self._libros_prestados:
            return libro"""
               
    
    
