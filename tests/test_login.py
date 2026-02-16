from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from locators import Locators
from data import Credentials
from curl import *


class TestLogin:
    def test_account_button_login(self, driver):#проверка входа через кнопку "Войти в аккаунт" на главной старнице
        #Открываем главную страницу
        driver.get(main_site)
        #Находим кнопку "Войти в аккаунт" и кликаем
        driver.find_element(*Locators.MAIN_PAGE_LOGIN_BUTTON).click()

        #Заполняем поля и кликаем по кнопке "Войти" 
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        time.sleep(2) #Даем время на обработку запроса
               
        assert driver.current_url == main_site #Проверяем, что после авторизации открылась главная страница
        assert driver.find_element(*Locators.ORDER_BUTTON)#Проверяем, что после авторизации на главной странице есть кнопка для оформления заказа

        driver.quit()



    def test_personal_cabinet_login(self, driver):#проверка входа через личный кабинет
        #Открываем главную страницу
        driver.get(main_site)
        #Находим кнопку "Личный Кабинет" и кликаем
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        #Заполняем поля и кликаем по кнопке "Войти"        
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        time.sleep(2) #Даем время на обработку запроса

        #Проверяем, что после авторизации открылась главная страница
        assert driver.current_url == main_site
        #Проверяем, что после авторизации на главной странице есть кнопка для оформления заказа
        assert driver.find_element(*Locators.ORDER_BUTTON)

        driver.quit()


    def test_login_from_registration(self, driver):#проверка входа через кнопку через форму регистрации
        #Открываем страницу с формой для регистрации
        driver.get(register_page)
        #Находим ссылку "Войти" и кликаем
        driver.find_element(*Locators.LOGIN_LINK).click()

        #Заполняем поля и кликаем по кнопке "Войти" 
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        time.sleep(2) #Даем время на обработку запроса

        #Проверяем, что после авторизации открылась главная страница
        assert driver.current_url == main_site
        #Проверяем, что после авторизации на главной странице есть кнопка для оформления заказа
        assert driver.find_element(*Locators.ORDER_BUTTON)

        driver.quit()


    def test_login_from_password_recovery(self, driver):#проверка входа через кнопку в форме восстановления пароля
        #Открываем страницу с формой для входа
        driver.get(login_page)
        #Находим ссылку "Восстановить пароль" и кликаем
        driver.find_element(*Locators.PASSWORD_RECOVERY_LINK).click()

        
        #Ждем пока загрузится страница с формой восстановления пароля
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.FORGOT_PASSWORD_PAGE))
        #Проверка что мы на странице восстановления пароля
        assert driver.current_url == main_site + 'forgot-password'
        
        #Находим ссылку "Войти" и кликаем
        driver.find_element(*Locators.LOGIN_LINK_ON_FORGOT_PAGE).click()

        #Заполняем поля и кликаем по кнопке "Войти" 
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        time.sleep(2) #Даем время на обработку запроса

        #Проверяем, что после авторизации открылась главная страница
        assert driver.current_url == main_site
        #Проверяем, что после авторизации на главной странице есть кнопка для оформления заказа
        assert driver.find_element(*Locators.ORDER_BUTTON)

        driver.quit()