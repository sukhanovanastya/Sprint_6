import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage

ORDER_DATA = {
    "first_name": "Иван",
    "last_name": "Иванов",
    "address": "Москва, ул. Пушкина, д. 1",
    "phone": "89991234567"
}

@allure.feature("Order Flow")
@allure.story("Create new order")
class TestOrderFlow:

    @pytest.fixture(scope="function", autouse=True)
    def setup_method(self):
        """Инициализация драйвера перед каждым тестом."""
        self.driver = webdriver.Firefox()
        yield
        self.driver.quit()

    @allure.title("Тест на оформление нового заказа")
    def test_order_flow(self):
        """Основной метод тестирования потока оформления заказа."""
        main_page = MainPage(self.driver)
        order_page = OrderPage(self.driver)

        with allure.step("Open main page"):
            main_page.go_to_site()

        with allure.step("Accept cookies"):
            main_page.accept_cookies()

        with allure.step("Click order button"):
            main_page.click_order_button_top()

        with allure.step("Fill in personal data"):
            order_page.fill_personal_data(
                ORDER_DATA["first_name"],
                ORDER_DATA["last_name"],
                ORDER_DATA["address"],
                ORDER_DATA["phone"]
            )

        with allure.step("Select metro station"):
            order_page.select_station(0)

        with allure.step("Select delivery date"):
            order_page.select_delivery_date()

        with allure.step("Select scooter color"):
            order_page.select_scooter_color()

        with allure.step("Fill courier comment"):
            order_page.fill_courier_comment("Оставить у двери")

        with allure.step("Submit the order"):
            order_page.submit_order()

        with allure.step("Check success modal is displayed"):
            assert order_page.is_success_modal_displayed(), "Success modal is not displayed"