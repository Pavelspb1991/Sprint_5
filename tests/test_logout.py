from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import LocatorsLoginPage, LocatorsAccountPage
from conftest import login_user


class TestLogout:

    #  Тестирование выхода из аккаунта. С использованием фикстуры
    def test_logout_from_personal_account(self, driver, login_user):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsLoginPage.account_button))
        driver.find_element(*LocatorsLoginPage.account_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsAccountPage.exit_button))
        driver.find_element(*LocatorsAccountPage.exit_button).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsLoginPage.submit_button)).is_displayed()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

