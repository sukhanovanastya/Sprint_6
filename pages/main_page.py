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
        return (By.ID, f"accordion__heading-{index}")

    def get_faq_answer(self, index):
        return (By.ID, f"accordion__panel-{index}")

    def click_faq_question(self, index):
        question = self.find_element(self.get_faq_question(index))
        self.driver.execute_script("arguments[0].click();", question)

    def get_faq_answer_text(self, index):
        return self.find_element(self.get_faq_answer(index)).text

    def wait_for_faq_answer_to_appear(self, index):
        """Ожидание появления текста ответа на вопрос FAQ."""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.get_faq_answer(index))
        )

    def click_order_button_top(self):
        self.find_element(self.ORDER_BUTTON_TOP).click()

    def click_order_button_middle(self):
        self.find_element(self.ORDER_BUTTON_MIDDLE).click()

    def click_scooter_logo(self):
        self.find_element(self.SCOOTER_LOGO).click()

    def click_yandex_logo(self):
        self.find_element(self.YANDEX_LOGO).click()

    def accept_cookies(self):
        cookie_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.COOKIE_BUTTON)
        )
        cookie_btn.click()