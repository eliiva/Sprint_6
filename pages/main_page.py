from locators.main_page_locators import header_order_button, yandex_logo, page_header, page_order_button
from pages.base_page import BasePage
import allure

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Дожидаемся загрузки страницы')
    def wait_for_load_main_page(self):
        super().wait_for_load_element(page_header)

    @allure.step('Кликаем на логотип Яндекса')
    def click_yandex_logo(self):
        super().click_page_element(yandex_logo)

    @allure.step('Кликаем на кнопку Заказать в хэдере')
    def click_header_order_button(self):
        super().click_page_element(header_order_button)

    @allure.step('Кликаем на кнопку Заказать на странице')
    def click_page_order_button(self):
        super().scroll_page_to_element(page_order_button)
        super().click_page_element(page_order_button)

    @allure.step('Кликаем на вопрос раздела FAQ')
    def click_question_block(self, question):
        super().scroll_page_to_element(question)
        super().wait_for_load_element(question)
        super().click_page_element(question)
