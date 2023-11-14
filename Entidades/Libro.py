import datetime
from Entidades import Prestamo
from Entidades import Socio


class Libro:
    _titulo = ""
    _precio_reposicion = 0
    _estado = ""

    def __init__(self, codigo : int, titulo: str, precio_reposicion : float):
        self._codigo = codigo
        self._titulo = titulo
        self._precio_reposicion = precio_reposicion
        self._estado = "disponible"

    def get_codigo(self) -> int:
        return self._codigo

    def get_titulo(self) -> str:
        return self._titulo

    def set_titulo(self, titulo: str):
        self._titulo = titulo

    def get_precio_reposicion(self) -> float:
        return  self._precio_reposicion

    def set_precio_reposicion(self, precio_reposicion: float):
         self._precio_reposicion = precio_reposicion

    def get_estado(self) -> str:
        return self._estado

    def set_estado(self,valor):
        #(disponible, x defecto
        # prestado  --> asociado a un socio 
        # extraviado -->  libro prestado y que posea más de 30 días de demora en su devolución se considera extraviado.
        self._estado = valor
        