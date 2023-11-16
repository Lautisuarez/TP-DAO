import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from Cruds.crudSocio import *
from Entidades.Socio import Socio

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
        self.DNI_entry.grid(row=1, column=1, padx=10)
        
        self.nombre_label.grid(row=2, column=0, sticky="e")  # Alineado a la derecha
        self.nombre_entry.grid(row=2, column=1, padx=10)

        self.apellido_label.grid(row=3, column=0, sticky="e")  # Alineado a la derecha
        self.apellido_entry.grid(row=3, column=1, padx=10)

        # BOTONES
        self.botones_frame = tk.Frame(self.titulosocios_label)
        self.botones_frame.grid(row=4, column=0, columnspan=2, pady=10)
        
        self.agregar_button = tk.Button(self.botones_frame, text="Agregar", command=self.agregar_socio)
        self.agregar_button.config(bg="lightblue")
        self.editar_button = tk.Button(self.botones_frame, text="Editar", command=self.editar_socio)
        self.editar_button.config(bg="lightblue")
        self.eliminar_button = tk.Button(self.botones_frame, text="Eliminar", command=self.eliminar_socio)
        self.eliminar_button.config(bg="lightblue")
        self.limpiar_button = tk.Button(self.botones_frame, text="Limpiar", command=self.limpiar)
        self.limpiar_button.config(bg="lightblue")
        
        self.agregar_button.grid(row=3, column=0, padx=5)
        self.editar_button.grid(row=3, column=1, padx=5)
        self.eliminar_button.grid(row=3, column=2, padx=5)
        self.limpiar_button.grid(row=3, column=2, padx=5)

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

        self.actualizar_lista_socios()

    def cargar_datos_seleccionados(self, event):
        seleccion = self.socios_tree.selection()
        if seleccion:
            
            # Obtener los valores actuales de la fila seleccionada
            valores_actuales = self.socios_tree.item(seleccion)['values']
            self.DNI_entry.config(state="normal")
            # Cargar los datos en los Entry
            self.DNI_entry.delete(0, tk.END)
            self.DNI_entry.insert(0, valores_actuales[0])
            self.nombre_entry.delete(0, tk.END)
            self.nombre_entry.insert(0, valores_actuales[1])
            self.apellido_entry.delete(0, tk.END)
            self.apellido_entry.insert(0, valores_actuales[2])
            self.DNI_entry.config(state="readonly")

    def agregar_socio(self):
        dni = self.DNI_entry.get()
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()

        socio = Socio(dni, nombre, apellido)
        agregar_socio(socio)

        self.socios.append((socio.get_dni(), socio.get_nombre(), socio.get_apellido()))
        self.actualizar_lista_socios()

    def editar_socio(self):
        seleccion = self.socios_tree.selection()
        if seleccion:
            
            # Obtener los valores actuales de la fila seleccionada
            nombre = self.nombre_entry.get()
            apellido = self.apellido_entry.get()

            # Actualizar el libro seleccionado
            socio = Socio(self.socios_tree.item(seleccion)['values'][0], nombre, apellido)
            self.socios_tree.item(seleccion, values=(socio.get_dni(), socio.get_nombre(), socio.get_apellido()))
            actualizar_socio(socio)

            messagebox.showinfo("Actualizado", f"El Socio: '{socio.get_nombre()}' fue actualizado correctamente.")

            # Reseteamos valores
            self.limpiar_entradas()
            self.socios_tree.selection_remove(seleccion)
                
        else:
            messagebox.showerror("Error", "Debe seleccionar un socio para actualizarlo.")

    def eliminar_socio(self):
        seleccion = self.socios_tree.selection()
        if seleccion:
            socio_eliminado = self.socios_tree.item(seleccion)['values']
            self.socios_tree.delete(seleccion)
            eliminar_socio(socio_eliminado[0])
            messagebox.showinfo("Eliminado", f"El socio: '{socio_eliminado[1]}' fue eliminado correctamente.")
        else:
            messagebox.showerror("Error", "Debe seleccionar un socio para eliminarlo.")

    def actualizar_lista_socios(self):
        self.socios_tree.delete(*self.socios_tree.get_children())
        for socio in self.socios:
            self.socios_tree.insert("", "end", values=socio)
        self.limpiar_entradas()

    def limpiar(self):
        self.limpiar_entradas()
    
    def limpiar_entradas(self):
        self.DNI_entry.config(state="normal")
        self.nombre_entry.delete(0, "end")
        self.DNI_entry.delete(0, "end")
        self.apellido_entry.delete(0, "end")

if __name__ == "__main__":
    root = tk.Tk()
    socios_app = SocioApp(root)
    root.mainloop()
