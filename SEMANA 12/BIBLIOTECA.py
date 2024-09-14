import json


class Libro:
    def __init__(self, isbn, titulo, autor, categoria, prestado=False):
        # Inicializa un libro con sus atributos
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.prestado = prestado

    def to_dict(self):
        # Convierte el objeto Libro a un diccionario para facilitar la serialización
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria,
            "prestado": self.prestado
        }


class Biblioteca:
    def __init__(self, archivo_json='biblioteca.json'):
        # Inicializa la biblioteca y carga los libros desde un archivo JSON
        self.archivo_json = archivo_json
        self.libros = self.cargar_libros()

    def cargar_libros(self):
        # Carga los libros desde el archivo JSON
        try:
            with open(self.archivo_json, 'r') as archivo:
                datos_libros = json.load(archivo)
                return {isbn: Libro(**datos) for isbn, datos in datos_libros.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            # Retorna un diccionario vacío si el archivo no existe o está vacío
            return {}

    def guardar_libros(self):
        # Guarda los libros en el archivo JSON
        with open(self.archivo_json, 'w') as archivo:
            json.dump({isbn: libro.to_dict() for isbn, libro in self.libros.items()}, archivo, indent=4)

    def añadir_libro(self, libro):
        # Añade un nuevo libro a la biblioteca
        if libro.isbn in self.libros:
            print("El libro ya existe en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            self.guardar_libros()
            print(f"Libro '{libro.titulo}' añadido con éxito.")

    def prestar_libro(self, isbn):
        # Presta un libro si está disponible
        libro = self.libros.get(isbn)
        if libro:
            if not libro.prestado:
                libro.prestado = True
                self.guardar_libros()
                print(f"Libro '{libro.titulo}' prestado con éxito.")
            else:
                print("El libro ya está prestado.")
        else:
            print("Libro no encontrado.")

    def devolver_libro(self, isbn):
        # Devuelve un libro si está prestado
        libro = self.libros.get(isbn)
        if libro:
            if libro.prestado:
                libro.prestado = False
                self.guardar_libros()
                print(f"Libro '{libro.titulo}' devuelto con éxito.")
            else:
                print("El libro no está prestado.")
        else:
            print("Libro no encontrado.")

    def mostrar_libros(self):
        # Muestra todos los libros en la biblioteca
        if not self.libros:
            print("No hay libros en la biblioteca.")
            return
        for libro in self.libros.values():
            estado = "Prestado" if libro.prestado else "Disponible"
            print(f"{libro.isbn}: {libro.titulo} por {libro.autor} - {estado}")


def menu():
    # Muestra el menú principal y gestiona las opciones del usuario
    biblioteca = Biblioteca()
    opciones = {
        '1': "Añadir Libro",
        '2': "Mostrar Libros",
        '3': "Prestar Libro",
        '4': "Devolver Libro",
        '5': "Salir"
    }
    while True:
        print("\n".join([f"{key}. {value}" for key, value in opciones.items()]))
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            # Añadir un nuevo libro
            isbn = input("ISBN: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            libro = Libro(isbn, titulo, autor, categoria)
            biblioteca.añadir_libro(libro)
        elif opcion == '2':
            # Mostrar todos los libros
            biblioteca.mostrar_libros()
        elif opcion == '3':
            # Prestar un libro
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(isbn)
        elif opcion == '4':
            # Devolver un libro
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(isbn)
        elif opcion == '5':
            # Salir del programa
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()  # Ejecutar el menú principal