from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip

class Input:
    baseURL = "http://the-internet.herokuapp.com/inputs"
    input_Field_CSS = "input[type = 'number']"
    enter_Input = "123absj"


    def __init__(self, driver):
        self.driver = driver

    def Enter_Input(self):
        ele = self.driver.find_element_by_css_selector(self.input_Field_CSS)
        ele.send_keys(self.enter_Input)
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('A').perform()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys(Keys.INSERT).perform()
        copiedString = pyperclip.paste()
        if self.enter_Input == copiedString:
            return True
        else:
            return False


