from selenium import webdriver

#para solventar problemas con las compatibilidades de las versiones de chrome y chromedriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from avisos import *
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException

# Opciones que bypasan los sistemas de seguridad anti-bot
options = webdriver.ChromeOptions()
def enable_stealth():
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--enable-javascript")
    options.add_argument("--enable-cookies")
    options.add_argument('--disable-web-security')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])






# Abre el link, rechaza las cookies y deja todo listo para scraping
# Devuelve el driver para poder seguir trabajando con él
def open_link(link, executable_path2):
    service = Service(ChromeDriverManager().install())
    enable_stealth()
    # Primer argumento sirve para no tener que estar pelenadose con versiones de chrome y chromedriver
    driver = webdriver.Chrome(service=service, options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.maximize_window()
    driver.get(link)




    # RECHAZA COOKIES
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'onetrust-reject-all-handler')))
    button = p_elements = driver.find_element("id", 'onetrust-reject-all-handler')
    actions = ActionChains(driver)
    actions.double_click(button).perform()


    # SALTA TUTORIAL
    # Sleep importante, el botón tiene animación y tarda en aparecer
    time.sleep(1)

    # Hace tres clics en el botón de saltar
    button = p_elements = driver.find_element("xpath", '/html/body/tsl-root/tsl-public/div/div/tsl-search/div/div')
    for _ in range(5):
        try:
            button.click()
        except ElementClickInterceptedException:
            driver.find_element("tag name", 'body').click()
        time.sleep(1)  # Sleep importante por la animación


    

    
    # SCROLL y BUSCAR TODOS LOS PRODUCTOS
    #Hace click en el botón de mostrar más productos 
    mas_productos = False
    try:
        button = p_elements = driver.find_element("id", 'btn-load-more')
        actions = ActionChains(driver)
        actions.double_click(button).perform()
        sleep(1)
        mas_productos = True
    except NoSuchElementException:
        mas_productos = False
        print("No hay más productos")

    mas_productos = True
    while mas_productos:
        try:
            # Si localiza el pie de pagina quiere decir que ha llegado al final y no queda más productos por cargar
            elemento_bottom = driver.find_element("xpath", "/html/body/tsl-root/tsl-public/div/tsl-footer/footer/div[1]/div/div[2]/div/div[1]/ul/li[2]/a")
            mas_productos = False
        except NoSuchElementException:
            driver.execute_script("window.scrollTo(0, 20000000000);")
                    

    return driver

