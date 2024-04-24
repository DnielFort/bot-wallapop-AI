from web_acces import *
from obtain_elements import *
from data_processing import *
import pandas as pd
import time
from products import *
import requests
from avisos import *
import os
from acces_params import *
import re
from dotenv import load_dotenv #pip install python-dotenv
from urllib.parse import urlparse, parse_qs



#Ubicacion del csv donde se guardan los productos
#Ubicacion del executable_path de selenium, el chromedriver
#Datos para enviar mensajes por telegram
# Atención!, executable_path2 no se llega a usar, se utiliza ChromeDriverManager por tema de compatibilidades
# debido a que da problemas de compatibilidades se deja por si se necesita

def obtener_nombre_producto(link):
    # Analizar la el link
    url_parsed = urlparse(link)

    # Obtener los parámetros de la consulta
    query_params = parse_qs(url_parsed.query)

    # Obtener el valor del parámetro 'keywords'
    nombre_producto = query_params.get('keywords', [None])[0]

    return nombre_producto

def buscar_productos(link, ruta_usuario, chat_id):
    # Se avisa al usuario de que se ha encontrado un nuevo producto
    avisar = True

    # Carga el archivo .env (temporalmente esta en la funcion, pero debería estar fuera de la funcion y/o en el main)
    """¡¡¡IMPORTANTE, EN EL .ENV HAY QUE DESCOMENTAR LAS 
    #VARIABLES DE ENTORNO QUE SE VAYAN A UTILIZAR (Y COMENTAR LAS QUE NO SE USEN)!!!"""

    load_dotenv() 



    #Obtener los datos del archivo .env
    csv_path = ruta_usuario + "/"
    executable_path2 = os.getenv("EXECUTABLE_PATH")
    token = os.getenv("TOKEN")
    chat_id = os.getenv("CHAT_ID")
    limite_productos = os.getenv("LIMITE_PRODUCTOS") #AUN NO IMPLEMENTADO
    
    #Obtiene el nombre del producto a partir del link
    nombre_producto = obtener_nombre_producto(link)

    #Le da nombre al fichero CSV
    fichero_csv = f"{csv_path+nombre_producto}.csv"
    


    #Enviar mensaje de inicio
    "-----PROVISIONAL------"
    enviar_mensaje_telegram(token, chat_id, 'empezamoooOoOoOOoos')



    #Array que contendrá los nuevos productos que se han encontrado
    lista_nuevos_productos = []

    #Comprobar si el archivo CSV está vacío y/o existe
    if not os.path.exists(fichero_csv) or os.stat(fichero_csv).st_size == 0:
        #Si el archivo no existe o está vacío, se crea y se añade la cabecera
        with open(fichero_csv, 'w', newline='') as producto_csv:
            # Si se busca por primera vez no se notifica al usuario de los nuevos productos
            avisar = False

            print("El archivo CSV está vacío")        
            start_csv = pd.DataFrame(columns=["nombre", "precio", "enlace"])
            start_csv.to_csv(producto_csv, index=False)
            print("csv creado correctamente")
            lista_enlaces = []
            producto_csv.close()
        
    df = pd.read_csv(fichero_csv)
    #Leer el csv y crear una lista con todos los links para procesarlos más adelante.
    lista_enlaces = df['enlace'].tolist()

    # Abre el link, rechaza las cookies y deja todo listo para scraping
    driver = open_link(link, executable_path2)

    # Encuentra los elementos que queremos obtener
    elements = obtain_elements(driver)

    # Procesa los elementos obtenidos
    lista_productos = process_data(elements, lista_enlaces, lista_nuevos_productos)

    # Después de abrir el navegador espera unos segundos antes de cerrarse.
    time.sleep(20)

    # Extraer las propiedades de cada producto y guardarlas en un diccionario
    data = [{'nombre': producto.titulo, 'precio': producto.precio, 'enlace': producto.link} 
        for producto in lista_productos]
    
    if len(lista_productos) > 0:
        print(len(lista_productos))
        # Convertir la lista de diccionarios en un DataFrame
        df = pd.DataFrame(data)

        # Escribir los datos en un archivo CSV
        df.to_csv(fichero_csv, index=False)

    driver.quit()

    #Si no se han encontrado productos, envia aviso y borra el CSV creado anteriormente
    if len(lista_nuevos_productos) == 0 and len(df) == 0:
        print("No se han encontrado productos")
        enviar_mensaje_telegram(token, chat_id, "No se han encontrado productos")
        os.remove(fichero_csv)

    #Imprimir los nuevos productos que se han encontrado y enviar aviso con ellos
    elif len(lista_nuevos_productos) == 0 and len(df) > 1:
        print("No se han encontrado nuevos productos")
        enviar_mensaje_telegram(token, chat_id, "No se han encontrado nuevos productos")
    
    #Imprimir los productos que se han encontrado y enviar aviso con ellos
    elif len(lista_nuevos_productos) > 0 and len(df) > 2:
        print("ESTOS SON LOS NUEVOS PRODUCTOS QUE SE HAN ENCONTRADO:")
        for producto in lista_nuevos_productos:
            print(producto.titulo)
            print(producto.precio)
            print(producto.link)
            print("\n---------------------------------------------------\n")
            mensaje = f"Nuevo producto encontrado: {producto.titulo} por {producto.precio} en {producto.link}"
            if avisar:
                enviar_mensaje_telegram(token, chat_id, mensaje)
    
    print("FIN DE LA BÚSQUEDA")

