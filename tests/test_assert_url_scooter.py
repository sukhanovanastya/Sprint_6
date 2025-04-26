import allure
from pages.main_page import MainPage
@allure.feature("Main Page Navigation")
@allure.story("Click on Scooter logo")
class TestMainPageNavigation:

    @allure.title("Тест на нажатие на логотип 'Самокат'")
    def test_click_scooter_logo(self, driver):
        """Тест на нажатие на логотип 'Самокат' и проверку URL."""

        driver.get("https://qa-scooter.praktikum-services.ru")
        main_page = MainPage(driver)

        with allure.step("Click on the Scooter logo"):
            main_page.click_scooter_logo()

        with allure.step("Verify that the URL is correct"):
            current_url = driver.current_url
            expected_url = "https://qa-scooter.praktikum-services.ru/"
            assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"