import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")  # Título de la ventana principal

        # Crear Frames para organizar la interfaz
        self.frame_entrada = tk.Frame(self.root)
        self.frame_entrada.pack(pady=10)

        self.frame_lista = tk.Frame(self.root)
        self.frame_lista.pack(pady=10)

        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack(pady=10)

        # Etiquetas y Entradas para introducción de datos
        self.label_fecha = tk.Label(self.frame_entrada, text="Fecha (DD-MM-AAAA):")
        self.label_fecha.grid(row=0, column=0)

        # Selector de fecha (DateEntry)
        self.fecha_entry = DateEntry(self.frame_entrada, width=12, background='darkblue', foreground='white',
                                     borderwidth=2)
        self.fecha_entry.grid(row=0, column=1)

        self.label_hora = tk.Label(self.frame_entrada, text="Hora (HH:MM):")
        self.label_hora.grid(row=0, column=2)

        # Campo de entrada para la hora
        self.hora_entry = tk.Entry(self.frame_entrada, width=10)
        self.hora_entry.grid(row=0, column=3)

        self.label_desc = tk.Label(self.frame_entrada, text="Descripción:")
        self.label_desc.grid(row=0, column=4)

        # Campo de entrada para la descripción
        self.desc_entry = tk.Entry(self.frame_entrada, width=25)
        self.desc_entry.grid(row=0, column=5)

        # Treeview para listar eventos
        self.lista_eventos = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.lista_eventos.heading("Fecha", text="Fecha")  # Encabezado de la columna de fecha
        self.lista_eventos.heading("Hora", text="Hora")  # Encabezado de la columna de hora
        self.lista_eventos.heading("Descripción", text="Descripción")  # Encabezado de la columna de descripción
        self.lista_eventos.pack()

        # Botones para acciones
        self.boton_agregar = tk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento)
        self.boton_agregar.grid(row=0, column=0)

        self.boton_eliminar = tk.Button(self.frame_botones, text="Eliminar Evento Seleccionado",
                                        command=self.eliminar_evento)
        self.boton_eliminar.grid(row=0, column=1)

        self.boton_salir = tk.Button(self.frame_botones, text="Salir", command=self.root.quit)
        self.boton_salir.grid(row=0, column=2)

    def agregar_evento(self):
        """ Agrega un evento a la lista de eventos. """
        fecha = self.fecha_entry.get()  # Obtiene la fecha del selector
        hora = self.hora_entry.get()  # Obtiene la hora del campo de entrada
        descripcion = self.desc_entry.get()  # Obtiene la descripción del campo de entrada

        # Verificar que todos los campos están completos
        if not all([fecha, hora, descripcion]):
            messagebox.showwarning("Error", "Todos los campos deben ser completados.")  # Mensaje de advertencia
            return

            # Insertar el evento en el Treeview
        self.lista_eventos.insert("", "end", values=(fecha, hora, descripcion))

        # Limpiar campos de entrada tras agregar el evento
        self.fecha_entry.delete(0, tk.END)
        self.hora_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def eliminar_evento(self):
        """ Elimina el evento seleccionado de la lista. """
        seleccionado = self.lista_eventos.selection()  # Obtiene el evento seleccionado
        if not seleccionado:
            messagebox.showwarning("Error", "No se ha seleccionado ningún evento.")  # Mensaje si no hay selección
            return

            # Solicitar confirmación antes de eliminar
        confirmacion = messagebox.askyesno("Confirmar Eliminación", "¿Está seguro de que desea eliminar este evento?")
        if confirmacion:
            for item in seleccionado:
                self.lista_eventos.delete(item)  # Eliminar el evento de la lista


if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal
    app = AgendaApp(root)  # Instanciar la aplicación
    root.mainloop()  # Iniciar el bucle principal de la aplicación