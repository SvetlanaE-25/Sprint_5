import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from curl import *


class TestSections:
   @pytest.mark.parametrize('tab_locator,expected_tab_name', [
    (Locators.BUNS_TAB, "Булки"),
    (Locators.SAUCES_TAB, "Соусы"),
    (Locators.FILLINGS_TAB, "Начинки"),
])
   
   def test_(self, driver, tab_locator, expected_tab_name):#Параметризованный тест переключения между всеми вкладками       
        driver.get(main_site)
        if expected_tab_name != "Булки": #вкладка "Булки" активна по умолчанию, поэтому на нее не кликаем
            # Кликаем на нужную вкладку
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(tab_locator)).click()          
            # Проверяем, что активная вкладка соответствует ожидаемой
        active_tab_text = driver.find_element(*Locators.ACTIVE_TAB_TEXT).text
            
        assert expected_tab_name == active_tab_text