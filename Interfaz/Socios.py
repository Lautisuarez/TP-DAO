import tkinter as tk
from tkinter import ttk

class SocioApp:
    def __init__(self, root):
        self.root = root
        self.socios = []

        self.tituloframe = tk.Frame(root)
        self.tituloframe.pack()
        self.titulosocios_label = tk.Label(self.tituloframe, text="LISTADO DE SOCIOS")
        self.titulosocios_label.grid(row=0, column=0, sticky="e")  # Alineado a la derecha
        
        self.cuadroframe = tk.Frame(root)
        self.cuadroframe.pack()
        
        self.socios_tree = ttk.Treeview(self.cuadroframe, columns=("Nombre", "Libros Prestados"), show="headings")
        self.socios_tree.heading("Nombre", text="Nombre")
        self.socios_tree.heading("Libros Prestados", text="Libros Prestados")

        self.socios_tree.pack()
        
        # Crear un contenedor Frame
        self.frame = tk.Frame(root)
        self.frame.pack()
        
        self.nombre_label = tk.Label(self.frame, text="Nombre")
        self.nombre_entry = tk.Entry(self.frame)
        
        self.libros_prestados_label = tk.Label(self.frame, text="Libros Prestados")
        self.libros_prestados_entry = tk.Entry(self.frame)
        
        # Colocar los widgets usando grid
        self.nombre_label.grid(row=0, column=0, sticky="e")  # Alineado a la derecha
        self.nombre_entry.grid(row=0, column=1)

        self.libros_prestados_label.grid(row=1, column=0, sticky="e")  # Alineado a la derecha
        self.libros_prestados_entry.grid(row=1, column=1)

        # Crear un contenedor para los botones
        self.botones_frame = tk.Frame(root)
        self.botones_frame.pack(pady=10)
        
        self.prestar_button = tk.Button(self.botones_frame, text="Prestar Libro", command=self.prestar_libro)
        self.prestar_button.config(bg="lightblue")
        self.devolver_button = tk.Button(self.botones_frame, text="Devolver Libro", command=self.devolver_libro)
        self.devolver_button.config(bg="lightblue")
        
        self.prestar_button.grid(row=0, column=0, padx=5)
        self.devolver_button.grid(row=0, column=1, padx=5)

        

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
