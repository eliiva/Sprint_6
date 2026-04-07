import allure
import pytest
from selenium import webdriver
from pages.main_page import MainPage
from locators.main_page_locators import price_question_block, price_answer_block, several_scooters_question_block, several_scooters_answer_block, time_calc_question_block, time_calc_answer_block, today_order_question_block, today_order_answer_block, change_time_question_block, change_time_answer_block, charging_question_block, charging_answer_block, cancel_order_question_block, cancel_order_answer_block, place_question_block, place_answer_block

class TestMainPage:

    driver = None
    faq_params = [
        [price_question_block, price_answer_block, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
        [several_scooters_question_block, several_scooters_answer_block, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
        [time_calc_question_block, time_calc_answer_block, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
        [today_order_question_block, today_order_answer_block, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
        [change_time_question_block, change_time_answer_block, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
        [charging_question_block, charging_answer_block, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
        [cancel_order_question_block, cancel_order_answer_block, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
        [place_question_block, place_answer_block, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
    ]

    @classmethod
    def setup_class(cls):
        with allure.step('Открываем браузер Firefox'):
            cls.driver = webdriver.Firefox()

    @allure.title('Проверка раздела FAQ на главной странице')
    @allure.description('На странице заказа кликаем на вопрос и проверяем, что отображается вернуй ответ')
    @pytest.mark.parametrize('question_locator, answer_locator, answer_text', faq_params)
    def test_check_faq_block(self, question_locator, answer_locator, answer_text):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        main_page = MainPage(self.driver)

        main_page.wait_for_load_main_page()
        main_page.click_question_block(question_locator)

        assert self.driver.find_element(*answer_locator).text == answer_text
        
    @classmethod
    def teardown_class(cls):
        with allure.step('Закрываем браузер'):
            cls.driver.quit()
    