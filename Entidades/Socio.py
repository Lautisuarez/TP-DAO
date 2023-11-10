class Socio:
    def __init__(self, codigo: int, nombre: str, libros_prestados: int):
        self._codigo = codigo
        self._nombre = nombre
        self._libros_prestados = libros_prestados

    def get_codigo(self) -> int:
        return self._codigo

    def get_nombre(self) -> str:
        return self._nombre

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def get_libros_prestados(self) -> int:
        return self._libros_prestados

    def set_libros_prestados(self, libros_prestados: int):
        self._libros_prestados = libros_prestados
