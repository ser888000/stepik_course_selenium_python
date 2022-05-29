from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators # класс с локаторами

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_text_in_url(LoginPageLocators.TEXT_IN_LOGIN_URL), "URL in not login" # проверку на корректный url адрес

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented" # проверку, что есть форма логина

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented" # проверку, что есть форма регистрации на странице
