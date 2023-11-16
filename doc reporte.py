from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

#hacer pip install reportLab

"""Reportes:
Cantidad de libros en cada estado (tres totales)
Sumatoria del precio de reposición de todos los libros extraviados
Nombre de todos los solicitantes de un libro en particular identificado por su título
Listado de préstamos de un socio identificado por su número de socio
Listado de préstamos demorados
"""
# Crear un documento PDF
doc = SimpleDocTemplate("report.pdf", pagesize=letter,
                        rightMargin=72, leftMargin=72,
                        topMargin=72, bottomMargin=18)

# Crear una lista para almacenar los elementos del informe
elements = []

# Crear estilos para el informe
styles = getSampleStyleSheet()

# Agregar un título
title = "Reportes libreria PDF"
elements.append(Paragraph(title, styles['Title']))

# REPORTE 1
reporte_1 = "1) Cantidad de libros en cada estado"
elements.append(Paragraph(reporte_1, styles['Normal']))

# REPORTE 2
reporte_2 = "2) Sumatoria del precio de reposición de todos los libros extraviados"
elements.append(Paragraph(reporte_2, styles['Normal']))

# REPORTE 3
reporte_3 = "3) Nombre de todos los solicitantes de un libro en particular identificado por su título"
elements.append(Paragraph(reporte_3, styles['Normal']))

# REPORTE 4
reporte_4 = "4) Listado de préstamos de un socio identificado por su número de socio"
elements.append(Paragraph(reporte_4, styles['Normal']))

# REPORTE 5
reporte_5 = "5) Listado de préstamos demorados"
elements.append(Paragraph(reporte_5, styles['Normal']))

# Construir el informe y guardar en un archivo PDF
doc.build(elements)
