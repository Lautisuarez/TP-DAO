import tkinter as tk
from tkinter import ttk, messagebox
from Cruds.crudLibro import agregar_libro, obtener_libros, actualizar_libro, eliminar_libro
from Entidades.Libro import Libro

class LibreriaApp:
    def __init__(self, root):
        self.root = root
        self.libros = []

        for libro in obtener_libros():
            self.libros.append(libro)

        # TITULO
        self.tituloframe = tk.Frame(root)
        self.tituloframe.pack(pady=10)
        self.titulolibros_label = tk.LabelFrame(self.tituloframe, text="Agregar Libro")
        self.titulolibros_label.grid(row=0, column=0, pady=10, padx=10) 

        # FRAME INPUTS
        self.titulo_label = tk.Label(self.titulolibros_label, text="Título")
        self.titulo_entry = tk.Entry(self.titulolibros_label)

        self.precio_label = tk.Label(self.titulolibros_label, text="Precio")
        self.precio_entry = tk.Entry(self.titulolibros_label)

        # INPUTS
        self.titulo_label.grid(row=0, column=0, sticky="e")  # Alineado a la derecha
        self.titulo_entry.grid(row=0, column=1)

        self.precio_label.grid(row=1, column=0, sticky="e")  # Alineado a la derecha
        self.precio_entry.grid(row=1, column=1)

        # BOTONES
        self.botones_frame = tk.Frame(self.titulolibros_label)
        self.botones_frame.grid(row=2, column=0, columnspan=2, pady=10)

        self.agregar_button = tk.Button(self.botones_frame, text="Agregar", command=self.agregar_libro_BD)
        self.agregar_button.config(bg="lightblue")
        self.actualizar_button = tk.Button(self.botones_frame, text="Actualizar", command=self.actualizar_libro_BD)
        self.actualizar_button.config(bg="lightblue")
        self.eliminar_button = tk.Button(self.botones_frame, text="Eliminar", command=self.eliminar_libro)
        self.eliminar_button.config(bg="lightblue")

        self.agregar_button.grid(row=3, column=0, padx=5)
        self.actualizar_button.grid(row=3, column=1, padx=5)
        self.eliminar_button.grid(row=3, column=2, padx=5)

        # TITULO TABLA
        self.titulo_tabla_frame = tk.Frame(root)
        self.titulo_tabla_frame.pack()
        self.titulolibros_label = tk.Label(self.titulo_tabla_frame, text="LISTADO DE LIBROS", bg="#5c6e78", fg="white", font=("Helvetica", 12, "bold"))
        self.titulolibros_label.grid(row=0, column=0, sticky="e")  # Alineado a la derecha
        
        # FRAME TABLA
        self.cuadroframe = tk.Frame(root)
        self.cuadroframe.pack()
        
        # TABLA
        self.libros_tree = ttk.Treeview(self.cuadroframe, columns=("Código", "Título", "Precio", "Estado"), show="headings", height=15)
        self.libros_tree.column("Código", width=50, anchor=tk.CENTER)
        self.libros_tree.heading("Código", text="Código", anchor=tk.CENTER)
        self.libros_tree.column("Título", width=200, anchor=tk.CENTER)
        self.libros_tree.heading("Título", text="Título", anchor=tk.CENTER)
        self.libros_tree.column("Precio", width=200, anchor=tk.CENTER)
        self.libros_tree.heading("Precio", text="Precio", anchor=tk.CENTER)
        self.libros_tree.column("Estado", width=200, anchor=tk.CENTER)
        self.libros_tree.heading("Estado", text="Estado", anchor=tk.CENTER)

        
        self.libros_tree.pack()
        self.libros_tree.bind('<ButtonRelease-1>', self.cargar_datos_seleccionados) # EVENTO CLICK FILA
        
        # ACTUALIZAR TABLA
        self.actualizar_lista()

    def cargar_datos_seleccionados(self, event):
        seleccion = self.libros_tree.selection()
        if seleccion:
            # Obtener los valores actuales de la fila seleccionada
            valores_actuales = self.libros_tree.item(seleccion)['values']

            # Cargar los datos en los Entry
            self.titulo_entry.delete(0, tk.END)
            self.titulo_entry.insert(0, valores_actuales[1])
            self.precio_entry.delete(0, tk.END)
            self.precio_entry.insert(0, valores_actuales[2])

    def agregar_libro_BD(self):
        titulo = self.titulo_entry.get()
        precio = self.precio_entry.get()

        libro = Libro(self.obtenerProximoID() ,titulo, precio, "disponible")
        agregar_libro(libro)

        self.libros.append((libro._codigo, libro._titulo, libro._precio_reposicion, libro._estado))
        self.actualizar_lista()

    def actualizar_libro_BD(self):
        seleccion = self.libros_tree.selection()
        if seleccion:
            # Obtener los valores actuales de la fila seleccionada
            titulo = self.titulo_entry.get()
            precio = self.precio_entry.get()

            # Actualizar el libro seleccionado
            libro = Libro(self.libros_tree.item(seleccion)['values'][0], titulo, precio)
            self.libros_tree.item(seleccion, values=(libro.get_codigo(), libro.get_titulo(), libro.get_precio_reposicion(), libro.get_estado()))
            actualizar_libro(libro)

            messagebox.showinfo("Actualizado", f"El libro: '{libro.get_titulo()}' fue actualizado correctamente.")

            # Reseteamos valores
            self.limpiar_entradas()
            self.libros_tree.selection_remove(seleccion)
        else:
            messagebox.showerror("Error", "Debe seleccionar un libro para actualizarlo.")

    def eliminar_libro(self):
        seleccion = self.libros_tree.selection()
        if seleccion:
            libro_eliminado = self.libros_tree.item(seleccion)['values']
            self.libros_tree.delete(seleccion)
            eliminar_libro(libro_eliminado[0])
            messagebox.showinfo("Eliminado", f"El libro: '{libro_eliminado[1]}' fue eliminado correctamente.")
        else:
            messagebox.showerror("Error", "Debe seleccionar un libro para eliminarlo.")

    def actualizar_lista(self):
        self.libros_tree.delete(*self.libros_tree.get_children())
        for libro in self.libros:
            self.libros_tree.insert("", "end", values=libro)
        self.limpiar_entradas()

    def limpiar_entradas(self):
        self.titulo_entry.delete(0, "end")
        self.precio_entry.delete(0, "end")
    
    def obtenerProximoID(self):
        if(len(self.libros) == 0):
            return 1
        return int(self.libros[-1][0]) + 1

if __name__ == "__main__":
    root = tk.Tk()
    app = LibreriaApp(root)
    root.mainloop()