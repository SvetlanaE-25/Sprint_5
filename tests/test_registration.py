from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from data import Credentials
from helper import generate_registration_data
from curl import *
import time


class TestRegistration:

    
    def test_registration(self, driver):
        email, password = generate_registration_data()
        driver.get(register_page)

        #Заполнить поля Имя, Email, Пароль
        driver.find_element(*Locators.NAME_FIELD).send_keys("Svetlana")
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()#Нажать на кнопку "Зарегистрироваться"

        
        time.sleep(2) #Даем время на обработку запроса (редирект или показ ошибки)

        current_url = driver.current_url #Получаем текущий URL 

        assert current_url == main_site + "login" #проверка, что после регистрации произошел редирект на страницу с формой входа

        

class TestRegistrationShortPassword:
    def test_registration_short_password(self, driver):
        email, _ = generate_registration_data()
        driver.get(register_page)
        
        #Заполнить поля Имя, Email, Пароль
        driver.find_element(*Locators.NAME_FIELD).send_keys("Svetlana")
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credentials.short_password)#ввести невалидный пароль
        driver.find_element(*Locators.REGISTER_BUTTON).click() #Нажать на кнопку "Зарегистрироваться"

            
        validation_error_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.VALIDATION_ERROR_TEXT)).text
        
        assert validation_error_text == 'Некорректный пароль'