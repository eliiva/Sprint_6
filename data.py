from locators.main_page_locators import price_question_block, price_answer_block, several_scooters_question_block, several_scooters_answer_block, time_calc_question_block, time_calc_answer_block, today_order_question_block, today_order_answer_block, change_time_question_block, change_time_answer_block, charging_question_block, charging_answer_block, cancel_order_question_block, cancel_order_answer_block, place_question_block, place_answer_block
from locators.order_page_locators import one_day_interval, five_day_interval, black_color_checkbox, grey_color_checkbox
from datetime import date, timedelta

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

first_order_data = {
    'firstname': 'Михаил',
    'lastname': 'Глинка',
    'address': 'Улица Мира, 15',
    'metro_station': 'Тверская',
    'phone': '89119811234',
    'date': (date.today() + timedelta(days=3)).strftime('%d.%m.%Y'),
    'interval_locator': one_day_interval,
    'color_locator': black_color_checkbox,
    'comment': '-'
}

second_order_data = {
    'firstname': 'Сергей',
    'lastname': 'Прокофьев',
    'address': 'Ленинский пр., д.28',
    'metro_station': 'Ленинский проспект',
    'phone': '79060067878',
    'date': (date.today() + timedelta(days=1)).strftime('%d.%m.%Y'),
    'interval_locator': five_day_interval,
    'color_locator': grey_color_checkbox,
    'comment': 'Я буду с роялем'
}
