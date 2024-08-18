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

    # Definimos la clase Inventario para manejar la colección de productos.


class Inventario:
    def __init__(self):
        self.productos = []  # Lista para almacenar productos

    # Método para añadir un producto al inventario.
    def añadir_producto(self, producto):
        # Verificamos si el producto ya existe en el inventario por su ID
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con el mismo ID.")
                return
                # Si no existe, lo añadimos a la lista de productos
        self.productos.append(producto)
        print("Producto añadido con éxito.")

        # Método para eliminar un producto por su ID.

    def eliminar_producto(self, ID):
        # Buscamos el producto en el inventario
        for i, producto in enumerate(self.productos):
            if producto.get_id() == ID:
                del self.productos[i]  # Eliminamos el producto de la lista
                print(f"Producto con ID {ID} eliminado.")
                return
                # Si no se encuentra, informamos al usuario
        print("Error: Producto no encontrado.")

        # Método para actualizar la cantidad y/o el precio de un producto.

    def actualizar_producto(self, ID, cantidad=None, precio=None):
        # Buscamos el producto con el ID especificado
        for producto in self.productos:
            if producto.get_id() == ID:
                # Si se proporciona una nueva cantidad, la actualizamos
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                    # Si se proporciona un nuevo precio, lo actualizamos
                if precio is not None:
                    producto.set_precio(precio)
                print("Producto actualizado con éxito.")
                return
                # Si el producto no se encuentra, notificamos al usuario
        print("Error: Producto no encontrado.")

        # Método para buscar productos por nombre.

    def buscar_producto_por_nombre(self, nombre):
        # Filtramos productos cuyo nombre contiene el texto proporcionado
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        # Si se encuentran productos, mostramos la información de cada uno
        if encontrados:
            for p in encontrados:
                print(
                    f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")
        else:
            print("No se encontraron productos con ese nombre.")

            # Método para mostrar todos los productos en el inventario.

    def mostrar_todos_los_productos(self):
        # Si no hay productos, informamos al usuario
        if not self.productos:
            print("No hay productos en el inventario.")
            return
            # Mostramos la información de cada producto
        for p in self.productos:
            print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")

        # Función que despliega el menú de opciones para interactuar con el inventario


def menu():
    inventario = Inventario()  # Creamos una instancia de Inventario

    while True:
        print("\n------ Menú de Inventario ------")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        # Solicitamos al usuario que seleccione una opción
        opcion = input("Seleccione una opción: ")

        # Opción para añadir un nuevo producto
        if opcion == "1":
            ID = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(ID, nombre, cantidad, precio)  # Creamos una nueva instancia de Producto
            inventario.añadir_producto(producto)  # Añadimos el producto al inventario

        # Opción para eliminar un producto por su ID
        elif opcion == "2":
            ID = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(ID)  # Llamamos a la función para eliminar el producto

        # Opción para actualizar un producto existente
        elif opcion == "3":
            ID = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje vacío para no cambiar): ")
            precio = input("Ingrese el nuevo precio (deje vacío para no cambiar): ")

            # Convertimos los inputs a sus tipos correspondientes si no están vacíos
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(ID, cantidad, precio)  # Actualizamos la información del producto

        # Opción para buscar productos por nombre
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)  # Buscamos el producto

        # Opción para mostrar todos los productos en el inventario
        elif opcion == "5":
            inventario.mostrar_todos_los_productos()  # Mostramos los productos existentes

        # Opción para salir del programa
        elif opcion == "6":
            print("Saliendo del programa.")
            break  # Terminamos el bucle y cerramos el programa

        # Opción no válida
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

        # Punto de entrada del programa


if __name__ == "__main__":
    menu()  # Llamamos a la función del menú para iniciar la aplicación