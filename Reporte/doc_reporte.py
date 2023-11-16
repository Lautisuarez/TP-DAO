from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

#hacer pip install reportLab
from Reporte.reportes import *

"""Reportes:
Cantidad de libros en cada estado (tres totales)
Sumatoria del precio de reposicion de todos los libros extraviados
Nombre de todos los solicitantes de un libro en particular identificado por su titulo
Listado de prestamos de un socio identificado por su numero de socio
Listado de prestamos demorados
"""
def generar_reporte(nombre_libro, codigo_socio):
    # Crear un documento PDF
    doc = SimpleDocTemplate("report.pdf", pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=28)

    # Crear una lista para almacenar los elementos del informe
    elements = []

    # Crear estilos para el informe
    styles = getSampleStyleSheet()

    # Agregar un titulo
    title = "Reportes libreria PDF"
    elements.append(Paragraph(title, styles['Title']))

    # REPORTE 1
    reporte_1 = "1) Cantidad de libros en cada estado \n"
    estado_disponible = "Disponibles: " + str(cantidad_libros_por_estado()[0]) + "\n"
    estado_prestado = "Prestados: " + str(cantidad_libros_por_estado()[1]) + "\n"
    estado_extraviado = "Extraviados: " + str(cantidad_libros_por_estado()[2]) + "\n"
    elements.append(Paragraph(reporte_1, styles['Normal']))
    elements.append(Paragraph(estado_disponible, styles['Normal']))
    elements.append(Paragraph(estado_prestado, styles['Normal']))
    elements.append(Paragraph(estado_extraviado , styles['Normal']))

    # REPORTE 2
    reporte_2 = "2) Sumatoria del precio de reposicion de todos los libros extraviados: " + str(precio_libros_extraviados())
    elements.append(Paragraph(reporte_2, styles['Normal']))

    # REPORTE 3
    reporte_3 = "3) Nombre de todos los solicitantes de un libro en particular identificado por su titulo"
    elements.append(Paragraph(reporte_3, styles['Normal']))
    nombres = nombres_solicitantes_libro(nombre_libro)
    elements.append(Paragraph(f"Nombre Libro: {nombre_libro}", styles['Normal']))
    for nombre in nombres:
        elements.append(Paragraph(nombre, styles['Normal']))

    # REPORTE 4
    reporte_4 = "4) Listado de prestamos de un socio identificado por su numero de socio"
    elements.append(Paragraph(reporte_4, styles['Normal']))
    prestamos_de_socio = prestamos_por_socio(codigo_socio)
    elements.append(Paragraph(f"Socio: {codigo_socio}", styles['Normal']))
    for prestamo in prestamos_de_socio:
        elements.append(Paragraph(prestamo.__str__(), styles['Normal']))

    # REPORTE 5
    reporte_5 = "5) Listado de prestamos demorados \n"
    elements.append(Paragraph(reporte_5, styles['Normal']))

    demorados = prestamos_demorados()
    for prestamo in demorados:
        elements.append(Paragraph(prestamo.__str__(), styles['Normal']))

    # Construir el informe y guardar en un archivo PDF
    doc.build(elements)
