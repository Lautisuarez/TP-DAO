import tkinter as tk
from tkinter import ttk
from Interfaz.Libreria import LibreriaApp
from Interfaz.Reporte import ReporteApp
from Interfaz.Socios import SocioApp
from Interfaz.Prestamo import PrestamoApp

# Funciones para alternar entre las interfaces
def mostrar_libreria():
    frame_socios.grid_remove()
    frame_libreria.grid()

def mostrar_socios():
    frame_libreria.grid_remove()
    frame_socios.grid()

root = tk.Tk()
root.title("Gestión de Biblioteca")

# Crear pestañas para alternar entre Librería y Socios
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# TODO: ARREGLAR ESTILOS
""" style = ttk.Style()
settings = {"TNotebook": 
                {
                    "configure": 
                        {
                            "padding": [10, 10],
                            "background": "#2c3e50"
                        }
                },
            "TNotebook.Tab": {"configure": {"padding": [10, 5],
                                            "background": "#3c6382",
                                            "foreground": "#ffffff"
                                           },
                              "map": {"background": [("selected", "#0a3d62"), 
                                                     ("active", "#0a3d62")],
                                      "foreground": [("selected", "#ffffff"),
                                                     ("active", "#ffffff")]
                                     }
                              }
           }  


style.theme_create("mi_estilo", parent="alt", settings=settings)
style.theme_use("mi_estilo") """
frame_libreria = tk.Frame(notebook, background="#5c6e78")
frame_socios = tk.Frame(notebook, background="#5c6e78")
frame_prestamo = tk.Frame(notebook, background="#5c6e78")
frame_reporte = tk.Frame(notebook, background="#5c6e78")

notebook.add(frame_libreria, text="Librería")
notebook.add(frame_socios, text="Socios")
notebook.add(frame_prestamo, text="Prestamo")
notebook.add(frame_reporte, text="Reporte")

# Inicializar las  interfaces
libreria_app = LibreriaApp(frame_libreria)
socio_app = SocioApp(frame_socios)
prestamo_app = PrestamoApp(frame_prestamo)
reporte_app = ReporteApp(frame_reporte)

root.mainloop()
