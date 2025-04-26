from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class MainPage(BasePage):
    FAQ_SECTION = (By.XPATH, "//div[contains(text(), 'Вопросы о важном')]")
    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BUTTON_MIDDLE = (By.CLASS_NAME, "Button_UltraBig__UU3Lp")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    def get_faq_question(self, index):
        """Возвращает локатор для вопроса FAQ по индексу."""
        return (By.ID, f"accordion__heading-{index}")

    def get_faq_answer(self, index):
        """Возвращает локатор для ответа FAQ по индексу."""
        return (By.ID, f"accordion__panel-{index}")

    def click_faq_question(self, index):
        """Кликает на вопрос FAQ по индексу."""
        question = self.find_element(self.get_faq_question(index))
        self.driver.execute_script("arguments[0].click();", question)

    def get_faq_answer_text(self, index):
        """Возвращает текст ответа на вопрос FAQ по индексу."""
        return self.find_element(self.get_faq_answer(index)).text

    def wait_for_faq_answer_to_appear(self, index):
        """Ожидание появления текста ответа на вопрос FAQ."""
        self.find_element(self.get_faq_answer(index), time=10)

    def click_order_button_top(self):
        """Кликает на верхнюю кнопку заказа."""
        self.find_element(self.ORDER_BUTTON_TOP).click()

    def click_order_button_middle(self):
        """Кликает на среднюю кнопку заказа."""
        self.find_element(self.ORDER_BUTTON_MIDDLE).click()

    def click_scooter_logo(self):
        """Кликает на логотип самоката."""
        self.find_element(self.SCOOTER_LOGO).click()

    def click_yandex_logo(self):
        """Кликает на логотип Яндекса и переключается на новую вкладку."""
        self.find_element(self.YANDEX_LOGO).click()

        def switch_to_new_window(self):
            """Переключается на новую вкладку."""
            current_window = self.driver.current_window_handle
            WebDriverWait(self.driver, 10).until(EC.new_window_is_opened([current_window]))

            new_window = [window for window in self.driver.window_handles if window != current_window][0]
            self.driver.switch_to.window(new_window)

    def accept_cookies(self):
        """Принимает куки через кнопку согласия."""
        cookie_btn = self.find_element(self.COOKIE_BUTTON)
        cookie_btn.click()

    def get_current_url(self):
        """Возвращает текущий URL страницы."""
        return self.driver.current_url