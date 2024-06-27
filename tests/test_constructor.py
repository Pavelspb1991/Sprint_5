from conftest import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import LocatorsConstructor
from url_pages import Url


class TestConstructor:

    # Тест проверяет переход по разделам при нажатии на кнопку Булки
    def test_constructor_switch_bun_button(self, driver):
        driver.get(Url.main_page_url)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsConstructor.bun_button))
        driver.find_element(*LocatorsConstructor.sauce_button).click()
        driver.find_element(*LocatorsConstructor.bun_button).click()
        assert 'tab_tab_type_current__2BEPc' in driver.find_element(*LocatorsConstructor.active_button).get_attribute('class')

    # Тест проверяет переход по разделам при нажатии на кнопку Соусы
    def test_constructor_switch_sauce_button(self, driver):
        driver.get(Url.main_page_url)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsConstructor.sauce_button))
        driver.find_element(*LocatorsConstructor.sauce_button).click()
        assert 'tab_tab_type_current__2BEPc' in driver.find_element(*LocatorsConstructor.sauce_button).get_attribute('class')

    # Тест проверяет переход по разделам при нажатии на кнопку Начинки
    def test_constructor_switch_ingredient_button(self, driver):
        driver.get(Url.main_page_url)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LocatorsConstructor.ingredient_button))
        driver.find_element(*LocatorsConstructor.ingredient_button).click()
        assert 'tab_tab_type_current__2BEPc' in driver.find_element(*LocatorsConstructor.ingredient_button).get_attribute('class')


