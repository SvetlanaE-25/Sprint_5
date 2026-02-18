from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from locators import Locators
from data import Credentials
from curl import *


class TestLogin:
    def test_account_button_login(self, login_through_account_button):#проверка входа через кнопку "Войти в аккаунт" на главной старнице           
        assert login_through_account_button.current_url == main_site #Проверяем, что после авторизации открылась главная страница
        assert login_through_account_button.find_element(*Locators.ORDER_BUTTON)#Проверяем, что после авторизации на главной странице есть кнопка для оформления заказа




    def test_personal_account_login(self, login_through_personal_account):#проверка входа через Личный кабинет
        assert login_through_personal_account.current_url == main_site #Проверяем, что после авторизации открылась главная страница 
        assert login_through_personal_account.find_element(*Locators.ORDER_BUTTON) #Проверяем, что после авторизации на главной странице есть кнопка для оформления заказа



    def test_login_from_registration(self, login_through_registration):#проверка входа через кнопку через форму регистрации
        assert login_through_registration.current_url == main_site #Проверяем, что после авторизации открылась главная страница
        assert login_through_registration.find_element(*Locators.ORDER_BUTTON)#Проверяем, что после авторизации на главной странице есть кнопка для оформления заказа



    def test_login_from_password_recovery(self, navigate_to_password_recovery_form):#проверка входа через кнопку в форме восстановления пароля
        #Проверка что мы на странице восстановления пароля
        assert navigate_to_password_recovery_form.current_url == main_site + 'forgot-password'
        
        navigate_to_password_recovery_form.find_element(*Locators.LOGIN_LINK_ON_FORGOT_PAGE).click()#Находим ссылку "Войти" и кликаем

        #Заполняем поля и кликаем по кнопке "Войти" 
        navigate_to_password_recovery_form.find_element(*Locators.EMAIL_FIELD).send_keys(Credentials.email)
        navigate_to_password_recovery_form.find_element(*Locators.PASSWORD_FIELD).send_keys(Credentials.password)
        navigate_to_password_recovery_form.find_element(*Locators.LOGIN_BUTTON).click()

        #Ожидаем переход на главную страницу, на которой появилась кнопка "Оформить заказ"
        WebDriverWait(navigate_to_password_recovery_form, 3).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

        assert navigate_to_password_recovery_form.current_url == main_site #Проверяем, что после авторизации открылась главная страница
        assert navigate_to_password_recovery_form.find_element(*Locators.ORDER_BUTTON)#Проверяем, что после авторизации на главной странице есть кнопка для оформления заказа