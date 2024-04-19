from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from avisos import *


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



#Datos para enviar mensajes por telegram
token = '7036583138:AAFdsovf1zwXA3rP2IITx_2Uc_5kJzTjxgU'
chat_id = '407676263'
service = webdriver.ChromeService(executable_path='/home/daniel/Documents/chromedriver')

# Abre el link, rechaza las cookies y deja todo listo para scraping
# Devuelve el driver para poder seguir trabajando con él
def open_link(link):
    enable_stealth()
    driver = webdriver.Chrome(options=options, service=service)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.maximize_window()
    driver.get(link)




    #rechaza cookies
    WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.ID, 'onetrust-reject-all-handler')))
    button = p_elements = driver.find_element("id", 'onetrust-reject-all-handler')
    actions = ActionChains(driver)
    actions.double_click(button).perform()



    # Haz tres clics en cualquier parte de la pantalla para quitar el tutorial de wallapop
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    button = p_elements = driver.find_element("tag name", 'body')
    sleep(1)
    for _ in range(3):
        actions = ActionChains(driver)
        button.click()
        time.sleep(1)  # espera un segundo entre cada clic

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
            elemento_bottom = driver.find_element("xpath", "/html/body/tsl-root/tsl-public/div/tsl-footer/footer/div[1]/div/div[2]/div/div[1]/ul/li[2]/a")
            mas_productos = False
        except NoSuchElementException:
                driver.execute_script("window.scrollTo(0, 20000000000);")        

    return driver

