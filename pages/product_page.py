from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def add_to_basket(self):
        self.name_before = self.browser.find_element(*ProductPageLocators.NAME_BEFORE).text
        self.price_before = self.browser.find_element(*ProductPageLocators.PRICE_BEFORE).text
        print(self.price_before)
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
        self.name_after = self.browser.find_element(*ProductPageLocators.NAME_AFTER).text
        self.price_after = self.browser.find_element(*ProductPageLocators.PRICE_AFTER).text
        self.should_be_correct_name()
        self.should_be_correct_price()

    def add_to_basket_no_promo(self):
        self.name_before = self.browser.find_element(*ProductPageLocators.NAME_BEFORE).text
        self.price_before = self.browser.find_element(*ProductPageLocators.PRICE_BEFORE).text
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
        self.name_after = self.browser.find_element(*ProductPageLocators.NAME_AFTER).text
        self.price_after = self.browser.find_element(*ProductPageLocators.PRICE_AFTER).text
        self.should_be_correct_name()
        self.should_be_correct_price()

    def should_be_correct_name(self):
        # реализуйте проверку на совпадение имени
        assert self.name_before == self.name_after, f"Name mismatch, before operation the itne's name was '{self.name_before}', after add operation is '{self.name_after}'"

    def should_be_correct_price(self):
        # реализуйте проверку совпадения цены
        assert self.price_before == self.price_after, f"Price mismatch, item price was '{self.price_before}', but after add operation basket the price is '{self.price_after}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"