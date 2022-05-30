from selenium.webdriver.common.by import By
from .base_page import BasePage # импорт базового класса BasePage
#from .locators import MainPageLocators # класс с локаторами


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
