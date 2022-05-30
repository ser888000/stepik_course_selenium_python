from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        # Проверка, в корзине отсутствует элемент с классом total
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TOTAL), ("there is a product in the basket, and the basket should be empty")

    def should_be_text_basket_empty(self):
        # Проверка, есть сообщение, что корзина пуста
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), ("the basket is not empty, not message 'Ваша корзина пуста'")
