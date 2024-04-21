import time
from selenium import webdriver
from products import *
from selenium.common.exceptions import NoSuchElementException
from urllib3.exceptions import MaxRetryError

# SI ESTA PARTE FALLA ES PROBABLE QUE SEA POR HABER EJECUTADO UN driver.quit() ANTESD DE TIEMPO
# Devuelve una lista con los productos que se han encontrado en la página
def process_data(data, lista_enlaces, lista_nuevos_productos):
    # Leer los datos del archivo CSV
    lista = []
    for element in data:
        product = Product()
        try:
            #En caso de que esté display por filas
            product.set_name(element.get_attribute("title"))
            product.set_price(element.find_element("class name", "ItemCardWide__price--bold").text)
        except NoSuchElementException:
            #En caso de que esté display por recuadros
            product.set_name(element.find_element("class name", "ItemCard__title").text)
            product.set_price(element.find_element("class name", "ItemCard__price").text)
        except MaxRetryError:
            #En caso de que esté display por recuadros
            product.set_name(element.find_element("class name", "ItemCard__title").text)
            product.set_price(element.find_element("class name", "ItemCard__price").text)
        
        enlace = element.get_attribute("href")
        product.set_link(enlace)
        print(product.get_name())
        print(product.get_price())
        print(product.get_link())
        print("\n---------------------------------------------------\n")

        if product.get_link() in lista_enlaces:
            print("El elemento está en la lista")
        else:
            print("El elemento no está en la lista")
            lista_nuevos_productos.append(product)

        lista.append(product)

    return lista

