import allure
from pages.main_page import MainPage

@allure.feature("Main Page Navigation")
@allure.story("Click on Yandex logo and verify new tab")
class TestYandexLogoNavigation:

    @allure.title("Тест на нажатие на логотип 'Яндекс'")
    def test_click_yandex_logo(self, driver):
        """Тест на нажатие на логотип 'Яндекс' и проверку URL новой вкладки."""

        driver.get("https://qa-scooter.praktikum-services.ru")
        main_page = MainPage(driver)

        with allure.step("Click on the Yandex logo"):
            main_page.click_yandex_logo()
            main_page.switch_to_new_window()

        with allure.step("Verify that the URL is correct"):
            current_url = main_page.get_current_url()
            expected_url = "https://dzen.ru/?yredirect=true"
            assert current_url == expected_url, f"Expected URL: {expected_url}, but got: {current_url}"