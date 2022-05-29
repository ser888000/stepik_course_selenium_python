from selenium.webdriver.common.by import By
from .base_page import BasePage # импорт базового класса BasePage

class MainPage(BasePage): # наследник класса BasePage
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click() 

