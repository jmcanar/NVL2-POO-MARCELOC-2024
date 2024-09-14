import tkinter as tk
from tkinter import messagebox


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Gestión de Información")  # Título de la ventana principal

        # Etiqueta para indicar al usuario que ingrese información
        self.label = tk.Label(root, text="Ingrese información:")
        self.label.pack(pady=10)  # Espaciado vertical

        # Campo de texto donde el usuario puede ingresar información
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)  # Espaciado vertical

        # Botón "Agregar" que llama a la función add_info al ser presionado
        self.add_button = tk.Button(root, text="Agregar", command=self.add_info)
        self.add_button.pack(pady=5)  # Espaciado vertical

        # Lista para mostrar los datos ingresados por el usuario
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)  # Espaciado vertical

        # Botón "Limpiar" que llama a la función clear_info al ser presionado
        self.clear_button = tk.Button(root, text="Limpiar", command=self.clear_info)
        self.clear_button.pack(pady=5)  # Espaciado vertical

    def add_info(self):
        # Obtener el texto ingresado en el campo de texto
        info = self.entry.get()
        if info:
            # Agregar la información a la lista
            self.listbox.insert(tk.END, info)
            self.entry.delete(0, tk.END)  # Limpiar el campo de texto
        else:
            # Mostrar advertencia si el campo de texto está vacío
            messagebox.showwarning("Advertencia", "Por favor, ingrese información.")

    def clear_info(self):
        # Limpiar el campo de texto y la lista
        self.entry.delete(0, tk.END)
        self.listbox.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal
    app = App(root)  # Instanciar la aplicación
    root.mainloop()  # Iniciar el bucle principal de la aplicación
