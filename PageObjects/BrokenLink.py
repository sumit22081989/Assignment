from selenium import webdriver

class BrokenLinks:

    imageLink = "img"
    baseURL = "http://the-internet.herokuapp.com/broken_images"

    def __init__(self, driver):
        self.driver = driver

    def getImages(self):
        elements = self.driver.find_elements_by_tag_name(self.imageLink)
        listOfLinks = ([i.get_attribute("src") for i in elements])
        return listOfLinks