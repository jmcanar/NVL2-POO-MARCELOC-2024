#temperaturas diarias programacion tradicional
# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas


# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio


# Función principal para organizar la lógica
def main():
    # Entrada de datos
    temperaturas = ingresar_temperaturas()

    # Cálculo del promedio
    promedio_semanal = calcular_promedio(temperaturas)

    # Mostrar resultado
    print(f"La temperatura promedio de la semana es: {promedio_semanal:.2f}°C")


# Llamar a la función principal
if __name__ == "__main__":
    main()
