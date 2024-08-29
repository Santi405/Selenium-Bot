from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

nombres = ['"Zanin"', '"Brizio"', '"Waniewski"', '"Lanselotto"']

driver = webdriver.Chrome()

for nombre in nombres:
    driver.get("https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAZ__ufG30dUNFZKRDAwWTJLWTRaUUpNV01MQjNaTTdZMS4u")

    time.sleep(2)
    rB = driver.find_element(By.XPATH, "//input[@value="+ nombre +"]")
    rB.click()

    rB = driver.find_element(By.XPATH, "//*[@id='form-main-content1']/div/div/div[2]/div[2]/div/button")
    rB.click()
    time.sleep(2)

time.sleep(10)
# Cierra el WebDriver
driver.quit()
