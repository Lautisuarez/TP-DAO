

from Entidades.Negocio import negocio

neg = negocio()

codigo_libro = 1
dni_socio = 1
dias_pactados = 1

print("1. Pedir libro")
print("2. Devolver libro")

seleccion = input("Selecciona una opción: ")

if seleccion == "1":
    neg.prestar_libro(codigo_libro, dni_socio, dias_pactados)
elif seleccion == "2":
    neg.devolver_libro(codigo_libro)



