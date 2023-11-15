import tkinter as tk
from tkinter import ttk

from Cruds.crudSocio import obtener_socios

class SocioApp:
    def __init__(self, root):
        self.root = root
        self.socios = []

        for socio in obtener_socios():
            self.socios.append(socio)
            
        # TITULO
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)
        self.titulosocios_label = tk.LabelFrame(self.frame, text="Agregar Socio")
        self.titulosocios_label.grid(row=0, column=0, pady=10, padx=10)
        
        # FRAME INPUTS
        self.DNI_label = tk.Label(self.titulosocios_label, text="DNI")
        self.DNI_entry = tk.Entry(self.titulosocios_label)
        
        self.nombre_label = tk.Label(self.titulosocios_label, text="Nombre")
        self.nombre_entry = tk.Entry(self.titulosocios_label)
        
        self.apellido_label = tk.Label(self.titulosocios_label, text="Apellido")
        self.apellido_entry = tk.Entry(self.titulosocios_label)
        
        # INPUTS
        self.DNI_label.grid(row=1, column=0, sticky="e")  # Alineado a la derecha
        self.DNI_label.grid(row=1, column=1, padx=10)
        
        self.nombre_label.grid(row=0, column=0, sticky="e")  # Alineado a la derecha
        self.nombre_entry.grid(row=0, column=1, padx=10)

        self.apellido_label.grid(row=1, column=0, sticky="e")  # Alineado a la derecha
        self.apellido_label.grid(row=1, column=1, padx=10)

        # BOTONES
        self.botones_frame = tk.Frame(self.titulosocios_label)
        self.botones_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.prestar_button = tk.Button(self.botones_frame, text="Prestar Libro", command=self.prestar_libro)
        self.prestar_button.config(bg="lightblue")
        self.devolver_button = tk.Button(self.botones_frame, text="Devolver Libro", command=self.devolver_libro)
        self.devolver_button.config(bg="lightblue")
        
        self.prestar_button.grid(row=3, column=0, padx=5)
        self.devolver_button.grid(row=3, column=1, padx=5)

        # TITULO TABLA
        self.tituloframe = tk.Frame(root)
        self.tituloframe.pack()
        self.titulosocios_label = tk.Label(self.tituloframe, text="LISTADO DE SOCIOS", bg="#5c6e78", fg="white", font=("Helvetica", 12, "bold"))
        self.titulosocios_label.grid(row=0, column=0, sticky="e")  # Alineado a la derecha
        
        # FRAME TABLA
        self.cuadroframe = tk.Frame(root)
        self.cuadroframe.pack()
        
        # TABLA
        self.socios_tree = ttk.Treeview(self.cuadroframe, columns=("DNI", "Nombre", "Apellido"), show="headings", height=15)
        self.socios_tree.column("DNI", width=200, anchor=tk.CENTER)
        self.socios_tree.heading("DNI", text="DNI", anchor=tk.CENTER)
        self.socios_tree.column("Nombre", width=200, anchor=tk.CENTER)
        self.socios_tree.heading("Nombre", text="Nombre", anchor=tk.CENTER)
        self.socios_tree.column("Apellido", width=200, anchor=tk.CENTER)
        self.socios_tree.heading("Apellido", text="Apellido", anchor=tk.CENTER)

        self.socios_tree.pack()
        self.socios_tree.bind('<ButtonRelease-1>', self.cargar_datos_seleccionados) 

    def cargar_datos_seleccionados(self, event):
        seleccion = self.socios_tree.selection()

    def prestar_libro(self):
        nombre = self.nombre_entry.get()
        libros_prestados = self.libros_prestados_entry.get()

        if nombre and libros_prestados:
            libros_prestados = libros_prestados.split(',')
            socio = (nombre, libros_prestados)
            self.socios.append(socio)
            self.actualizar_lista_socios()
            for libro in libros_prestados:
                self.libros_app.prestar_libro_a_socio(nombre, libro)

    def devolver_libro(self):
        seleccion = self.socios_tree.selection()
        if seleccion:
            nombre = self.nombre_entry.get()
            libro = self.libros_prestados_entry.get()
            socio = self.socios_tree.item(seleccion[0])['values']

            if nombre and libro:
                if socio[0] == nombre and libro in socio[1]:
                    socio[1].remove(libro)
                    self.libros_app.devolver_libro_de_socio(nombre, libro)
                    self.actualizar_lista_socios()

    def actualizar_lista_socios(self):
        self.socios_tree.delete(*self.socios_tree.get_children())
        for socio in self.socios:
            self.socios_tree.insert("", "end", values=socio)
        self.limpiar_entradas()

    def limpiar_entradas(self):
        self.nombre_entry.delete(0, "end")
        self.libros_prestados_entry.delete(0, "end")

if __name__ == "__main__":
    root = tk.Tk()
    socios_app = SocioApp(root)
    root.mainloop()
