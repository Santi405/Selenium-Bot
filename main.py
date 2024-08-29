from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from materias import *
import time

service = Service(executable_path = "chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.get("https://qr-creator.com/urls/i8soKSkottLXL9ErLMoq0MtLLdFPyzc3isMibppSXhUHBEbeBsbajs6Ourpg0imxODM5sRhdODizuCQ1FygOBAA")

def click(x):
    link = driver.find_element(By.PARTIAL_LINK_TEXT, x)
    time.sleep(1)
    link.click()

click(BASICAS)
click(AM2)


time.sleep(10)

driver.quit()



