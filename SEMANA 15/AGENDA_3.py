import tkinter as tk
from tkinter import ttk


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Crear y configurar widgets
        # Campo de entrada para nuevas tareas
        self.task_input = ttk.Entry(root, width=40)
        # Botón para añadir nuevas tareas
        self.add_button = ttk.Button(root, text="Añadir Tarea", command=self.add_task)
        # Lista para mostrar las tareas
        self.listbox = tk.Listbox(root, width=50, height=10)
        # Botón para marcar/desmarcar tareas como completadas
        self.complete_button = ttk.Button(root, text="Marcar/Desmarcar Completada", command=self.toggle_complete_task)
        # Botón para eliminar tareas
        self.delete_button = ttk.Button(root, text="Eliminar Tarea", command=self.delete_task)

        # Posicionar widgets en la ventana usando el sistema de grid
        self.task_input.grid(row=0, column=0, padx=5, pady=5)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)
        self.listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.complete_button.grid(row=2, column=0, padx=5, pady=5)
        self.delete_button.grid(row=2, column=1, padx=5, pady=5)

        # Vincular eventos a acciones
        # Presionar Enter en el campo de entrada añade la tarea
        self.task_input.bind('<Return>', lambda event: self.add_task())
        # Doble clic en una tarea la marca/desmarca como completada
        self.listbox.bind('<Double-1>', lambda event: self.toggle_complete_task())
        # Presionar Escape cierra la aplicación
        self.root.bind('<Escape>', lambda event: self.root.quit())

    def add_task(self):
        """Añade una nueva tarea a la lista."""
        task = self.task_input.get()
        if task:
            # Insertar la nueva tarea al final de la lista
            self.listbox.insert(tk.END, task)
            # Configurar el color de fondo de la nueva tarea a blanco
            self.listbox.itemconfig(tk.END, {'bg': 'white'})
            # Limpiar el campo de entrada
            self.task_input.delete(0, tk.END)

    def toggle_complete_task(self):
        """Alterna el estado de completado de una tarea seleccionada."""
        try:
            # Obtener el índice de la tarea seleccionada
            index = self.listbox.curselection()[0]
            # Obtener el color de fondo actual de la tarea
            current_color = self.listbox.itemcget(index, 'bg')
            if current_color == 'white':
                # Si la tarea no está completada, marcarla como completada (verde claro)
                self.listbox.itemconfig(index, {'bg': 'light green'})
            else:
                # Si la tarea está completada, desmarcarla (blanco)
                self.listbox.itemconfig(index, {'bg': 'white'})
        except IndexError:
            # No hacer nada si no hay tarea seleccionada
            pass

    def delete_task(self):
        """Elimina la tarea seleccionada de la lista."""
        try:
            # Obtener el índice de la tarea seleccionada
            index = self.listbox.curselection()[0]
            # Eliminar la tarea de la lista
            self.listbox.delete(index)
        except IndexError:
            # No hacer nada si no hay tarea seleccionada
            pass


if __name__ == "__main__":
    # Crear la ventana principal
    root = tk.Tk()
    # Inicializar la aplicación
    app = ToDoApp(root)
    # Iniciar el loop principal de la aplicación
    root.mainloop()