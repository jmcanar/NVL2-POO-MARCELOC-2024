class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, temperatura):
        self.temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)
# Función principal para organizar el flujo del programa
def main():
    clima_semanal = ClimaDiario()
    print("Registro de temperaturas diarias y cálculo del promedio semanal")
    for dia in range(7):
        temp = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
        clima_semanal.ingresar_temperatura(temp)

    promedio = clima_semanal.calcular_promedio_semanal()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")
# Ejecutar la función principal
if __name__ == "__main__":
    main()