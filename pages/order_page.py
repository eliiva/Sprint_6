from locators.order_page_locators import order_header, samokat_logo, firstname_input, lastname_input, address_input, metro_station_input, metro_station_value, phone_input, next_button, date_input, date_selected, time_interval_block, time_interval_list, comment_input, complete_order_button, agree_button, check_status_button
import allure
from pages.base_page import BasePage

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Дожидаемся загрузки страницы')
    def wait_for_load_order_page(self):
        super().wait_for_load_element(order_header)

    @allure.step('Кликаем на логотим Самоката')
    def click_samokat_logo(self):
        super().click_page_element(samokat_logo)

    @allure.step('Указываем имя')
    def fill_firstname_input(self, firstname):
        super().fill_input(firstname_input, firstname)

    @allure.step('Указываем фамилию')
    def fill_lasttname_input(self, lastname):
        super().fill_input(lastname_input, lastname)

    @allure.step('Указываем адрес')
    def fill_address_input(self, address):
        super().fill_input(address_input, address)

    @allure.step('Указываем станцию метро')
    def fill_metro_station_input(self, metro_station):
        super().fill_input(metro_station_input, metro_station)
        super().wait_for_load_element(metro_station_value)
        super().click_page_element(metro_station_value)

    @allure.step('Указываем телефон')
    def fill_phone_input(self, phone):
        super().fill_input(phone_input, phone)

    @allure.step('Заполняем раздел Для кого самокат')
    def fill_customer_info(self, firstname, lastname, address, metro_station, phone):
        self.fill_firstname_input(firstname)
        self.fill_lasttname_input(lastname)
        self.fill_address_input(address)
        self.fill_metro_station_input(metro_station)
        self.fill_phone_input(phone)

    @allure.step('Нажимаем кнопку Далее')
    def click_next_button(self):
        super().click_page_element(next_button)

    @allure.step('Дожидаемся отображения раздела Про аренду')
    def wait_for_load_rent_info_block(self):
        super().wait_for_load_element(complete_order_button)

    @allure.step('Указываем дату')
    def fill_date_input(self, date):
        super().fill_input(date_input, date)
        super().wait_for_load_element(date_selected)
        super().click_page_element(date_selected)

    @allure.step('Указываем срок аренды')
    def select_time_interval(self, interval_locator):
        super().click_page_element(time_interval_block)
        super().wait_for_load_element(time_interval_list)
        super().click_page_element(interval_locator)

    @allure.step('Выбираем цвет самоката')
    def select_scooter_color(self, color_locator):
        super().click_page_element(color_locator)

    @allure.step('Заполняем комментарий для курьера')
    def fill_comment_input(self, comment):
        super().fill_input(comment_input, comment)

    @allure.step('Заполняем раздел Про аренду')
    def fill_rent_info_block(self, date, interval_locator, color_locator, comment):
        self.fill_date_input(date)
        self.select_time_interval(interval_locator)
        self.select_scooter_color(color_locator)
        self.fill_comment_input(comment)

    @allure.step('Нажимаем кнопку Заказать')
    def click_complete_order_button(self):
        super().click_page_element(complete_order_button)

    @allure.step('Дожидаемся отображения модального окна для подтверждения')
    def wait_for_agree_block_load(self):
        super().wait_for_load_element(agree_button)

    @allure.step('Нажимаем кнопку Подтверждения заказа')
    def click_agree_button(self):
        super().click_page_element(agree_button)

    @allure.step('Дожидаемся отображения модального окна Заказ оформлен')
    def wait_for_status_block_load(self):
        super().wait_for_load_element(check_status_button)
    