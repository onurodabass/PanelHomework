from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.partner_page import PartnerPage


class LoginPage(BasePage):
    EMAIL_TEXT_BOX = (By.ID, 'email')
    PASSWORD_TEXT_BOX = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    def check_page_loaded(self):
        return True if self.find_element(*self.LOGIN_BUTTON) else False

    def fill_login_form(self, email, password):
        self.fill(email, *self.EMAIL_TEXT_BOX)
        self.fill(password, *self.PASSWORD_TEXT_BOX)

    def click_login_button(self):
        self.wait_for_element_clickable(self.LOGIN_BUTTON).click()
        return PartnerPage(self.driver)