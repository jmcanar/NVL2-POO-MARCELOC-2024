import os

# Definimos la clase Producto para representar cada producto en nuestro inventario.
class Producto:
    def __init__(self, ID, nombre, cantidad, precio):
        self.ID = ID  # ID único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad en stock
        self.precio = precio  # Precio del producto

    # Métodos para obtener los atributos del producto.
    def get_id(self):
        return self.ID

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos para establecer los nuevos valores de cantidad y precio.
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    # Método para representar el producto en formato de texto para el archivo.
    def to_string(self):
        return f"{self.ID},{self.nombre},{self.cantidad},{self.precio}\n"

# Clase para manejar el archivo de inventario
class ArchivoInventario:
    @staticmethod
    def cargar_inventario():
        productos = []
        if os.path.exists("inventario.txt"):
            try:
                with open("inventario.txt", "r") as file:
                    for line in file:
                        ID, nombre, cantidad, precio = line.strip().split(',')
                        productos.append(Producto(ID, nombre, int(cantidad), float(precio)))
            except (FileNotFoundError, PermissionError) as e:
                print(f"Error al cargar el inventario: {e}")
        return productos

    @staticmethod
    def guardar_inventario(productos):
        try:
            with open("inventario.txt", "w") as file:
                for producto in productos:
                    file.write(producto.to_string())
        except (PermissionError) as e:
            print(f"Error al guardar el inventario: {e}")

# Definimos la clase Inventario para manejar la colección de productos.
class Inventario:
    def __init__(self):
        self.productos = ArchivoInventario.cargar_inventario()  # Cargamos los productos del archivo

    # Método para añadir un producto al inventario y al archivo.
    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con el mismo ID.")
                return
        self.productos.append(producto)
        ArchivoInventario.guardar_inventario(self.productos)  # Guardamos cambios en el archivo
        print("Producto añadido con éxito al inventario y guardado en el archivo.")

    # Método para eliminar un producto por su ID.
    def eliminar_producto(self, ID):
        for i, producto in enumerate(self.productos):
            if producto.get_id() == ID:
                del self.productos[i]
                ArchivoInventario.guardar_inventario(self.productos)  # Guardamos cambios en el archivo
                print(f"Producto con ID {ID} eliminado y cambios guardados en el archivo.")
                return
        print("Error: Producto no encontrado.")

    # Método para actualizar la cantidad y/o el precio de un producto.
    def actualizar_producto(self, ID, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == ID:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                ArchivoInventario.guardar_inventario(self.productos)  # Guardamos cambios en el archivo
                print("Producto actualizado con éxito y cambios guardados en el archivo.")
                return
        print("Error: Producto no encontrado.")

    # Método para buscar productos por nombre.
    def buscar_producto_por_nombre(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for p in encontrados:
                print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")
        else:
            print("No se encontraron productos con ese nombre.")

    # Método para mostrar todos los productos en el inventario.
    def mostrar_todos_los_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
            return
        for p in self.productos:
            print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")

# Función que despliega el menú de opciones para interactuar con el inventario
def menu():
    inventario = Inventario()

    while True:
        print("\n------ Menú de Inventario ------")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ID = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(ID, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            ID = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(ID)

        elif opcion == "3":
            ID = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje vacío para no cambiar): ")
            precio = input("Ingrese el nuevo precio (deje vacío para no cambiar): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(ID, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos_los_productos()

        elif opcion == "6":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, intente nuevamente.")

# Punto de entrada del programa
if __name__ == "__main__":
    menu()  # Llamamos a la función del menú para iniciar la aplicación