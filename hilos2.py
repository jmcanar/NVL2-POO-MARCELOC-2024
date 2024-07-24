import threading
import time

# Función que simula la descarga de un archivo
def descargar_archivo(nombre_archivo):
    print(f"Descargando {nombre_archivo}...")
    time.sleep(2)  # Simulación de tiempo de descarga
    print(f"{nombre_archivo} descargado.")

# Lista de archivos a descargar
archivos = ["archivo1.txt", "archivo2.txt", "archivo3.txt"]

# Crear un hilo para cada archivo a descargar
threads = []
for archivo in archivos:
    thread = threading.Thread(target=descargar_archivo, args=(archivo,))
    threads.append(thread)
    thread.start()

# Esperar a que todos los hilos terminen
for thread in threads:
    thread.join()

print("Todas las descargas han finalizado.")