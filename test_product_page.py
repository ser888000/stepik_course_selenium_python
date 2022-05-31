from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.login
class TestLoginFromProductPage(): # Класс для логина со страницы товара
    def test_guest_should_see_login_link_on_product_page(self, browser):
        # Проверка наличия ссылки на страницу авторизации
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open() # in BasePage
        page.should_be_login_link() # in BasePage

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        # Переход на страницу авторизации и проверка полей на LoginPage
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open() # in BasePage
        page.go_to_login_page()  # in BasePage     
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()    # in LoginPage

@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage():
    # Добавление товара в корзину зарегистрирвоанным пользователем
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Функция запускается перед выполнением каждого теста в классе, и если надо, то после (здесь не реализовано)
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open() # in BasePage
        page.register_new_user(str(time.time()) + "@fakemail.org", 'asdfKH76.') # in LoginPage
        page.should_be_authorized_user()  # in BasePage

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # Добавление зарегистрированным пользователем товара в корзину
        page = ProductPage(browser, link)
        page.open() # in BasePage
        # in ProductPage
        page.press_button_add_product_to_basket() # Добавить товар в корзину
        page.should_be_message_about_adding() # Проверить что товар добавлен
        page.should_be_message_basket_total() # Прверить что сумма корзины совпадает с ценой товара

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

    

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", 
                                    marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_add_to_cart_from_product_page_with_promo(browser, link):
    # Добавление промо товара в корзину с вычислением каптчи
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_product_to_basket_with_promo()
    page.solve_quiz_and_get_code() # вычислить каптчу
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    # добавление товара в корзину гостем
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_product_to_basket()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket_with_promo()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket_with_promo()
    page.solve_quiz_and_get_code()
    page.should_be_success_message_disappeared() # Проверяем, что нет сообщения об успехе с помощью is_disappeared
   
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # переход на страницу корзины + проверка на ее пустоту
    page = ProductPage(browser, link)   
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_empty()    
    basket_page.should_be_text_basket_empty()

