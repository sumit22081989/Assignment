from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class LoppedScript:

    baseURL = "http://the-internet.herokuapp.com/notification_message_rendered"
    link_ClickHere = "Click here"
    success_CSS = "div[id='flash']"

    def __init__(self, driver):
        self.driver = driver

    def findSuccessMsg(self):
        try:
            self.driver.find_element_by_link_text(self.link_ClickHere).click()
            successMsg = str(self.driver.find_element_by_css_selector(self.success_CSS).text)
            successMsg = successMsg.strip()
            if successMsg.__contains__("Action successful"):
                pass
            else:
                self.findSuccessMsg()
        except NoSuchElementException:
            self.findSuccessMsg()
