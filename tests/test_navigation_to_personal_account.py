from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import LocatorsLoginPage, LocatorsAccountPage
from conftest import login_user


class Test_navigation_to_personal_page:
    # Тест переход по клику на «Личный кабинет» с главной страницы. С использованием фукстуры для авторизации
    def test_navigation_to_personal_page(self, driver, login_user):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsLoginPage.account_button))
        driver.find_element(*LocatorsLoginPage.account_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsLoginPage.name))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    # Тест переход по клику на «Конструктор» из личного кабинета. С использованием фукстуры для авторизации
    def test_navigation_from_personal_account_to_constructor(self,driver, login_user):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsLoginPage.account_button))
        driver.find_element(*LocatorsLoginPage.account_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsAccountPage.constuctor_button))
        driver.find_element(*LocatorsAccountPage.constuctor_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsLoginPage.account_button))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    # Тест переход по клику на Логотип Stellar Burgers из личного кабинета. С использованием фукстуры для авторизации
    def test_navigation_from_personal_account_to_home_by_logo(self,driver, login_user):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsLoginPage.account_button))
        driver.find_element(*LocatorsLoginPage.account_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsAccountPage.logo))
        driver.find_element(*LocatorsAccountPage.logo).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsLoginPage.account_button))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"





