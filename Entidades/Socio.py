
import datetime
from Entidades import Prestamo

class Socio:
    def __init__(self, dni: int, nombre: str, apellido :str):
        self._dni = dni
        self._nombre = nombre
        self.apellido = apellido

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
    
    
