from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from curl import *


class TestPersonalAccount:
    
    def test_personal_account_click(self, login_authorized_profile):#проверка перехода в личный кабинет по клику на «Личный Кабинет» после авторизации
        #Кликаем на "Личный кабинет" (уже будучи авторизованным)
        personal_account_link = WebDriverWait(login_authorized_profile, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT))
        personal_account_link.click()
        #Ждем загрузки страницы личного кабинета
        WebDriverWait(login_authorized_profile,3).until(EC.visibility_of_all_elements_located(Locators.PERSONAL_ACCOUNT_PAGE))
        #Проверяем URL
        assert login_authorized_profile.current_url == main_site + 'account/profile'

            
    def test_navigate_from_account_to_constructor(self, authorized_user_personal_account):#проверка перехода в Конструктор по клику на «Конструктор» после авторизации
        #Нажимаем на "Конструктор" в Личном кабинете (уже будучи авторизованным)
        authorized_user_personal_account.find_element(*Locators.CONSTRUCTOR_LINK).click()
        #Ожидаем переход на главную страницу
        WebDriverWait(authorized_user_personal_account, 3).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_HEADER))
        #Проверяем URL
        assert authorized_user_personal_account.current_url == main_site
        

    def test_navigate_to_constructor_via_logo_from_account(self, authorized_user_personal_account):#проверка перехода в Конструктор по клику на логотип «Stellar Burrgers» после авторизации
        #Нажимаем на логотип «Stellar Burrgers» в Личном кабинете (уже будучи авторизованным)
        authorized_user_personal_account.find_element(*Locators.LOGO).click()
        #Ожидаем переход на главную страницу
        WebDriverWait(authorized_user_personal_account, 3).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_HEADER))
        #Проверяем URL
        assert authorized_user_personal_account.current_url == main_site



    def test_logout_from_personal_account(self,  authorized_user_personal_account): #проверка выхода из Личного кабинета по клику на кнопку "Выход"
        #Находим кнопку "Выход" и кликаем
        logout_button = authorized_user_personal_account.find_element(*Locators.LOGOUT)
        logout_button.click()
        #Ожидаем,что открылась страница с формой для входа
        WebDriverWait(authorized_user_personal_account,5).until(EC.visibility_of_all_elements_located(Locators.LOGIN_FORM_PAGE))
        #Проверяем,что открылась страница с формой для входа
        assert authorized_user_personal_account.current_url == main_site + 'login'

   


