import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects import SubmitHomePage
from PageObjects.SubmitHomePage import Submission
from TestData.HomepageData import HomePageData
from Utilities.BaseClass import Baseclass


class TestFormSubmission(Baseclass):
    def test_form(self,dataload):
        nameobject = Submission(self.driver)
        nameobject.entername().send_keys(dataload["Firstname"])
        nameobject.enteremail().send_keys(dataload["Email"])
        nameobject.enterpassword().send_keys(dataload["Password"])
        nameobject.checkoption().click()
        self.dropdown_text(nameobject.getgender(),dataload["Gender"])
        nameobject.submitbutton().click()
        message = nameobject.successmsg().text
        assert 'success' in message
        # nameobject.clearpage().clear()
        self.driver.refresh()

    # @pytest.fixture(params=[("Arun","vardhan@gmail.com","Male",9876543)]) #with tuples
    @pytest.fixture(params=HomePageData.test_data)
    # @pytest.fixture(params=HomePageData.get_test_data("Testcase2"))  #get data from excel
    def dataload(self,request):
        return request.param
