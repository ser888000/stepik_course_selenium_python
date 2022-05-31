from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, "i.icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    TEXT_IN_LOGIN_URL = "login"
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")
    SIGN_OK = (By.CSS_SELECTOR, "i.icon-ok-sign")
    LOGIN_USERNAME = (By.CSS_SELECTOR, "[name='login-username']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "[name='login-password']")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "[name='login_submit']")

class ProductPageLocators():
    TEXT_IN_URL = "promo"
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE_IN_MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")

class BasketPageLocators():
    BASKET_TOTAL = (By.CSS_SELECTOR, ".total")
    BASKET_EMPTY = (By.CSS_SELECTOR, ".content #content_inner > p")
