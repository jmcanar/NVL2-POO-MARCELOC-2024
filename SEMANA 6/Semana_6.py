# Clase base: Animal
class Animal:
    def __init__(self, nombre, edad):
        # Atributos privados (encapsulación)
        self.__nombre = nombre
        self.__edad = edad

    def comer(self):
        print(f"{self.__nombre} está comiendo.")

    def dormir(self):
        print(f"{self.__nombre} está durmiendo.")

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad


# Clase derivada: Perro (herencia de Animal)
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.__raza = raza

    def ladrar(self):
        print(f"{self.get_nombre()} está ladrando.")

    def get_raza(self):
        return self.__raza


# Clase derivada: Gato (herencia de Animal)
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.__color = color

    def maullar(self):
        print(f"{self.get_nombre()} está maullando.")

    def get_color(self):
        return self.__color


# Ejemplo de polimorfismo: método sobrescrito
def saludar(animal):
    print(f"Hola, soy {animal.get_nombre()}")

# Creación de instancias
perro = Perro("Max", 3, "Pequines")
gato = Gato("Pantera", 2, "Negro")

# Uso de métodos
perro.comer()
perro.ladrar()
print(f"Raza: {perro.get_raza()}")

gato.comer()
gato.maullar()
print(f"Color: {gato.get_color()}")

# Uso del método polimórfico
saludar(perro)
saludar(gato)