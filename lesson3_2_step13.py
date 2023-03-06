from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
import unittest
from selenium import webdriver
import time 

browser = webdriver.Chrome()

class TestAbs(unittest.TestCase):
    def test_abs1(self):
    
        link = "http://suninjuly.github.io/registration1.html"

        browser.get(link)

        input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input3.send_keys("email@gmail.com")
        button = browser.find_element(By.CLASS_NAME, "btn-default")
        button.click()

    
        self.assertEqual("Congratulations! You have successfully registered!", "Congratulations! You have successfully registered!", "CSS selector is wrong written")


    def test_abs2(self):

        link = "http://suninjuly.github.io/registration2.html"

        browser.get(link)

        input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input3.send_keys("email@gmail.com")
        button = browser.find_element(By.CLASS_NAME, "btn-default")
        button.click()

    
        self.assertEqual("Congratulations! You have successfully registered!", "Congratulations! You have successfully registered!", "CSS selector is wrong written")

    
if __name__ == "__main__":
    unittest.main()

    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
