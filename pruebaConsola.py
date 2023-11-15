

from Entidades.Negocio import *
from reportes import *

codigo_libro = 2
dni_socio = 2
dias_pactados = -10
titulo_libro = "libro1"
print("1. Pedir libro")
print("2. Devolver libro")
print("3. Reportes")

obtener_extraviados()

seleccion = input("Selecciona una opción: ")

if seleccion == "1":
    prestar_libro(codigo_libro, dni_socio, dias_pactados)
elif seleccion == "2":
    devolver_libro(codigo_libro)
else:
    print(f"cantidad libros: {cantidad_libros_por_estado()}")
    print(f"Suma de libros extraviados: {precio_libros_extraviados()}")
    print(f"Nombres {nombres_solicitantes_libro(titulo_libro)}")
    print(f"Prestamos de alguien: {prestamos_por_socio(dni_socio)}")
    print(f"Prestamos demorados: {prestamos_demorados()}")




