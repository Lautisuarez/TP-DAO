import tkinter as tk
from tkinter import ttk
from Cruds.crudLibro import agregar_libro, obtener_libros, actualizar_libro, eliminar_libro
from Entidades.Libro import Libro

class LibreriaApp:
    def __init__(self, root):
        self.root = root
        self.libros = []
        for libro in obtener_libros():
            self.libros.append(libro[1:])
        
        self.titulo_label = tk.Label(root, text="Título")
        self.precio_label = tk.Label(root, text="Precio")
        self.estado_label = tk.Label(root, text="Estado")

        self.titulo_entry = tk.Entry(root)
        self.precio_entry = tk.Entry(root)
        self.estado_entry = tk.Entry(root)

        self.agregar_button = tk.Button(root, text="Agregar", command=self.agregar_libro)
        self.agregar_button.config(bg="lightblue")
        self.actualizar_button = tk.Button(root, text="Actualizar", command=self.actualizar_libro)
        self.actualizar_button.config(bg="lightblue")
        self.eliminar_button = tk.Button(root, text="Eliminar", command=self.eliminar_libro)
        self.eliminar_button.config(bg="lightblue")

        self.libros_tree = ttk.Treeview(root, columns=("Título", "Precio", "Estado"), show="headings")
        self.libros_tree.heading("Título", text="Título")
        self.libros_tree.heading("Precio", text="Precio")
        self.libros_tree.heading("Estado", text="Estado")
        
        self.titulo_label.pack()
        self.titulo_entry.pack()
        self.precio_label.pack()
        self.precio_entry.pack()
        self.estado_label.pack()
        self.estado_entry.pack()
        self.agregar_button.pack()
        self.actualizar_button.pack()
        self.eliminar_button.pack()
        self.libros_tree.pack()
        self.actualizar_lista()

    def agregar_libro(self):
        titulo = self.titulo_entry.get()
        precio = self.precio_entry.get()
        estado = self.estado_entry.get()
        libro = Libro(2, titulo, precio, estado)
        agregar_libro(libro)

        self.libros.append((titulo, precio, estado))
        self.actualizar_lista()

    def actualizar_libro(self):
        seleccion = self.libros_tree.selection()
        if seleccion:
            titulo = self.titulo_entry.get()
            precio = self.precio_entry.get()
            estado = self.estado_entry.get()

            libro = self.libros_tree.item(seleccion[0])['values']
            indice = self.libros.index(tuple(libro))

            self.libros[indice] = (titulo, precio, estado)
            self.actualizar_lista()

    def eliminar_libro(self):
        seleccion = self.libros_tree.selection()
        if seleccion:
            libro = self.libros_tree.item(seleccion[0])['values']
            self.libros.remove(tuple(libro))
            self.actualizar_lista()

    def actualizar_lista(self):
        self.libros_tree.delete(*self.libros_tree.get_children())
        for libro in self.libros:
            self.libros_tree.insert("", "end", values=libro)
        self.limpiar_entradas()

    def limpiar_entradas(self):
        self.titulo_entry.delete(0, "end")
        self.precio_entry.delete(0, "end")
        self.estado_entry.delete(0, "end")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibreriaApp(root)
    root.mainloop()