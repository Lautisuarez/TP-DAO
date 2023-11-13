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
    
        self.tituloframe = tk.Frame(root)
        self.tituloframe.pack()
        self.titulolibros_label = tk.Label(self.tituloframe, text="LISTADO DE LIBROS")
        self.titulolibros_label.grid(row=0, column=0, sticky="e")  # Alineado a la derecha
        
        self.cuadroframe = tk.Frame(root)
        self.cuadroframe.pack()
        
        self.libros_tree = ttk.Treeview(self.cuadroframe, columns=("Título", "Precio", "Estado"), show="headings")
        self.libros_tree.heading("Título", text="Título")
        self.libros_tree.heading("Precio", text="Precio")
        self.libros_tree.heading("Estado", text="Estado")
        
        self.libros_tree.pack()
        
        # Crear un contenedor Frame
        self.frame = tk.Frame(root)
        self.frame.pack()

        # Crear y colocar los widgets en el Frame
        self.titulo_label = tk.Label(self.frame, text="Título")
        self.titulo_entry = tk.Entry(self.frame)

        self.precio_label = tk.Label(self.frame, text="Precio")
        self.precio_entry = tk.Entry(self.frame)

        # Colocar los widgets usando grid
        self.titulo_label.grid(row=0, column=0, sticky="e")  # Alineado a la derecha
        self.titulo_entry.grid(row=0, column=1)

        self.precio_label.grid(row=1, column=0, sticky="e")  # Alineado a la derecha
        self.precio_entry.grid(row=1, column=1)

        # Crear un contenedor para los botones
        self.botones_frame = tk.Frame(root)
        self.botones_frame.pack(pady=10)
        
        self.agregar_button = tk.Button(self.botones_frame, text="Agregar", command=self.agregar_libro)
        self.agregar_button.config(bg="lightblue")
        self.actualizar_button = tk.Button(self.botones_frame, text="Actualizar", command=self.actualizar_libro)
        self.actualizar_button.config(bg="lightblue")
        self.eliminar_button = tk.Button(self.botones_frame, text="Eliminar", command=self.eliminar_libro)
        self.eliminar_button.config(bg="lightblue")

        self.agregar_button.grid(row=0, column=0, padx=5)
        self.actualizar_button.grid(row=0, column=1, padx=5)
        self.eliminar_button.grid(row=0, column=2, padx=5)

        self.actualizar_lista()
    def agregar_libro(self):
        titulo = self.titulo_entry.get()
        precio = self.precio_entry.get()

        libro = Libro(2,titulo, precio)
        agregar_libro(libro)
        print(libro._titulo, libro._precio_reposicion, libro._estado)

        self.libros.append((libro._titulo, libro._precio_reposicion, libro._estado))
        self.actualizar_lista()

    def actualizar_libro(self):
        seleccion = self.libros_tree.selection()
        if seleccion:
            titulo = self.titulo_entry.get()
            precio = self.precio_entry.get()

            libro = self.libros_tree.item(seleccion[0])['values']
            indice = self.libros.index(tuple(libro))

            self.libros[indice] = (titulo, precio)
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

if __name__ == "__main__":
    root = tk.Tk()
    app = LibreriaApp(root)
    root.mainloop()