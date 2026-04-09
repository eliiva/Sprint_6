import allure
import pytest
from selenium import webdriver
from pages.main_page import MainPage
from data import faq_params
from urls import main_page_url

class TestMainPage:

    driver = None

    @classmethod
    def setup_class(cls):
        with allure.step('Открываем браузер Firefox'):
            cls.driver = webdriver.Firefox()

    @allure.title('Проверка раздела FAQ на главной странице')
    @allure.description('На странице заказа кликаем на вопрос и проверяем, что отображается вернуй ответ')
    @pytest.mark.parametrize('question_locator, answer_locator, answer_text', faq_params)
    def test_check_faq_block(self, question_locator, answer_locator, answer_text):
        self.driver.get(main_page_url)

        main_page = MainPage(self.driver)

        main_page.wait_for_load_main_page()
        main_page.click_question_block(question_locator)

        assert main_page.get_element_text(answer_locator) == answer_text
        
    @classmethod
    def teardown_class(cls):
        with allure.step('Закрываем браузер'):
            cls.driver.quit()
    