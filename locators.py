from selenium.webdriver.common.by import By


class Locators:
    #Локаторы для регистрации
    REGISTER_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Зарегистрироваться']")#кнопка с ссылкой на страницу для регистрации 
    NAME_FIELD = (By.XPATH, "//input[@name='name' and contains(@class, 'input__textfield')]") #Поле Имя 
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input") #Поле Email
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") #Поле Пароль
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") #Кнопка "Зарегистрироваться"
    VALIDATION_ERROR_TEXT = (By.XPATH, "//*[contains(@class, 'input__error') and text()='Некорректный пароль']")#надпись "Некорректный пароль"

    

    #Локаторы для входа
    PERSONAL_ACCOUNT = (By.XPATH, "//*[text() = 'Личный Кабинет']") #кнопка для перехода в Личный Кабинет
    MAIN_PAGE_LOGIN_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")#кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON = (By.XPATH, "//button[text() = 'Войти']") #кнопка "Войти"
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']") #ссылка "Войти" в форме регистрации
    PASSWORD_RECOVERY_LINK = (By.XPATH, "//a[@href='/forgot-password']") #ссылка "Восстановить пароль" в форме для входа
    LOGIN_FORM_PAGE = (By.CSS_SELECTOR, ".Auth_login__3hAey")#страница с формой для входа
    FORGOT_PASSWORD_PAGE = (By.CSS_SELECTOR, ".Auth_login__3hAey") #страница с формой для восставновления пароля
    LOGIN_LINK_ON_FORGOT_PAGE = (By.XPATH, "//a[@href='/login']") #ссылка "Войти" на странице восстановления пароля

    #Локаторы для оформления заказа
    ORDER_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']") #кнопка "Оформить заказ" на главной странице
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']") #заголовок Конструктора
    #Локаторы для разделов (табов)
    BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_') and .//span[text()='Булки']]")
    SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_') and .//span[text()='Соусы']]")
    FILLINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_') and .//span[text()='Начинки']]")
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_') and contains(@class, 'tab_tab_type_current')]") #Выбранный раздел
    ACTIVE_TAB_TEXT = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span")# Локатор для текста выбранного раздела

    #Локаторы в Личном кабинете
    PERSONAL_ACCOUNT_PAGE = (By.CSS_SELECTOR, "[href='/account']")#страница Личного кабинета
    CONSTRUCTOR_LINK = (By.XPATH, "//*[text() = 'Конструктор']")#ссылка для перехода в Конструктор
    LOGOUT = (By.XPATH, "//button[text()='Выход']")
    LOGO = (By.CSS_SELECTOR, "a[href='/']")#локатор логотипа "Stellar Burgers"