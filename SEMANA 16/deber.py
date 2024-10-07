import tkinter as tk
from tkinter import messagebox, Listbox, END, SINGLE

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas Pendientes")

        self.tasks = []  # Lista para almacenar las tareas

        # Campo de entrada
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        # Botón para añadir tarea
        self.add_task_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Listbox para mostrar tareas
        self.task_listbox = Listbox(root, width=50, height=15, selectmode=SINGLE)
        self.task_listbox.pack(pady=10)

        # Botón para marcar tarea como completada
        self.complete_task_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        # Botón para eliminar tarea
        self.delete_task_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        # Atajos de teclado
        self.root.bind("<Return>", lambda event: self.add_task())  # Enter
        self.root.bind("<c>", lambda event: self.complete_task())  # C
        self.root.bind("<Delete>", lambda event: self.delete_task())  # Delete
        self.root.bind("<Escape>", lambda event: self.root.quit())  # Escape

    def add_task(self):
        task = self.task_entry.get()
        if task:  # Comprobar si el campo no está vacío
            self.tasks.append(task)
            self.update_task_list()  # Actualizar la lista de tareas
            self.task_entry.delete(0, END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Debes escribir una tarea.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]  # Obtener índice de la tarea seleccionada
            completed_task = self.tasks[selected_index] + " (Completada)"
            self.tasks[selected_index] = completed_task  # Marcar tarea como completada
            self.update_task_list()  # Actualizar la lista de tareas
        except IndexError:
            messagebox.showwarning("Advertencia", "Debes seleccionar una tarea.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]  # Obtener índice de la tarea seleccionada
            del self.tasks[selected_index]  # Eliminar tarea
            self.update_task_list()  # Actualizar la lista de tareas
        except IndexError:
            messagebox.showwarning("Advertencia", "Debes seleccionar una tarea para eliminar.")

    def update_task_list(self):
        self.task_listbox.delete(0, END)  # Limpiar el Listbox
        for task in self.tasks:  # Añadir todas las tareas de la lista
            self.task_listbox.insert(END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()