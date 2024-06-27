import pytest
from selenium import webdriver
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import LocatorsLoginPage
from test_account_info import TestAccountInfo

from url_pages import Url


# Фикстура для запуска браузера
@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1600,900")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


# Фикстура для генерации email при регистрации
@pytest.fixture()
def generate_email():
    name = f"PavelTushin7{random.randint(100, 999)}"
    domain = "yandex.ru"
    return f"{name}@{domain}"


# Фикстура для авторизации
@pytest.fixture()
def login_user(driver):
    driver.get(Url.main_page_url)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsLoginPage.login_in_account))
    driver.find_element(*LocatorsLoginPage.login_in_account).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsLoginPage.email_input))
    driver.find_element(*LocatorsLoginPage.email_input).send_keys(TestAccountInfo.login_user)
    driver.find_element(*LocatorsLoginPage.password_input).send_keys(TestAccountInfo.password_user)
    driver.find_element(*LocatorsLoginPage.submit_button).click()
