from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
import pytest
import time



#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"

@pytest.mark.login
class TestLoginFromProductPage():
    '''
    Эти функции называются setup — функция, которая выполнится перед запуском каждого теста из класса, 
    обычно туда входит подготовка данных, и teardown — функция, которая выполняется ПОСЛЕ каждого теста из класса, 
    обычно там происходит удаление тех данных, которые мы создали во время теста. 
    Хороший автотест должен сработать даже на чистой базе данных и удалить за собой сгенерированные в тесте данные. 
    акие функции реализуются с помощью фикстур, которые мы изучили в предыдущем модуле. 
    Чтобы функция запускалась автоматически перед каждым тест-кейсом, 
    нужно пометить её как @pytest.fixture с параметрами scope="function", 
    что значит запускать на каждую функцию, и autouse=True, что значит запускать автоматически без явного вызова фикстуры.
    '''
    '''
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        #
        self.product = ProductFactory(title = "Best book created by robot")
        # создаем по апи
        self.link = self.product.link
        yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали 
        self.product.delete()
    '''
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()        

@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(str(time.time()) + "@fakemail.org", 'asdfKH76.')
        main_page = BasePage(browser, browser.current_url)
        main_page.should_be_authorized_user()  

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.press_button_add_product_to_basket()
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()


    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
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

@pytest.mark.skip
def test_add_to_cart_from_product_page_with_promo(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_product_to_basket_with_promo()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()

@pytest.mark.skip
def test_add_to_cart_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_product_to_basket()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()

#    time.sleep(20)

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket_with_promo()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket_with_promo()
    page.solve_quiz_and_get_code()
    page.should_be_success_message_disappeared() # Проверяем, что нет сообщения об успехе с помощью is_disappeared
   
@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # переход на страницу корзины + проверка на ее пустоту
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_empty()    
    basket_page.should_be_text_basket_empty()

