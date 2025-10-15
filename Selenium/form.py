from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.anotepad.com")

time.sleep(10)

titulo = driver.find_element(By.ID, "edit_title")
titulo.send_keys("Sou aluno do Senac!")

time.sleep(2)

desc = driver.find_element(By.ID, "edit_textarea")
desc.send_keys("Dados dados dados dados teste automáizado!")

time.sleep(5)

driver.quit()