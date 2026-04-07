import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage

class TestRedirect:

    driver = None
    main_page_url = 'https://qa-scooter.praktikum-services.ru/'
    order_page_url = 'https://qa-scooter.praktikum-services.ru/order'
    dzen_page_url = 'https://dzen.ru/?yredirect=true'

    @classmethod
    def setup_class(cls):
        with allure.step('Открываем браузер Firefox'):
            cls.driver = webdriver.Firefox()

    @allure.title('Проверка редиректа на главную страницу Самоката')
    @allure.description('На странице заказа кликаем на лого Самокат и проверяем, что произошёл редирект на главную Самоката')
    def test_redirect_to_main_page(self):
        self.driver.get(self.order_page_url)

        base_page = BasePage(self.driver)

        base_page.wait_for_load_base_page()
        base_page.click_samokat_logo()

        assert self.driver.current_url == self.main_page_url

    @allure.title('Проверка редиректа на главную страницу Дзена')
    @allure.description('На главной странице кликаем на лого Яндекс и проверяем, что произошёл редирект на главную Дзена')
    def test_redirect_to_yandex_page(self):
        self.driver.get(self.main_page_url)

        base_page = BasePage(self.driver)

        base_page.wait_for_load_base_page()
        base_page.click_yandex_logo()

        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])
        WebDriverWait(self.driver, 10).until(EC.url_contains('https://dzen.ru/'))

        assert self.dzen_page_url in self.driver.current_url
  
    @classmethod
    def teardown_class(cls):
        with allure.step('Закрываем браузер'):
            cls.driver.quit()
    