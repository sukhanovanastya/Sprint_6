import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@allure.feature("Main Page Navigation")
@allure.story("Click on Yandex logo and verify new tab")
class TestYandexLogoNavigation:

    def setup_method(self):
        """Инициализация драйвера перед каждым тестом."""
        self.driver = webdriver.Firefox()
        self.driver.get("https://qa-scooter.praktikum-services.ru")

    def teardown_method(self):
        """Закрытие драйвера после каждого теста."""
        self.driver.quit()

    def test_click_yandex_logo(self):
        """Тест на нажатие на логотип 'Яндекс' и проверку URL новой вкладки."""

        with allure.step("Click on the Yandex logo"):
            yandex_logo = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//img[@alt='Yandex'][1]"))
            )
            yandex_logo.click()

            current_window = self.driver.current_window_handle

            WebDriverWait(self.driver, 10).until(EC.new_window_is_opened([current_window]))

            new_window = [window for window in self.driver.window_handles if window != current_window][0]
            self.driver.switch_to.window(new_window)

            time.sleep(2)

        with allure.step("Verify that the URL is correct"):
            current_url = self.driver.current_url
            expected_url = "https://dzen.ru/?yredirect=true"
            assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"
