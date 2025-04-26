from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    def find_element(self, locator, time=10):
        """Находит элемент на странице с заданным локатором."""
        try:
            return WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(locator),
                message=f"Can't find element by locator {locator}"
            )
        except TimeoutException:
            raise Exception(f"Element with locator {locator} was not found within {time} seconds.")

    def find_elements(self, locator, time=10):
        """Находит все элементы на странице с заданным локатором."""
        try:
            return WebDriverWait(self.driver, time).until(
                EC.presence_of_all_elements_located(locator),
                message=f"Can't find elements by locator {locator}"
            )
        except TimeoutException:
            raise Exception(f"Elements with locator {locator} were not found within {time} seconds.")

    def go_to_site(self):
        """Переходит на базовый URL сайта."""
        self.driver.get(self.base_url)

    def switch_to_new_window(self):
        """Переключается на новое окно браузера."""
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def close_current_window(self):
        """Закрывает текущее окно браузера и переключается на предыдущее."""
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[-1])