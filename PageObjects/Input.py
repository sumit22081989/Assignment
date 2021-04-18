from selenium import webdriver

class Input:
    baseURL = "http://the-internet.herokuapp.com/inputs"
    input_Field_CSS = "input[type = 'number']"
    enter_Input = "123"


    def __init__(self, driver):
        self.driver = driver

    def Enter_Input(self):
        self.driver.find_element_by_css_selector(self.input_Field_CSS).send_keys(self.enter_Input)

