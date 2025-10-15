from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")
caixa_pesquisa  = driver.find_element(By.NAME,'q')
time.sleep(3)
caixa_pesquisa.send_keys("Python")
caixa_pesquisa.send_keys(Keys.ENTER)
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.maximize_window()
time.sleep(2)


driver.minimize_window()
time.sleep(2)

driver.quit()