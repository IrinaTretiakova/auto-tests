from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://stepik.org/lesson/25969/step/8")
time.sleep(5)
driver.quit()