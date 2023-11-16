import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from Reporte.doc_reporte import generar_reporte

class ReporteApp:
    def __init__(self, root):
        self.root = root
        
        # TITULO
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)
        self.tituloprestamo_label = tk.LabelFrame(self.frame, text="Reporte de prestamos")
        self.tituloprestamo_label.grid(row=0, column=0, pady=10, padx=10)

        # FRAME INPUTS
        self.DNI_label = tk.Label(self.tituloprestamo_label, text="DNI Socio")
        self.DNI_entry = tk.Entry(self.tituloprestamo_label)

        self.titulo_label = tk.Label(self.tituloprestamo_label, text="Titulo Libro")
        self.titulo_entry = tk.Entry(self.tituloprestamo_label)

        # INPUTS
        self.DNI_label.grid(row=1, column=0, sticky="e")
        self.DNI_entry.grid(row=1, column=1, padx=10)

        self.titulo_label.grid(row=2, column=0, sticky="e")
        self.titulo_entry.grid(row=2, column=1, padx=10)

        # BOTONES
        self.botones_frame = tk.Frame(self.tituloprestamo_label)
        self.botones_frame.grid(row=4, column=0, columnspan=2, pady=10)

        self.generar_button = tk.Button(self.botones_frame, text="Generar Reporte", command=self.generarReporte)
        self.generar_button.config(bg="lightblue")
        self.limpiar_button = tk.Button(self.botones_frame, text="Limpiar", command=self.limpiar)
        self.limpiar_button.config(bg="lightblue")

        self.generar_button.grid(row=3, column=0, padx=5)
        self.limpiar_button.grid(row=3, column=1, padx=5)
        
    def generarReporte(self):
        titulo = self.titulo_entry.get()
        dni = self.DNI_entry.get()
        generar_reporte(titulo, dni)
        self.limpiar()
        messagebox.showinfo(message="Reporte generado con éxito con el nombre: report.pdf", title="Reporte")
        
    def limpiar(self):
        self.titulo_entry.delete(0, tk.END)
        self.DNI_entry.delete(0, tk.END)
        
if __name__ == "__main__":
    root = tk.Tk()
    reporte_app = ReporteApp(root)
    root.mainloop()