#Тут хранятся фикстуры
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # pyright: ignore[reportMissingImports]
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from curl import *
from data import Credentials
from locators import Locators


@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для создания и использования драйвера
    """
    options = Options()
    options.add_argument("--window-size=1600,900")
    options.add_experimental_option("prefs", {
            "profile.password_manager_leak_detection": False
        })
    #options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()

@pytest.fixture
def login_authorized_profile(driver):
    """
    Фикстура для авторизации пользователя.
    """
    driver.get(login_page)#перейти на страницу с формой входа

    #заполнить поля
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credentials.password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()   

    WebDriverWait(driver, 5).until(EC.url_to_be(main_site))#Ожидание загрузки главной страницы

    return driver

@pytest.fixture
def authorized_user_personal_account(driver):
    """Авторизация + переход в Личный кабинет"""
    # Сначала авторизуемся
    driver.get(login_page)
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credentials.password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    
    # Ждем главную страницу
    WebDriverWait(driver, 5).until(EC.url_to_be(main_site))
    
    # Переходим в профиль
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(main_site + 'account/profile'))
    
    return driver