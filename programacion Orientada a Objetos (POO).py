class ClimaDiario: #Esta clase representa la información diaria del clima.
    def __init__(self):#Método constructor que inicializa la lista
        self.temperaturas = []

    def ingresar_temperatura(self, temp):#Método para agregar una nueva temperatura a la lista.
        self.temperaturas.append(temp)

    def calcular_promedio_semanal(self):#Método para calcular el promedio semanal de las temperaturas almacenadas.
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

def main():#La función principal organiza la lógica del programa
    # Crear una instancia de ClimaDiario
    clima = ClimaDiario()

    # Ingresar las temperaturas diarias
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        clima.ingresar_temperatura(temp)

    # Calcular y mostrar el promedio semanal
    promedio_semanal = clima.calcular_promedio_semanal()
    print(f"La temperatura promedio de la semana es: {promedio_semanal:.2f}°C")

# Llamar a la función principal
if __name__ == "__main__":
    main()
