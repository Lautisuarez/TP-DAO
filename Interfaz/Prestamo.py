import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from Entidades.Negocio import devolver_libro, prestar_libro, obtener_prestamos

class PrestamoApp:
    def __init__(self, root):
        self.root = root
        self.prestamos = []

        for prestamo in obtener_prestamos():
            self.prestamos.append(prestamo)

        # TITULO
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)
        self.tituloprestamo_label = tk.LabelFrame(self.frame, text="Manejo de prestamos")
        self.tituloprestamo_label.grid(row=0, column=0, pady=10, padx=10)

        # FRAME INPUTS
        self.DNI_label = tk.Label(self.tituloprestamo_label, text="DNI Socio")
        self.DNI_entry = tk.Entry(self.tituloprestamo_label)

        self.codigo_label = tk.Label(self.tituloprestamo_label, text="Código Libro")
        self.codigo_entry = tk.Entry(self.tituloprestamo_label)

        self.dias_label = tk.Label(self.tituloprestamo_label, text="Días pactados")
        self.dias_entry = tk.Entry(self.tituloprestamo_label)

        # INPUTS
        self.DNI_label.grid(row=1, column=0, sticky="e")
        self.DNI_entry.grid(row=1, column=1, padx=10)

        self.codigo_label.grid(row=2, column=0, sticky="e")
        self.codigo_entry.grid(row=2, column=1, padx=10)

        self.dias_label.grid(row=3, column=0, sticky="e")
        self.dias_entry.grid(row=3, column=1, padx=10)

        # BOTONES
        self.botones_frame = tk.Frame(self.tituloprestamo_label)
        self.botones_frame.grid(row=4, column=0, columnspan=2, pady=10)

        self.prestar_button = tk.Button(self.botones_frame, text="Prestar", command=self.prestar_libro)
        self.prestar_button.config(bg="lightblue")
        self.devolver_button = tk.Button(self.botones_frame, text="Devolver", command=self.devolver_libro)
        self.devolver_button.config(bg="lightblue")
        self.limpiar_button = tk.Button(self.botones_frame, text="Limpiar", command=self.limpiar)
        self.limpiar_button.config(bg="lightblue")

        self.prestar_button.grid(row=3, column=0, padx=5)
        self.devolver_button.grid(row=3, column=1, padx=5)
        self.limpiar_button.grid(row=3, column=2, padx=5)

        # TITULO TABLA  
        self.tituloframe = tk.Frame(root)
        self.tituloframe.pack()
        self.tituloprestamo_label = tk.Label(self.tituloframe, text="LISTADO DE PRESTAMOS", bg="#5c6e78", fg="white", font=("Helvetica", 12, "bold"))
        self.tituloprestamo_label.grid(row=0, column=0, sticky="e")

        # TABLA
        self.tabla_frame = tk.Frame(root)
        self.tabla_frame.pack()

        self.prestamo_tree = ttk.Treeview(self.tabla_frame, columns=("ID", "DNI", "Código", "Fecha de préstamo", "Días pactados", "Fecha de devolución", "Demora"), show="headings", height=15)
        self.prestamo_tree.heading("ID", text="ID", anchor=tk.CENTER)
        self.prestamo_tree.heading("DNI", text="DNI", anchor=tk.CENTER)
        self.prestamo_tree.heading("Código", text="Código", anchor=tk.CENTER)
        self.prestamo_tree.heading("Fecha de préstamo", text="Fecha de préstamo", anchor=tk.CENTER)
        self.prestamo_tree.heading("Fecha de devolución", text="Fecha de devolución", anchor=tk.CENTER)
        self.prestamo_tree.heading("Días pactados", text="Días pactados", anchor=tk.CENTER)
        self.prestamo_tree.heading("Demora", text="Demora", anchor=tk.CENTER)
        self.prestamo_tree.column("ID", width=50, anchor=tk.CENTER)
        self.prestamo_tree.column("DNI", width=100, anchor=tk.CENTER)
        self.prestamo_tree.column("Código", width=50, anchor=tk.CENTER)
        self.prestamo_tree.column("Fecha de préstamo", width=150, anchor=tk.CENTER)
        self.prestamo_tree.column("Fecha de devolución", width=150, anchor=tk.CENTER)
        self.prestamo_tree.column("Días pactados", width=100, anchor=tk.CENTER)
        self.prestamo_tree.column("Demora", width=100, anchor=tk.CENTER)

        self.prestamo_tree.pack()
        self.prestamo_tree.bind("<ButtonRelease-1>", self.cargar_datos_seleccionados)

        self.actualizar_lista_prestamos()

    def cargar_datos_seleccionados(self, event):
        seleccion = self.prestamo_tree.selection()
        if seleccion:
            self.DNI_entry.config(state="normal")
            self.dias_entry.config(state="normal")
            valores_actuales = self.prestamo_tree.item(seleccion)['values']

            self.codigo_entry.delete(0, tk.END)
            self.codigo_entry.insert(0, valores_actuales[1])
            self.DNI_entry.delete(0, tk.END)
            self.DNI_entry.insert(0, valores_actuales[2])
            self.dias_entry.delete(0, tk.END)
            self.dias_entry.insert(0, valores_actuales[4])
            self.DNI_entry.config(state="readonly")
            self.dias_entry.config(state="readonly")

    def prestar_libro(self):
        dni = self.DNI_entry.get()
        codigo = self.codigo_entry.get()
        dias = self.dias_entry.get()

        prestamo = prestar_libro(codigo, dni, dias)
        print(prestamo)
        self.prestamos.append((prestamo.get_id(), prestamo.get_dni_socio(), prestamo.get_codigo_libro(), prestamo.get_fecha_prestamo(), prestamo.get_dias_pactados(), prestamo.get_fecha_devolucion(), prestamo.get_demora()))
        self.actualizar_lista_prestamos()
        

    def devolver_libro(self):
        
        seleccion = self.prestamo_tree.selection()
        if seleccion:
            # Actualizar el prestamo
            codigo = self.codigo_entry.get()
            prestamo = devolver_libro(codigo)
            self.prestamos.append((prestamo.get_id(), prestamo.get_dni_socio(), prestamo.get_codigo_libro(), prestamo.get_fecha_prestamo(), prestamo.get_dias_pactados(), prestamo.get_fecha_devolucion(), prestamo.get_demora()))
            self.actualizar_lista_prestamos()

            messagebox.showinfo("Actualizado", f"El Prestamo: '{codigo}' fue actualizado correctamente.")

            # Reseteamos valores
            self.limpiar()
            self.prestamo_tree.selection_remove(seleccion)
                
        else:
            messagebox.showerror("Error", "Debe seleccionar un prestamo para actualizarlo.")

    def actualizar_lista_prestamos(self):
        self.prestamo_tree.delete(*self.prestamo_tree.get_children())
        for prestamo in self.prestamos:
            self.prestamo_tree.insert("", "end", values=prestamo)
        self.limpiar_entradas()

    def limpiar_entradas(self):
        self.DNI_entry.delete(0, "end")
        self.codigo_entry.delete(0, "end")
        self.dias_entry.delete(0, "end")
        
        
    def limpiar(self):
        self.DNI_entry.config(state="normal")
        self.dias_entry.config(state="normal")
        self.limpiar_entradas()
        

if __name__ == "__main__":
    root = tk.Tk()
    prestamo_app = PrestamoApp(root)
    root.mainloop()