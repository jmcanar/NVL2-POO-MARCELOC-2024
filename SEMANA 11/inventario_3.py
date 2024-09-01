import json
import os
#Se importan los módulos json para manejar la serialización y deserialización de datos en formato JSON,
# y os para interactuar con el sistema operativo, como verificar la existencia de archivos.
class Producto:
    def __init__(self, ID, nombre, cantidad, precio):
        #"""Inicializa un nuevo producto con ID, nombre, cantidad y precio."""
        self.ID = ID
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        #"""Convierte el objeto Producto a un diccionario para guardar en JSON."""
        return {
            'ID': self.ID,
            'nombre': self.nombre,
            'cantidad': self.cantidad,
            'precio': self.precio
        }

    @classmethod
    def from_dict(cls, data):
        #"""Crea un objeto Producto a partir de un diccionario."""
        return cls(data['ID'], data['nombre'], data['cantidad'], data['precio'])

class Inventario:
    def __init__(self, archivo='inventario.json'):
        #"""Inicializa el inventario y carga los productos desde un archivo JSON, si existe."""
        self.archivo = archivo
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        #"""Carga el inventario desde un archivo JSON. Crea uno nuevo si no existe."""
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, 'r') as f:
                    data = json.load(f)
                    self.productos = [Producto.from_dict(p) for p in data]
                print("Inventario cargado exitosamente.")
            else:
                print("No se encontró archivo de inventario. Se creará uno nuevo.")
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error al cargar el inventario: {e}")
        except PermissionError:
            print("Error: No se tiene permiso para leer el archivo de inventario.")

    def guardar_inventario(self):
       # """Guarda el inventario en un archivo JSON."""
        try:
            with open(self.archivo, 'w') as f:
                json.dump([p.to_dict() for p in self.productos], f, indent=2)
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: No se tiene permiso para escribir en el archivo de inventario.")
        except IOError as e:
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        #"""Añade un nuevo producto al inventario."""
        for p in self.productos:
            if p.ID == producto.ID:
                print("Error: Ya existe un producto con el mismo ID.")
                return
        self.productos.append(producto)
        self.guardar_inventario()
        print("Producto añadido con éxito.")

    def eliminar_producto(self, ID):
        #"""Elimina un producto del inventario por su ID."""
        for i, producto in enumerate(self.productos):
            if producto.ID == ID:
                del self.productos[i]
                self.guardar_inventario()
                print(f"Producto con ID {ID} eliminado.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, ID, cantidad=None, precio=None):
        #"""Actualiza la cantidad y/o precio de un producto existente."""
        for producto in self.productos:
            if producto.ID == ID:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                self.guardar_inventario()
                print("Producto actualizado con éxito.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        #"""Busca y muestra los productos que coinciden con el nombre proporcionado."""
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(f"ID: {p.ID}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos_los_productos(self):
        #"""Muestra todos los productos en el inventario."""
        if not self.productos:
            print("No hay productos en el inventario.")
            return
        for p in self.productos:
            print(f"ID: {p.ID}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")

def menu():
    #"""Muestra el menú principal y gestiona las opciones del usuario."""
    inventario = Inventario()

    while True:
        # Menú de opciones
        print("\n------ Menú de Inventario ------")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Añadir nuevo producto
            try:
                ID = input("Ingrese el ID del producto: ")
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = float(input("Ingrese el precio del producto: "))
                producto = Producto(ID, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("Error: Por favor, ingrese valores numéricos válidos para cantidad y precio.")

        elif opcion == "2":
            # Eliminar producto por ID
            ID = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(ID)

        elif opcion == "3":
            # Actualizar producto
            try:
                ID = input("Ingrese el ID del producto a actualizar: ")
                cantidad = input("Ingrese la nueva cantidad (deje vacío para no cambiar): ")
                precio = input("Ingrese el nuevo precio (deje vacío para no cambiar): ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                inventario.actualizar_producto(ID, cantidad, precio)
            except ValueError:
                print("Error: Por favor, ingrese valores numéricos válidos para cantidad y precio.")

        elif opcion == "4":
            # Buscar producto por nombre
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == "5":
            # Mostrar todos los productos
            inventario.mostrar_todos_los_productos()

        elif opcion == "6":
            # Salir del programa
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    menu()
