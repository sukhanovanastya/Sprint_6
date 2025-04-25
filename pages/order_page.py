from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class OrderPage(BasePage):
    # Локаторы для формы заказа
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_OPTIONS = (By.CSS_SELECTOR, "div.select-search__select button")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Локаторы для второй страницы заказа
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    CALENDAR_MONTH = (By.CLASS_NAME, "react-datepicker__month-select")
    CALENDAR_YEAR = (By.CLASS_NAME, "react-datepicker__year-select")
    CALENDAR_DAY = (By.CSS_SELECTOR, ".react-datepicker__day:not(.react-datepicker__day--outside-month)")
    BLACK_COLOR_CHECKBOX = (By.ID, "black")
    GREY_COLOR_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Заказать')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")

    def fill_personal_data(self, first_name, last_name, address, phone):
        """Заполнение личных данных пользователя."""
        self.find_element(self.FIRST_NAME_INPUT).send_keys(first_name)
        self.find_element(self.LAST_NAME_INPUT).send_keys(last_name)
        self.find_element(self.ADDRESS_INPUT).send_keys(address)
        self.find_element(self.PHONE_INPUT).send_keys(phone)

        next_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.NEXT_BUTTON)
        )
        next_button.click()

    def select_station(self, index):
        """Выбор станции метро по индексу."""
        self.find_element(self.METRO_STATION_INPUT).click()
        stations = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.METRO_STATION_OPTIONS)
        )
        if len(stations) > index:
            stations[index].click()

    def select_delivery_date(self):
        """Выбор даты доставки из календаря."""
        self.find_element(self.DELIVERY_DATE_INPUT).click()

        weekday_name = "среда"
        day = 23
        month_name = "апреля"
        year = 2025

        xpath_day = f"//div[@aria-label='Choose {weekday_name}, {day}-е {month_name} {year} г.']"

        selected_day_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_day))
        )

        selected_day_element.click()

    def select_scooter_color(self):
        """Выбор цвета самоката."""
        self.find_element(self.BLACK_COLOR_CHECKBOX).click()
    def fill_courier_comment(self, comment):
        """Заполнение комментария для курьера."""
        self.find_element(self.COMMENT_INPUT).send_keys(comment)

    def submit_order(self):
        """Отправка заказа."""
        self.find_element(self.ORDER_BUTTON).click()

        confirm_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONFIRM_BUTTON)
        )

        confirm_button.click()

    def is_success_modal_displayed(self):
        """Проверка отображения модального окна успешного завершения заказа."""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((self.SUCCESS_MODAL))
        ).is_displayed()