from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import page_header, page_order_button
import allure

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Дожидаемся загрузки страницы')
    def wait_for_load_main_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(page_header))

    @allure.step('Кликаем на кнопку Заказать')
    def click_order_button(self):
        button = self.driver.find_element(*page_order_button)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        button.click()

    @allure.step('Кликаем на вопрос раздела FAQ')
    def click_question_block(self, question):
        question_block = self.driver.find_element(*question)
        self.driver.execute_script("arguments[0].scrollIntoView();", question_block)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(question))
        question_block.click()
