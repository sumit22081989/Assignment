from selenium import webdriver

class Sort:

    baseURL = "http://the-internet.herokuapp.com/tables"
    sort_Table1 = "//*[@id='table1']/thead/tr/th[2]/span"
    sort_Table2 = "//*[@id='table2']/thead/tr/th[2]/span"

    def __init__(self, driver):
        self.driver = driver

    def Sort(self):
        self.driver.find_element_by_xpath(self.sort_Table1).click()
        self.driver.find_element_by_xpath(self.sort_Table2).click()