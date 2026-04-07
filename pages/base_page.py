from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import samokat_logo, yandex_logo, header_order_button
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Дожидаемся загрузки страницы')
    def wait_for_load_base_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(samokat_logo))

    @allure.step('Кликаем на логотим Самоката')
    def click_samokat_logo(self):
        self.driver.find_element(*samokat_logo).click()

    @allure.step('Кликаем на логотип Яндекса')
    def click_yandex_logo(self):
        self.driver.find_element(*yandex_logo).click()

    @allure.step('Кликаем на кнопку Заказать')
    def click_order_button(self):
        self.driver.find_element(*header_order_button).click()
