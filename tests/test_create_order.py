import allure
from selenium import webdriver
from pages.order_page import OrderPage
from pages.main_page import MainPage
from locators.order_page_locators import order_modal_header
from urls import main_page_url
from data import first_order_data, second_order_data

class TestCreateOrder:

    driver = None

    @classmethod
    def setup_class(cls):
        with allure.step('Открываем браузер Firefox'):
            cls.driver = webdriver.Firefox()

    @allure.title('Проверка создания заказа через кнопку Заказать в хэдере')
    @allure.description('Создаём заказ через кнопку Заказать в хэдере и проверяем всплывающее окно с сообщением об успехе')
    def test_create_order_by_header_order_button(self):
        self.driver.get(main_page_url)

        main_page = MainPage(self.driver)

        main_page.wait_for_load_main_page()
        main_page.click_header_order_button()

        order_page = OrderPage(self.driver)
        order_page.wait_for_load_order_page()
        order_page.fill_customer_info(
            firstname=first_order_data['firstname'],
            lastname=first_order_data['lastname'],
            address=first_order_data['address'],
            metro_station=first_order_data['metro_station'],
            phone=first_order_data['phone']
        )
        order_page.click_next_button()
        order_page.fill_rent_info_block(
            date=first_order_data['date'],
            interval_locator=first_order_data['interval_locator'],
            color_locator=first_order_data['color_locator'],
            comment=first_order_data['comment']
        )
        order_page.click_complete_order_button()
        order_page.wait_for_agree_block_load()
        order_page.click_agree_button()
        order_page.wait_for_status_block_load()

        assert "Заказ оформлен" in order_page.get_element_text(order_modal_header)

    @allure.title('Проверка создания заказа через кнопку Заказать на главной')
    @allure.description('Создаём заказ через кнопку Заказать на главной и проверяем всплывающее окно с сообщением об успехе')
    def test_create_order_by_main_page_order_button(self):
        self.driver.get(main_page_url)

        main_page = MainPage(self.driver)

        main_page.wait_for_load_main_page()
        main_page.click_page_order_button()

        order_page = OrderPage(self.driver)
        order_page.wait_for_load_order_page()
        order_page.fill_customer_info(
            firstname=second_order_data['firstname'],
            lastname=second_order_data['lastname'],
            address=second_order_data['address'],
            metro_station=second_order_data['metro_station'],
            phone=second_order_data['phone']
        )
        order_page.click_next_button()
        order_page.fill_rent_info_block(
            date=second_order_data['date'],
            interval_locator=second_order_data['interval_locator'],
            color_locator=second_order_data['color_locator'],
            comment=second_order_data['comment']
        )
        order_page.click_complete_order_button()
        order_page.wait_for_agree_block_load()
        order_page.click_agree_button()
        order_page.wait_for_status_block_load()

        assert "Заказ оформлен" in order_page.get_element_text(order_modal_header)  
        
    @classmethod
    def teardown_class(cls):
        with allure.step('Закрываем браузер'):
            cls.driver.quit()
