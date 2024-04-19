# import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from products import *
import time
import pandas as pd

# Encuentra el HTML en el que se encuentran los elementos que queremos obtener
# El HTML está sin refinar, es necesario pasarlo por data_processing.py
def obtain_elements(driver):
    # Encuentra todos los elementos 'p' en la página
    TAG_NAME = "xpath"
    elements_div = driver.find_element(TAG_NAME, "/html/body/tsl-root/tsl-public/div/div/tsl-search/div/tsl-search-layout/div/div[2]/div/tsl-public-item-card-list")

    a_elements = elements_div.find_elements("class name", 'ItemCardList__item')

    # Imprime el código HTML de cada elemento 'a'
    for a_element in a_elements:
        print(a_element.get_attribute('outerHTML'))
        print("\n---------------------------------------------------\n")
    return a_elements

