import os
import subprocess

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def ejecutar_script(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        print(f"\n--- Ejecutando {ruta_script} ---\n")
        resultado = subprocess.run(['python', ruta_script_absoluta], capture_output=True, text=True)
        print(resultado.stdout)
        if resultado.stderr:
            print("Errores durante la ejecución:\n", resultado.stderr)
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el archivo: {e}")

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'programacion Orientada a Objetos (POO).py',
        '2': 'programacion tradicional.py',
        '3': 'tecnicas_de_POO.py',
        '4': 'SEMANA 4/situciones_mundo_real.py',
        '5': 'SEMANA 5/area_del_triangulo.py',
        '6': 'SEMANA 6/Semana_6.py',
        '7': 'SEMANA 7/contructores_destructores.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print('\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        print(".........................Menu Principal - Dashboard.........................")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script desde el 1 al 7 para ver su código, o '0' para salir: ")
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        if eleccion == '0':
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
            ejecutar = input("\n¿Quieres ejecutar este script? (si/no): ")
            if ejecutar.lower() == 'si':
                ejecutar_script(ruta_script)
        else:
            print("\nOpción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()