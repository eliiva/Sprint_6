import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
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

        assert self.driver.current_url == main_page_url

    @allure.title('Проверка редиректа на главную страницу Дзена')
    @allure.description('На главной странице кликаем на лого Яндекс и проверяем, что произошёл редирект на главную Дзена')
    def test_redirect_to_yandex_page(self):
        self.driver.get(main_page_url)

        main_page = MainPage(self.driver)

        main_page.wait_for_load_main_page()
        main_page.click_yandex_logo()

        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])
        WebDriverWait(self.driver, 10).until(EC.url_contains('https://dzen.ru/'))

        assert dzen_page_url in self.driver.current_url
  
    @classmethod
    def teardown_class(cls):
        with allure.step('Закрываем браузер'):
            cls.driver.quit()
    