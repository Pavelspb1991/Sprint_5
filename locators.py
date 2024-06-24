from selenium.webdriver.common.by import By


# Локаторы для страницы регистрации
class LocatorsRegistrationPage:
    name_input = (By.XPATH, "//label[text()='Имя']/parent::div/input")  # локатор для поля ввода имени
    email_input = (By.XPATH, "//label[text()='Email']/parent::div/input")  # локатор для поля ввода email
    password_input = (By.XPATH, "//label[text()='Пароль']/parent::div/input")  # локатор для поля ввода пароля
    register_title = (By.XPATH, "//h2[text()='Регистрация']")  # локатор для заголовка
    submit_button = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # локатор для кнопки "Зарегистрироваться" страницы регистрации
    error_message = (By.XPATH,
                     "//p[contains(@class, 'input__error') and contains(text(), 'Некорректный пароль')]")  # локатор для ошибки при регистрации


# Локаторы для страницы логина
class LocatorsLoginPage:
    email_input = (By.XPATH, "//label[text()='Email']/parent::div/input")  # локатор для поля ввода email
    password_input = (By.XPATH, "//label[text()='Пароль']/parent::div/input")  # локатор для поля ввода пароля
    login_title = (By.XPATH, "//h2[text()='Вход']")  # локатор для заголовка
    submit_button = (By.XPATH, "//button[contains(text(), 'Войти')]")  # локатор для кнопки "Войти" в странице логина
    account_button = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")  # локатор для кнопки "Личный Кабинет"
    name = (By.XPATH, "//label[text()='Имя']/parent::div/input")  # локатор для имени в личном кабинете
    login = (By.XPATH, '//*[text()="Логин"]/following-sibling::input')  # локатор для email
    login_in_account = (By.XPATH,
                        './/button[contains(text(), "Войти в аккаунт")]')  # локатор для кнопки "Войти в аккаунт" из главной страницы
    login_in_account_registration = (
        By.XPATH, "//a[@class='Auth_link__1fOlj']")  # локатор для кнопки "Войти" в форме регистрации


# Локаторы для страницы личного кабинета
class LocatorsAccountPage:
    order_button = (By.XPATH, "//button[text()='Оформить заказ']")  # локатор кнопки "Оформить заказ"
    constuctor_button = (By.XPATH, '//p[contains(text(), "Конструктор")]/parent::a')  # локатор кнопки "Конструктор"
    logo = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/a")  # лолкатор логотипа
    exit_button = (By.XPATH, "//button[text()='Выход']")  # локатор кнопки "Выход"


# Локаторы для конструктора
class LocatorsConstructor:
    bun_button = (By.XPATH, "//span[text()='Булки']/parent::div")  # Локатор кнопки "Булки"
    sauce_button = (By.XPATH, "//span[text()='Соусы']/parent::div")  # Локатор кнопки Соусы
    ingredient_button = (By.XPATH, "//span[text()='Начинки']/parent::div")  # Локатор кнопки "Начинки"
    active_button = By.XPATH, ('//div[@class = '
                               '"tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')
    # Локатор активного элемента в конструкторе
