import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from curl import *


class TestSections:
   def test_buns_tab_active_by_default(self, driver):#Тест проверяет, что вкладка 'Булки' активна по умолчанию
        driver.get(main_site)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.ACTIVE_TAB_TEXT))# Ждем загрузки страницы
        active_tab_text = driver.find_element(*Locators.ACTIVE_TAB_TEXT).text # Проверяем, что активна именно вкладка "Булки"
        assert active_tab_text == "Булки"

   
   
   @pytest.mark.parametrize('tab_locator,expected_tab_name', [
    (Locators.SAUCES_TAB, "Соусы"),
    (Locators.FILLINGS_TAB, "Начинки"),
])
   
   def test_switch_to_non_default_tabs(self, driver, tab_locator, expected_tab_name):#Параметризованный тест переключения на вкладки 'Соусы' и 'Начинки'      
        driver.get(main_site)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(tab_locator)).click()  # Ждем и кликаем на вкладку (даже если она уже активна)        
        active_tab_text = driver.find_element(*Locators.ACTIVE_TAB_TEXT).text# Проверяем, что активная вкладка соответствует ожидаемой          
        assert expected_tab_name == active_tab_text
  