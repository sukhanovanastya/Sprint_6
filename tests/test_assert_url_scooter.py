import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.feature("Main Page Navigation")
@allure.story("Click on Scooter logo")
class TestMainPageNavigation:

    def setup_method(self):
        """Инициализация драйвера перед каждым тестом."""
        self.driver = webdriver.Firefox()
        self.driver.get("https://qa-scooter.praktikum-services.ru")

    def teardown_method(self):
        """Закрытие драйвера после каждого теста."""
        self.driver.quit()

    def test_click_scooter_logo(self):
        """Тест на нажатие на логотип 'Самокат' и проверку URL."""

        with allure.step("Click on the Scooter logo"):
            logo = self.driver.find_element(By.XPATH, "//img[@alt='Scooter'][1]")
            logo.click()

        with allure.step("Verify that the URL is correct"):
            current_url = self.driver.current_url
            expected_url = "https://qa-scooter.praktikum-services.ru/"
            assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"
