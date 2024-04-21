from buscar_productos import *

# Devuelve una lista con todos los links
def leer_links():
    try:
        with open('links.txt', 'r') as archivo:
            lineas = archivo.readlines()
            links = [linea.strip() for linea in lineas]
            return links
    except IOError:
        print("Error: El archivo 'links.txt' no se pudo abrir. Asegúrate de que el archivo existe y está en el directorio correcto.")
        return []



if __name__ == '__main__':
    links = leer_links()
    
    for i in range(len(links)):
        print("Buscando productos en:")
        print(i)
        time.sleep(3)
        print(links[i])
        buscar_productos(links[i])

