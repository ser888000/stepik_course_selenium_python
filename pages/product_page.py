from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def press_button_add_product_to_basket_with_promo(self):
        # проверка на корректный url адрес
        self.should_be_promo_in_url()
        # нажать кнопку добавления товара в корзину
        self.press_button_add_product_to_basket() 

    def should_be_promo_in_url(self):
        # проверка, что в url адресе есть слово promo
        assert self.is_text_in_url(ProductPageLocators.TEXT_IN_URL), "URL in not promo" 

    def press_button_add_product_to_basket(self):
        # проверка, что есть кнопка добавления в корзину
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button add to basket is not presented" 
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click() 

    def should_be_message_about_adding(self):
        # Проверка, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), ("Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE_ABOUT_ADDING), ("Message about adding is not presented")
        # получить текст элементов для проверки
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE_ABOUT_ADDING).text
        # проверка, что название товара присутствует в сообщении о добавлении
        assert product_name == message, "The name of the product in the message does not match the name of the product"

    def should_be_message_basket_total(self):
        # проверка, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE_BASKET_TOTAL), ("Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), ("Product price is not presented")
        # получить текст элементов для проверки
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message_basket_total = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE_BASKET_TOTAL).text
        # проверка, что цена товара присутствует в сообщении со стоимостью корзины
        assert product_price == message_basket_total, "The cost of the basket does not match the price of the product"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message has disappeared, but should have disappeared"








