from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    @allure.step('Получаем текст элемента')
    def get_element_text(self, element_locator):
        return self.driver.find_element(*element_locator).text
    
    @allure.step('Получаем текущий урл страницы')
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Переключаемся на новую вкладку')
    def switch_to_new_tab(self, new_tab_url):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])
        WebDriverWait(self.driver, 10).until(EC.url_contains(new_tab_url))
