from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, f"expected 'login' to be substring of URL '{self.browser.current_url}'"        

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is absent"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is absent"

    def register_new_user(self, email, password):
        registration_email = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-email")
        registration_password = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password1")
        registration_password_confirm = self.browser.find_element(By.CSS_SELECTOR, "#id_registration-password2")
        registration_button = self.browser.find_element(By.CSS_SELECTOR, "#register_form > button")
        registration_email.send_keys(email)
        registration_password.send_keys(password)
        registration_password_confirm.send_keys(password)
        registration_button.click()


