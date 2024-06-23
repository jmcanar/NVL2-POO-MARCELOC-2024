#creamos la clase producto
class Producto:
## En esta linea de codigo se muestra los atributos
    def __init__(self, nombre, precio, cantidad_disponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

 # En esta linea de codigo se muestra los metodos
    def mostrar_informacion(self):
        print(f"{self.nombre} - Precio: {self.precio} - Disponible: {self.cantidad_disponible}")
#creamos la clase cliente
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []
#En esta linea de codigo se muestra los metodos
    def agregar_producto_al_carrito(self, producto, cantidad):
        self.carrito.append((producto, cantidad))
        print(f"{self.nombre} ha agregado {cantidad} unidades de {producto.nombre} al carrito.")
#creamos la clase TiendaAlimentos
class TiendaAlimentos:
# En esta linea de codigo se muestra los atributos
    def __init__(self):
        self.inventario = []

    # En esta linea de codigo se muestra los metodos
    def agregar_producto(self, producto):
        self.inventario.append(producto)
        print(f"Se ha agregado {producto.nombre} al inventario de la tienda.")

    def mostrar_inventario(self):
        for producto in self.inventario:
            producto.mostrar_informacion()

# Creamos algunos productos
manzanas = Producto("Manzanas", 2.5, 100)
leche = Producto("Leche", 1.5, 50)

# Creamos una instancia de la clase Cliente
cliente1 = Cliente("Ana")

# Creamos una instancia de la clase TiendaAlimentos
tienda_alimentos = TiendaAlimentos()

# Agregamos los productos al inventario de la tienda
tienda_alimentos.agregar_producto(manzanas)
tienda_alimentos.agregar_producto(leche)

# Cliente agrega productos al carrito
cliente1.agregar_producto_al_carrito(manzanas, 3)
cliente1.agregar_producto_al_carrito(leche, 2)

# Mostramos el inventario de la tienda
tienda_alimentos.mostrar_inventario()