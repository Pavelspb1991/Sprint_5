from conftest import driver
from conftest import generate_email
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LocatorsRegistrationPage, LocatorsLoginPage
from url_pages import Url


# Тест на регистрацию с валидными данными
class TestRegistration:
    def test_registration_valid_data(self, driver, generate_email):
        driver.get(Url.registration_page_url)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsRegistrationPage.register_title))
        name = "Павел"
        email = generate_email
        password = '123456'
        driver.find_element(*LocatorsRegistrationPage.name_input).send_keys(name)
        driver.find_element(*LocatorsRegistrationPage.email_input).send_keys(email)
        driver.find_element(*LocatorsRegistrationPage.password_input).send_keys(password)
        driver.find_element(*LocatorsRegistrationPage.submit_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsLoginPage.login_title))
        # авторизация в личный кабинет
        driver.find_element(*LocatorsLoginPage.email_input).send_keys(email)
        driver.find_element(*LocatorsLoginPage.password_input).send_keys(password)
        driver.find_element(*LocatorsLoginPage.submit_button).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LocatorsLoginPage.account_button))
        driver.find_element(*LocatorsLoginPage.account_button).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LocatorsLoginPage.name))
        name_current_user = driver.find_element(*LocatorsLoginPage.name).get_attribute('value')
        login_current_user = driver.find_element(*LocatorsLoginPage.login).get_attribute('value')
        # сравниваем данные, которые мы вводили при регистрации с теми, что в личном кабинете
        assert name_current_user == name and login_current_user == email.lower()

    # Негативная проверка на регистрацию. Ввод в поле пароль - 5 символов.
    def test_registration_password_not_valid(self, generate_email, driver):
        driver.get(Url.registration_page_url)
        name = "Павел"
        email = generate_email
        password = '12345'
        driver.find_element(*LocatorsRegistrationPage.name_input).send_keys(name)
        driver.find_element(*LocatorsRegistrationPage.email_input).send_keys(email)
        driver.find_element(*LocatorsRegistrationPage.password_input).send_keys(password)
        driver.find_element(*LocatorsRegistrationPage.submit_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsRegistrationPage.error_message))
        assert driver.find_element(*LocatorsRegistrationPage.error_message).text == 'Некорректный пароль'

    # Негативная проверка на регистрацию. Пустое поле имени
    def test_registration_name_is_empty(self, generate_email, driver):
        driver.get(Url.registration_page_url)
        name = ""
        email = generate_email
        password = '123456'
        driver.find_element(*LocatorsRegistrationPage.name_input).send_keys(name)
        driver.find_element(*LocatorsRegistrationPage.email_input).send_keys(email)
        driver.find_element(*LocatorsRegistrationPage.password_input).send_keys(password)
        driver.find_element(*LocatorsRegistrationPage.submit_button).click()
        assert driver.find_element(*LocatorsRegistrationPage.submit_button).is_displayed()
