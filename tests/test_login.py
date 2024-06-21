from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from url_pages import Url
from locators import LocatorsLoginPage
from test_account_info import TestAccountInfo
from locators import LocatorsAccountPage


class TestLogin:
    # Тест вход по кнопке «Войти в аккаунт» на главной
    def test_login_main_page(self, driver):
        driver.get(Url.main_page_url)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsLoginPage.login_in_account))
        driver.find_element(*LocatorsLoginPage.login_in_account).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsLoginPage.email_input))
        driver.find_element(*LocatorsLoginPage.email_input).send_keys(TestAccountInfo.login_user)
        driver.find_element(*LocatorsLoginPage.password_input).send_keys(TestAccountInfo.password_user)
        driver.find_element(*LocatorsLoginPage.submit_button).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsAccountPage.order_button)).is_displayed()

    # Тест вход через кнопку «Личный кабинет»
    def test_login_account_page(self, driver):
        driver.get(Url.main_page_url)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsLoginPage.account_button))
        driver.find_element(*LocatorsLoginPage.account_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsLoginPage.email_input))
        driver.find_element(*LocatorsLoginPage.email_input).send_keys(TestAccountInfo.login_user)
        driver.find_element(*LocatorsLoginPage.password_input).send_keys(TestAccountInfo.password_user)
        driver.find_element(*LocatorsLoginPage.submit_button).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsAccountPage.order_button)).is_displayed()

    # Тест вход через кнопку в форме регистрации
    def test_login_registration_page(self, driver):
        driver.get(Url.registration_page_url)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsLoginPage.login_in_account_registration))
        driver.find_element(*LocatorsLoginPage.login_in_account_registration).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsLoginPage.email_input))
        driver.find_element(*LocatorsLoginPage.email_input).send_keys(TestAccountInfo.login_user)
        driver.find_element(*LocatorsLoginPage.password_input).send_keys(TestAccountInfo.password_user)
        driver.find_element(*LocatorsLoginPage.submit_button).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsAccountPage.order_button)).is_displayed()

    # Тест вход через кнопку в форме восстановления пароля
    def test_login_forgot_password_page(self, driver):
        driver.get(Url.forgot_password_page_url)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsLoginPage.login_in_account_registration))
        driver.find_element(*LocatorsLoginPage.login_in_account_registration).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsLoginPage.email_input))
        driver.find_element(*LocatorsLoginPage.email_input).send_keys(TestAccountInfo.login_user)
        driver.find_element(*LocatorsLoginPage.password_input).send_keys(TestAccountInfo.password_user)
        driver.find_element(*LocatorsLoginPage.submit_button).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsAccountPage.order_button)).is_displayed()
