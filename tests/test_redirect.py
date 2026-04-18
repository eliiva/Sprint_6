import allure
from selenium import webdriver
from pages.order_page import OrderPage
from pages.main_page import MainPage
from urls import main_page_url, order_page_url, dzen_page_url

class TestRedirect:

    driver = None

    @classmethod
    def setup_class(cls):
        with allure.step('Открываем браузер Firefox'):
            cls.driver = webdriver.Firefox()

    @allure.title('Проверка редиректа на главную страницу Самоката')
    @allure.description('На странице заказа кликаем на лого Самокат и проверяем, что произошёл редирект на главную Самоката')
    def test_redirect_to_main_page(self):
        self.driver.get(order_page_url)

        order_page = OrderPage(self.driver)

        order_page.wait_for_load_order_page()
        order_page.click_samokat_logo()

        assert order_page.get_current_url() == main_page_url

    @allure.title('Проверка редиректа на главную страницу Дзена')
    @allure.description('На главной странице кликаем на лого Яндекс и проверяем, что произошёл редирект на главную Дзена')
    def test_redirect_to_yandex_page(self):
        self.driver.get(main_page_url)

        main_page = MainPage(self.driver)

        main_page.wait_for_load_main_page()
        main_page.click_yandex_logo()
        main_page.switch_to_new_tab('https://dzen.ru/')

        assert  main_page.get_current_url() == dzen_page_url
  
    @classmethod
    def teardown_class(cls):
        with allure.step('Закрываем браузер'):
            cls.driver.quit()
    