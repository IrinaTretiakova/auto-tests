from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    # def calc(x):
    # return str(math.log(abs(12*math.sin(int(x)))))

    # x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    # x = x_element.text
    # y = calc(x)

    # answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    # answer.send_keys(y)

    # checkbox = browser.find_element(By.ID, "robotCheckbox")
    # checkbox.click()

    # browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)

    # radiobutton = browser.find_element(By.ID, "robotsRule")
    # radiobutton.click()

    firstname = browser.find_element(By.NAME, 'firstname')
    firstname.send_keys("first name")

    firstname = browser.find_element(By.NAME, 'lastname')
    firstname.send_keys("last name")

    firstname = browser.find_element(By.NAME, 'email')
    firstname.send_keys("email")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
