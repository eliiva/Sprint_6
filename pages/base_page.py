from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Дожидаемся загрузки элемента на странице')
    def wait_for_load_element(self, element_locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(element_locator))

    @allure.step('Кликаем по элементу')
    def click_page_element(self, element_locator):
        self.driver.find_element(*element_locator).click()

    @allure.step('Пролистываем страницу до нужного элемента')
    def scroll_page_to_element(self, element_locator):
        element = self.driver.find_element(*element_locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Указываем имя')
    def fill_input(self, input_locator, value):
        self.driver.find_element(*input_locator).send_keys(value)
