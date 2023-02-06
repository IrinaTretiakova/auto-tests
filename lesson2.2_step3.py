from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

# link = "http://suninjuly.github.io/selects1.html"
link = "https://suninjuly.github.io/selects2.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    # def calc(x):
    #     return str(math.log(abs(12*math.sin(int(x)))))

    element_num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    element_num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    num1 = element_num1.text
    num2 = element_num2.text

    print('num1:', num1)
    print('num2:', num2)

    c = str(int(num1) + int(num2))

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(c)

    # checkbox = browser.find_element(By.ID, "robotCheckbox")
    # checkbox.click()

    # radiobutton = browser.find_element(By.ID, "robotsRule")
    # radiobutton.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
