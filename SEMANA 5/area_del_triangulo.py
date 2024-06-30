# Este programa calcula el área de un triángulo utilizando la Programación Orientada a Objetos.
# Solicita al usuario ingresar la base y la altura del triángulo y calcula el área utilizando el tipo de dato float.
#definimos la clase
class AreaTriangulo:
# En esta linea de codigo se muestra los atributos
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

# En esta linea de codigo se muestra los metodos
# Función para calcular el area del triangulo
    def calcular_area(self):
        return (self.base * self.altura) / 2

# Solicitar al usuario ingresar la base y la altura
base = float(input("Ingrese la base del triángulo en cm: "))
altura = float(input("Ingrese la altura del triángulo en cm: "))

# Crear una instancia de la clase Triangulo
triangulo = AreaTriangulo(base, altura)

# Calcular el área
area = triangulo.calcular_area()

# Mostrar el resultado
print(f"El área del triángulo es: {area} cm^2")

#Nombre: Marcelo Cañar