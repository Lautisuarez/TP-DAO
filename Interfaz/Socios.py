import tkinter as tk
from tkinter import ttk

class SocioApp:
    def __init__(self, root):
        self.root = root
        self.socios = []

        self.nombre_label = tk.Label(root, text="Nombre")
        self.libros_prestados_label = tk.Label(root, text="Libros Prestados")

        self.nombre_entry = tk.Entry(root)
        self.libros_prestados_entry = tk.Entry(root)

        self.prestar_button = tk.Button(root, text="Prestar Libro", command=self.prestar_libro)
        self.devolver_button = tk.Button(root, text="Devolver Libro", command=self.devolver_libro)

        self.socios_tree = ttk.Treeview(root, columns=("Nombre", "Libros Prestados"), show="headings")
        self.socios_tree.heading("Nombre", text="Nombre")
        self.socios_tree.heading("Libros Prestados", text="Libros Prestados")

        self.nombre_label.pack()
        self.nombre_entry.pack()
        self.libros_prestados_label.pack()
        self.libros_prestados_entry.pack()
        self.prestar_button.pack()
        self.devolver_button.pack()
        self.socios_tree.pack()

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
    socios_app = SocioApp(root, libros_app)
    root.mainloop()
