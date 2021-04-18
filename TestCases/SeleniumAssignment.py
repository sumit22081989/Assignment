import pytest
from selenium import webdriver

from PageObjects.LoopedScript import LoppedScript
from PageObjects.BrokenLink import BrokenLinks
import PageObjects.Login
from PageObjects.Input import Input
from PageObjects.Login import Login
from TestCases import BrokenLink
from PageObjects.Sort import Sort


class Test_SeleniumAssignment:

    # a) Assert Broken images http://the-internet.herokuapp.com/broken_images
    def test_AssertBrokenImage(self, setup):
        self.driver = setup
        self.driver.get(BrokenLinks.baseURL)
        self.driver.maximize_window()
        status = BrokenLink.FindBrokenLink(self,setup)
        assert status == True, "Some images are broken"

    #c) Assert form validation functionality Post entering a dummy username and password on http://the-internet.herokuapp.com/login
    def test_Validate_Login(self,setup):
        self.driver = setup
        login = Login(setup)
        self.driver.get(login.baseURL)
        login.Login()
        status = login.Valiate_Login()
        assert status == True, "User Credentials are incorrect"


    def Validate_Input(self, setup):
        self.driver = setup
        input = Input(setup)
        self.driver.get(input.baseURL)
        self.driver.maximize_window()
        input.Enter_Input()

    ## e) Write a test to sort the table by the amount due on page http://the-internet.herokuapp.com/tables
    def Sort(self,setup):
        self.driver = setup
        sort = Sort(setup)
        self.driver.get(sort.baseURL)
        self.driver.maximize_window()
        sort.Sort()

    #f) Right a looped script to assert a 'successful notification" after repeated unsuccessful notification on page http://the-internet.herokuapp.com/notification_message_rendered
    def test_LoopWithSuccessMsg(self, setup):
        self.driver = setup
        loop = LoppedScript(setup)
        self.driver.get(loop.baseURL)
        self.driver.maximize_window()
        loop.findSuccessMsg()






