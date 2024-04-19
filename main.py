from web_acces import *
from obtain_elements import *
from data_processing import *
import pandas as pd
import time
from products import *
import requests
from avisos import *
import os

while True:
    # Link que queremos screpar
    link = 'https://es.wallapop.com/app/search?filters_source=search_box&keywords=thinkpad%20carbon&longitude=-3.69196&latitude=40.41956'
    #Ubicacion del csv donde se guardan los productos
    csv_path = '/home/daniel/Downloads/bot-wallapop-AI-main/productos.csv'
    #Datos para enviar mensajes por telegram
    token = '7036583138:AAFdsovf1zwXA3rP2IITx_2Uc_5kJzTjxgU'
    chat_id = '407676263'
    enviar_mensaje_telegram(token, chat_id, 'empezamuuuuuuuooos')
    #Array que contendrá los nuevos productos que se han encontrado
    lista_nuevos_productos = []

    #Comprobar si el archivo CSV está vacío
    if os.stat(csv_path).st_size == 0:
        print("El archivo CSV está vacío")
        lista_enlaces = []
    else:
        df = pd.read_csv(csv_path)
        #Leer el csv y crear una lista con todos los links para procesarlos más adelante.
        lista_enlaces = df['descripcion'].tolist()
        lista_enlaces = df['descripcion'].tolist()



    # Abre el link, rechaza las cookies y deja todo listo para scraping
    driver = open_link(link)

    # Encuentra los elementos que queremos obtener
    elements = obtain_elements(driver)

    # Procesa los elementos obtenidos
    lista_procutos = process_data(elements, lista_enlaces, lista_nuevos_productos)
    # Después de abrir el navegador espera unos segundos antes de cerrarse.
    time.sleep(20)
    # Extraer las propiedades de cada producto y guardarlas en un diccionario
    data = [{'nombre': producto.titulo, 'precio': producto.precio, 'descripcion': producto.link} for producto in lista_procutos]
    # Convertir la lista de diccionarios en un DataFrame
    df = pd.DataFrame(data)
    # Escribir los datos en un archivo CSV
    df.to_csv(csv_path, index=False)
    #Imprimir los nuevos productos que se han encontrado y enviar aviso con ellos
    print("ESTOS SON LOS NUEVOS PRODUCTOS QUE SE HAN ENCONTRADO:")
    for producto in lista_nuevos_productos:
        print(producto.titulo)
        print(producto.precio)
        print(producto.link)
        print("\n---------------------------------------------------\n")
        mensaje = f"Nuevo producto encontrado: {producto.titulo} por {producto.precio} en {producto.link}"
        enviar_mensaje_telegram(token, chat_id, mensaje)
    print("FIN DE LA BÚSQUEDA")




        # Link que queremos screpar
    link = 'https://es.wallapop.com/app/search?filters_source=search_box&keywords=thinkpad%20carbon&longitude=-3.69196&latitude=40.41956'
    #Ubicacion del csv donde se guardan los productos
    csv_path = '/home/daniel/Downloads/bot-wallapop-AI-main/productos.csv'
    #Datos para enviar mensajes por telegram
    token = '7036583138:AAFdsovf1zwXA3rP2IITx_2Uc_5kJzTjxgU'
    chat_id = '407676263'
    enviar_mensaje_telegram(token, chat_id, 'empezamuuuuuuuooos')
    #Array que contendrá los nuevos productos que se han encontrado
    lista_nuevos_productos = []

    #Comprobar si el archivo CSV está vacío
    if os.stat(csv_path).st_size == 0:
        print("El archivo CSV está vacío")
        lista_enlaces = []
    else:
        df = pd.read_csv(csv_path)
        #Leer el csv y crear una lista con todos los links para procesarlos más adelante.
        lista_enlaces = df['descripcion'].tolist()
        lista_enlaces = df['descripcion'].tolist()



    # Abre el link, rechaza las cookies y deja todo listo para scraping
    driver = open_link(link)

    # Encuentra los elementos que queremos obtener
    elements = obtain_elements(driver)

    # Procesa los elementos obtenidos
    lista_procutos = process_data(elements, lista_enlaces, lista_nuevos_productos)
    # Después de abrir el navegador espera unos segundos antes de cerrarse.
    time.sleep(20)
    # Extraer las propiedades de cada producto y guardarlas en un diccionario
    data = [{'nombre': producto.titulo, 'precio': producto.precio, 'descripcion': producto.link} for producto in lista_procutos]
    # Convertir la lista de diccionarios en un DataFrame
    df = pd.DataFrame(data)
    # Escribir los datos en un archivo CSV
    df.to_csv(csv_path, index=False)
    #Imprimir los nuevos productos que se han encontrado y enviar aviso con ellos
    print("ESTOS SON LOS NUEVOS PRODUCTOS QUE SE HAN ENCONTRADO:")
    for producto in lista_nuevos_productos:
        print(producto.titulo)
        print(producto.precio)
        print(producto.link)
        print("\n---------------------------------------------------\n")
        mensaje = f"Nuevo producto encontrado: {producto.titulo} por {producto.precio} en {producto.link}"
        enviar_mensaje_telegram(token, chat_id, mensaje)
    print("FIN DE LA BÚSQUEDA")
    print("Cerrando el navegador...")
    driver.quit()
    time.sleep(180)


