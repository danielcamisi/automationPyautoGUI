from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

driver = webdriver.Chrome()
driver.get("https://automatizado.netlify.app/")

time.sleep(2)

name = driver.find_element(By.ID, "nome")
name.send_keys("Daniel Camillo Silva")

time.sleep(2)

email = driver.find_element(By.ID, "email")
email.send_keys("danielcamillo2010@hotmail.com")

time.sleep(1)

phone = driver.find_element(By.ID, "telefone" )
phone.send_keys("1999456557")

time.sleep(1)

datanasc = driver.find_element(By.ID, "nascimento")
datanasc.send_keys("09072003")

time.sleep(1)

cpf = driver.find_element(By.ID, "cpf")
cpf.send_keys("519.283.221-11")

time.sleep(1)

cep = driver.find_element(By.ID, "cep")
cep.send_keys("13060-840")

time.sleep(1)

endereco = driver.find_element(By.ID, "endereco")
endereco.send_keys("Av marcio egídio de Souza Aranha")

time.sleep(1)

city = driver.find_element(By.ID,"cidade")
city.send_keys("Campinas")

time.sleep(1)

state = driver.find_element(By.ID, "estado")
state.send_keys("SP")

time.sleep(1)

obs = driver.find_element(By.ID,"observacoes")
obs.send_keys("Somente um teste automatizado")

time.sleep(1)

form = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
form.click()

time.sleep(1)

pyautogui.press('enter')

time.sleep(10)

driver.quit()
