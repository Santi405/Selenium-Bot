from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from materias import *
import time

nombres = ['"Zanin"', '"Brizio"', '"Waniewski"', '"Lanselotto"']

service = Service(executable_path = "chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.get("https://qr-creator.com/urls/i8soKSkottLXL9ErLMoq0MtLLdFPyzc3isMibppSXhUHBEbeBsbajs6Ourpg0imxODM5sRhdODizuCQ1FygOBAA")

def click(x):
    link = driver.find_element(By.PARTIAL_LINK_TEXT, x)
    time.sleep(1)
    link.click()



for nombre in nombres:
    driver.get("https://qr-creator.com/urls/i8soKSkottLXL9ErLMoq0MtLLdFPyzc3isMibppSXhUHBEbeBsbajs6Ourpg0imxODM5sRhdODizuCQ1FygOBAA")
    click(BASICAS)
    click(AM2)

    time.sleep(2)
    rB = driver.find_element(By.XPATH, "//input[@value="+ nombre +"]")
    rB.click()

    rB = driver.find_element(By.XPATH, "//*[@id='form-main-content1']/div/div/div[2]/div[2]/div/button")
    rB.click()
    time.sleep(2)

time.sleep(10)
# Cierra el WebDriver
driver.quit()

