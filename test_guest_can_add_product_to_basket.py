from .pages.product_page import ProductPage
import pytest
import time



link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_add_to_cart_from_product_page_with_promo(browser):
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket_with_promo()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()

#    time.sleep(0)
    
#def test_guest_can_go_to_login_page(browser):
#    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#    page.open()                      # открываем страницу
#    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
#    login_page = LoginPage(browser, browser.current_url)
#    login_page.should_be_login_page()
