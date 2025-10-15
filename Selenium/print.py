from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.python.org")

time.sleep(2)
driver.save_screenshot("site_python.png")

driver.quit()
