from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def register_new_user(self):
        number = str(time.time())
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(str(number)  + "@fakemail.org")
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1).send_keys(str(number))
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2).send_keys(str(number))
        self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT).click()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, \
            "URL is not correct"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"

