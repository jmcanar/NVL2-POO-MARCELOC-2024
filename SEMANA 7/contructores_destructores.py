class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f'Se ha creado una nueva persona llamada {self.nombre} de {self.edad} años.')

    def __del__(self):
        print(f'La persona {self.nombre} ha sido eliminada.')

# Creación de una instancia de la clase Persona
persona1 = Persona("Juan", 30)

# Creación de otra instancia de la clase Persona
persona2 = Persona("María", 25)

# Eliminación de la instancia persona1
del persona1

# La instancia persona2 sigue existiendo