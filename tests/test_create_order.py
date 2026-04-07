import allure
from selenium import webdriver
from datetime import date, timedelta
from pages.base_page import BasePage
from pages.order_page import OrderPage
from pages.main_page import MainPage
from locators.order_page_locators import one_day_interval, five_day_interval, black_color_checkbox, grey_color_checkbox, order_modal_header

class TestCreateOrder:

    driver = None
    main_page_url = 'https://qa-scooter.praktikum-services.ru/'
    order_page_url = 'https://qa-scooter.praktikum-services.ru/order'

    @classmethod
    def setup_class(cls):
        with allure.step('Открываем браузер Firefox'):
            cls.driver = webdriver.Firefox()

    @allure.title('Проверка создания заказа через кнопку Заказать в хэдере')
    @allure.description('Создаём заказ через кнопку Заказать в хэдере и проверяем всплывающее окно с сообщением об успехе')
    def test_create_order_by_header_order_button(self):
        order_date = (date.today() + timedelta(days=3)).strftime('%d.%m.%Y')
        test_data = {
            'firstname': 'Михаил',
            'lastname': 'Глинка',
            'address': 'Улица Мира, 15',
            'metro_station': 'Тверская',
            'phone': '89119811234',
            'date': order_date,
            'interval_locator': one_day_interval,
            'color_locator': black_color_checkbox,
            'comment': '-'
        }

        self.driver.get(self.order_page_url)

        base_page = BasePage(self.driver)

        base_page.wait_for_load_base_page()
        base_page.click_order_button()

        order_page = OrderPage(self.driver)
        order_page.wait_for_load_order_page()
        order_page.fill_customer_info(
            firstname=test_data['firstname'],
            lastname=test_data['lastname'],
            address=test_data['address'],
            metro_station=test_data['metro_station'],
            phone=test_data['phone']
        )
        order_page.click_next_button()
        order_page.fill_rent_info_block(
            date=test_data['date'],
            interval_locator=test_data['interval_locator'],
            color_locator=test_data['color_locator'],
            comment=test_data['comment']
        )
        order_page.click_complete_order_button()
        order_page.wait_for_agree_block_load()
        order_page.click_agree_button()
        order_page.wait_for_status_block_load()

        assert "Заказ оформлен" in self.driver.find_element(*order_modal_header).text

    @allure.title('Проверка создания заказа через кнопку Заказать на главной')
    @allure.description('Создаём заказ через кнопку Заказать на главной и проверяем всплывающее окно с сообщением об успехе')
    def test_create_order_by_main_page_order_button(self):
        order_date = (date.today() + timedelta(days=1)).strftime('%d.%m.%Y')
        test_data = {
            'firstname': 'Сергей',
            'lastname': 'Прокофьев',
            'address': 'Ленинский пр., д.28',
            'metro_station': 'Ленинский проспект',
            'phone': '79060067878',
            'date': order_date,
            'interval_locator': five_day_interval,
            'color_locator': grey_color_checkbox,
            'comment': 'Я буду с роялем'
        }

        self.driver.get(self.main_page_url)

        main_page = MainPage(self.driver)

        main_page.wait_for_load_main_page()
        main_page.click_order_button()

        order_page = OrderPage(self.driver)
        order_page.wait_for_load_order_page()
        order_page.fill_customer_info(
            firstname=test_data['firstname'],
            lastname=test_data['lastname'],
            address=test_data['address'],
            metro_station=test_data['metro_station'],
            phone=test_data['phone']
        )
        order_page.click_next_button()
        order_page.fill_rent_info_block(
            date=test_data['date'],
            interval_locator=test_data['interval_locator'],
            color_locator=test_data['color_locator'],
            comment=test_data['comment']
        )
        order_page.click_complete_order_button()
        order_page.wait_for_agree_block_load()
        order_page.click_agree_button()
        order_page.wait_for_status_block_load()

        assert "Заказ оформлен" in self.driver.find_element(*order_modal_header).text    
        
    @classmethod
    def teardown_class(cls):
        with allure.step('Закрываем браузер'):
            cls.driver.quit()
