from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
 

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")


price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
    )

button = browser.find_element(By.CSS_SELECTOR, "#book")     
button.click()

def calc(x):
            return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

answer = browser.find_element(By.CSS_SELECTOR, "#answer")
answer.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, "#solve")
button.click()

 #message = browser.find_element(By.ID, "verify_message")

 #assert "successful" in message.text


    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
    # закрываем браузер после всех манипуляций
browser.quit()