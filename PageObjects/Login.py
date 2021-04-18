from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class Login:

    baseURL = "http://the-internet.herokuapp.com/login"
    username = "tomsmith"
    password = "SuperSecretPassword!"
    username_Locator_ID = "username"
    password_Locator_ID = "password"
    login_Locator_CSS = "button[class = 'radius']"
    success_Login_CSS = "i[class='icon-2x icon-signout']"

    def __init__(self, driver):
        self.driver = driver

    def Login(self):
        ele_Username = self.driver.find_element_by_id(self.username_Locator_ID)
        ele_Password = self.driver.find_element_by_id(self.password_Locator_ID)
        ele_Username.send_keys(self.username)
        ele_Password.send_keys(self.password)
        self.driver.find_element_by_css_selector(self.login_Locator_CSS).click()

    def Valiate_Login(self):
        try:
            self.driver.find_element_by_css_selector(self.success_Login_CSS)
            return True
        except NoSuchElementException:
            return False



