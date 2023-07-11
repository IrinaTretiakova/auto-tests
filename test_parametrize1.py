import pytest
import conftest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


login = conftest.login
password = conftest.password

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    try:
        browser.get('chrome://settings/clearBrowserData')
        browser.find_element(By.XPATH, '//settings-ui').send_keys(Keys.ENTER)
        browser.delete_all_cookies()
        yield browser
    finally:
        print("\nquit browser..")
        browser.quit()


@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_links(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)
    #wait = WebDriverWait(browser, 10)
    enter = WebDriverWait(browser,10). until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".navbar__auth_login"))
    )
    enter.click()
    #Вводим доступы из отдельного конфигурационного файла
    login = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
    login.send_keys(conftest.login)

    password = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
    password.send_keys(conftest.password)
    submit = browser.find_element(By.CSS_SELECTOR, ".button_with-loader")
    submit.click()
       
    answer = str(math.log(int(time.time())))
    print("!!!!!!!!", answer)
    time.sleep(10)

    InputArea = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".string-quiz__textarea"))
    )
    InputArea.send_keys(answer)

    time.sleep(5)

    SendButton = WebDriverWait(browser, 5). until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )  
    SendButton.click()

    print('!!!!! eeeeee')

    feedback = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    )

    feedback_text = feedback.text
    assert feedback_text == "Correct!", "Incorrect"
    #нужна проверка, что окна для ввода логина и пароля больше нет
    #def test_loginform_is_absent(browser):
    time.sleep(2)
#   loginform = browser.find_elements(By.CSS_SELECTOR, "#id_login_email")
#    print("!!!!!")
#    print(loginform)

#    assert not loginform, "User is not loged in"
    