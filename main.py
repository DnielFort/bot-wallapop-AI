from buscar_productos import *
import os

# Devuelve una lista con todos los links
def leer_links(path):
    try:
        with open(path, 'r') as archivo:
            lineas = archivo.readlines()
            links = [linea.strip() for linea in lineas]
            return links
    except IOError:
        print("Error: El archivo 'links.txt' no se pudo abrir. Asegúrate de que el archivo existe y está en el directorio correcto.")
        return []

load_dotenv() 
refresh_time = os.getenv("REFRESH_TIME")

if __name__ == '__main__':
    while True:
        # Obtiene la ruta al directorio 'usuarios'
        usuarios_dir = os.getenv("USUARIOS_PATH")

        # Obtiene una lista de todos los archivos y directorios en 'usuarios'
        nombres = os.listdir(usuarios_dir)

        # Recorre cada nombre en la lista
        for nombre in nombres:
            # Construye la ruta completa al archivo o directorio
            ruta_completa = os.path.join(usuarios_dir, nombre)
            # Comprueba si la ruta es a un directorio
            if os.path.isdir(ruta_completa):
                # Si es un directorio, imprime su nombre
                print(f'Accediendo al directorio: {ruta_completa}')
                # Construye la ruta al archivo links.txt dentro del directorio
                ruta_links = os.path.join(ruta_completa, 'links.txt')
                # Abre el archivo links.txt
                links = leer_links(ruta_links)
                # Imprime los links
                for link in links:
                    print(link)
                # Si hay links, buscar productos
                for i in range(len(links)):
                    if links[i] != "":
                        print("Buscando productos en:")
                        print(i)
                        time.sleep(3)
                        print(links[i])
                        buscar_productos(links[i], ruta_completa, nombre)
                    else:
                        continue
        time.sleep(int(refresh_time))







