from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import order_header, firstname_input, lastname_input, address_input, metro_station_input, metro_station_value, phone_input, next_button, date_input, date_selected, time_interval_block, time_interval_list, comment_input, complete_order_button, agree_button, check_status_button
import allure

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Дожидаемся загрузки страницы')
    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(order_header))

    @allure.step('Указываем имя')
    def fill_firstname_input(self, firstname):
        self.driver.find_element(*firstname_input).send_keys(firstname)

    @allure.step('Указываем фамилию')
    def fill_lasttname_input(self, lastname):
        self.driver.find_element(*lastname_input).send_keys(lastname)

    @allure.step('Указываем адрес')
    def fill_address_input(self, address):
        self.driver.find_element(*address_input).send_keys(address)

    @allure.step('Указываем станцию метро')
    def fill_metro_station_input(self, metro_station):
        self.driver.find_element(*metro_station_input).send_keys(metro_station)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(metro_station_value))
        self.driver.find_element(*metro_station_value).click()

    @allure.step('Указываем телефон')
    def fill_phone_input(self, phone):
        self.driver.find_element(*phone_input).send_keys(phone)

    @allure.step('Заполняем раздел Для кого самокат')
    def fill_customer_info(self, firstname, lastname, address, metro_station, phone):
        self.fill_firstname_input(firstname)
        self.fill_lasttname_input(lastname)
        self.fill_address_input(address)
        self.fill_metro_station_input(metro_station)
        self.fill_phone_input(phone)

    @allure.step('Нажимаем кнопку Далее')
    def click_next_button(self):
        self.driver.find_element(*next_button).click()

    @allure.step('Дожидаемся отображения раздела Про аренду')
    def wait_for_load_rent_info_block(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(complete_order_button))

    @allure.step('Указываем дату')
    def fill_date_input(self, date):
        self.driver.find_element(*date_input).send_keys(date)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(date_selected))
        self.driver.find_element(*date_selected).click()

    @allure.step('Указываем срок аренды')
    def select_time_interval(self, interval_locator):
        self.driver.find_element(*time_interval_block).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(time_interval_list))
        self.driver.find_element(*interval_locator).click()

    @allure.step('Выбираем цвет самоката')
    def select_scooter_color(self, color_locator):
        self.driver.find_element(*color_locator).click()

    @allure.step('Заполняем комментарий для курьера')
    def fill_comment_input(self, comment):
        self.driver.find_element(*comment_input).send_keys(comment)

    @allure.step('Заполняем раздел Про аренду')
    def fill_rent_info_block(self, date, interval_locator, color_locator, comment):
        self.fill_date_input(date)
        self.select_time_interval(interval_locator)
        self.select_scooter_color(color_locator)
        self.fill_comment_input(comment)

    @allure.step('Нажимаем кнопку Заказать')
    def click_complete_order_button(self):
        self.driver.find_element(*complete_order_button).click()

    @allure.step('Дожидаемся отображения модального окна для подтверждения')
    def wait_for_agree_block_load(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(agree_button))

    @allure.step('Нажимаем кнопку Подтверждения заказа')
    def click_agree_button(self):
        self.driver.find_element(*agree_button).click()

    @allure.step('Дожидаемся отображения модального окна Заказ оформлен')
    def wait_for_status_block_load(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(check_status_button))
    