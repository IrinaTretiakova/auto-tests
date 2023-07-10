import pytest
import conftest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

login = conftest.login
password = conftest.password

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def test_user_is_autorised(browser):
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    #time.sleep(5) 
    enter = WebDriverWait(browser, 10). until (
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#ember33"))
        )
    enter.click()
#Вводим доступы из отдельного конфигурационного файла
    login = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
    login.send_keys(conftest.login)

    password = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
    password.send_keys(conftest.password)
    submit = browser.find_element(By.CSS_SELECTOR, ".button_with-loader")
    submit.click()
    
#нужна проверка, что окна для ввода логина и пароля больше нет
#def test_loginform_is_absent(browser):
    time.sleep(5)
    loginform = browser.find_elements(By.CSS_SELECTOR, "#id_login_email")
    print("!!!!!")
    print(loginform)

    assert not loginform, "User is not loged in"
    