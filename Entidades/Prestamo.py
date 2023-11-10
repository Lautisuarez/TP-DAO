class Prestamo:
    def init(self, codigo_libro : int, codigo_socio: int, dias_pactados: int, fecha_devolucion, demora : int):
        self.codigo_libro = codigo_libro
        self.codigo_socio = codigo_socio
        self.dias_pactados = dias_pactados
        self.fecha_devolucion = fecha_devolucion
        self.demora = demora

    def get_codigo_libro(self) -> int:
        return self._codigo
    
    def get_codigo_socio(self) -> int:
        return self._codigo_socio
        
    def set_codigo_socio(self, codigo_socio: int) -> int:
        self._codigo_socio = codigo_socio

    def get_dias_pactados(self) -> int:
        return self._dias_pactados 
    
    def set_dias_pactados(self, dias_pactados: int):
        self._dias_pactados = dias_pactados
    
    def get_fecha_devolucion(self) -> int:
        return self._fecha_devolucion
    
    def set_fecha_devolucion(self, fecha_devolucion):
        self._fecha_devolucion = fecha_devolucion
    
    def get_demora(self) -> int:
        return self._demora
    
    def set_demora(self, demora: int):
        self._demora = demora
    