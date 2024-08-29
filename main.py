from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from materias import *
import time

# Inicializamos
service = Service(executable_path = "chromedriver.exe")
driver = webdriver.Chrome(service = service)

# Definimos funcion para facilitar
def click(x):
    link = driver.find_element(By.PARTIAL_LINK_TEXT, x)
    time.sleep(1)
    link.click()


# Recorremos todos los nombres
for nombre in nombres:
    # Nos dirijimos a la web
    driver.get("https://qr-creator.com/urls/i8soKSkottLXL9ErLMoq0MtLLdFPyzc3isMibppSXhUHBEbeBsbajs6Ourpg0imxODM5sRhdODizuCQ1FygOBAA")

    # Entramos en la materia
    click(TIPO)
    click(MATERIA)

    # Le damos tiempo a cargar (A MODIFICAR)
    time.sleep(2)

    # Buscamos el nombre
    rB = driver.find_element(By.XPATH, "//input[@value="+ nombre +"]")
    rB.click()

    # Enviamos
    rB = driver.find_element(By.XPATH, "//*[@id='form-main-content1']/div/div/div[2]/div[2]/div/button")
    rB.click()
    time.sleep(2)

time.sleep(10)

# Cierra el WebDriver
driver.quit()

