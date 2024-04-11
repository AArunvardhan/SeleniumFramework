#This code is for test_end3end.py file
import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

from PageObjects.SubmitHomePage import Submission


@pytest.mark.usefixtures('setup')
class Baseclass:
    def explicitwait(self,text):
        waits = WebDriverWait(self.driver, 10)
        waits.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    # #This code is for test_Homepage.py
    def dropdown_text(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)
    def getlogger(self):
        # logger = logging.getLogger(__name__)
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler = logging.FileHandler("logfile.log")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger
