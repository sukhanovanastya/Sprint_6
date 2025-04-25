import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage


@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации и закрытия драйвера."""
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@allure.feature("Main Page Navigation")
@allure.story("Click on Yandex logo and verify new tab")
class TestYandexLogoNavigation:

    @allure.title("Тест на нажатие на логотип 'Яндекс'")
    def test_click_yandex_logo(self, driver):
        """Тест на нажатие на логотип 'Яндекс' и проверку URL новой вкладки."""

        driver.get("https://qa-scooter.praktikum-services.ru")
        main_page = MainPage(driver)

        with allure.step("Click on the Yandex logo"):
            yandex_logo = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(main_page.YANDEX_LOGO)
            )
            yandex_logo.click()

            current_window = driver.current_window_handle

            WebDriverWait(driver, 10).until(EC.new_window_is_opened([current_window]))

            new_window = [window for window in driver.window_handles if window != current_window][0]
            driver.switch_to.window(new_window)

        with allure.step("Verify that the URL is correct"):
            current_url = driver.current_url
            expected_url = "https://dzen.ru/?yredirect=true"
            assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"