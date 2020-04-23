from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators
from .locators import BasketPageLocators
import time

class BasketPage(BasePage):
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT_FROM_START_PAGE), "Basket contains items, but should be empty"

    def should_not_be_success_item_message(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT_FROM_ITEM_PAGE), "Basket contains items, but should be empty"

    def should_be_empty_message(self, language):
        languages = {
            "ar": "سلة التسوق فارغة",
            "ca": "La seva cistella està buida.",
            "cs": "Váš košík je prázdný.",
            "da": "Din indkøbskurv er tom.",
            "de": "Ihr Warenkorb ist leer.",
            "en": "Your basket is empty.",
            "el": "Το καλάθι σας είναι άδειο.",
            "es": "Tu carrito esta vacío.",
            "fi": "Korisi on tyhjä",
            "fr": "Votre panier est vide.",
            "it": "Il tuo carrello è vuoto.",
            "ko": "장바구니가 비었습니다.",
            "nl": "Je winkelmand is leeg",
            "pl": "Twój koszyk jest pusty.",
            "pt": "O carrinho está vazio.",
            "pt-br": "Sua cesta está vazia.",
            "ro": "Cosul tau este gol.",
            "ru": "Ваша корзина пуста",
            "sk": "Váš košík je prázdny",
            "uk": "Ваш кошик пустий.",
            "zh-cn": "Your basket is empty.",
            "en-US": "Your basket is empty.",
        }
        assert languages[language] in self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text, f"'{languages[language]}' should be substring of '{self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text}'"



