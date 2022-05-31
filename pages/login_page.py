from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators 
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url() # проверка на корректный url адрес
        self.should_be_login_form() # проверка, что есть форма логина
        self.should_be_register_form() # проверка, что есть форма регистрации на странице

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert self.is_text_in_url(LoginPageLocators.TEXT_IN_LOGIN_URL), "URL in not login" 

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented" 

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented" 

    def register_new_user(self, email, password):
        # Регистрация нового пользователя
        registration_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        registration_email.send_keys(email) 
        registration_password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        registration_password1.send_keys(password) 
        registration_password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        registration_password2.send_keys(password) 
        registration_submit = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        registration_submit.click() 
        assert self.is_element_present(*LoginPageLocators.SIGN_OK), "Register is not OK" # Регистрация прошла успешно
        
    def login_user(self, email, password):
        # Авторизация пользователя
        login_username = self.browser.find_element(*LoginPageLocators.LOGIN_USERNAME)
        login_username.send_keys(email) 
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys(password) 
        login_submit = self.browser.find_element(*LoginPageLocators.LOGIN_SUBMIT)
        login_submit.click() 
