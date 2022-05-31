from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, browser):
        # на странице есть ссылка на логин
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
    
    def test_guest_can_go_to_login_page(self, browser):
        # переход на страницу с логином
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # переход на страницу корзины + проверка на ее пустоту
    page = MainPage(browser, link)   
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_empty()    
    basket_page.should_be_text_basket_empty()