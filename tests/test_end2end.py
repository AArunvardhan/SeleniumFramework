from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects import Confirmpage
from PageObjects.Confirmpage import ConfirmPage
from Utilities.BaseClass import Baseclass
from PageObjects.Homepage import Homepage
from PageObjects.checkoutpage import CheckOutPage



class TestExample(Baseclass):
    def test_e2e(self):
        log = self.getlogger()
        # self.driver.find_element(By.XPATH, "//a[text()='Shop']").click()
        homepage = Homepage(self.driver)
        homepage.shopItems().click()

        # options = self.driver.find_elements(By.CSS_SELECTOR, ".col-lg-3.col-md-6.mb-3")
        checkoutpage = CheckOutPage(self.driver)
        options = checkoutpage.getCardTitles()
        log.info("Getting all mobile options")
        for option in options:
            if checkoutpage.getProductName().text == 'Samsung Note 8':
                checkoutpage.clickbutton().click()
        log.info(options)
        log.info("Selecting the required mobile phone")
        # self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        checkoutpage.checkout().click()
        # self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
        checkoutpage.successButton().click()
        # self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys('In')
        confirmpage = ConfirmPage(self.driver)
        confirmpage.getcountry().send_keys('In')
        log.info("entering the country by sending 'In'")
        # waits = WebDriverWait(self.driver, 10)
        # waits.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.explicitwait('India')
        # self.driver.find_element(By.LINK_TEXT, "India").click()
        confirmpage.clickcountry().click()

        # self.driver.find_element(By.XPATH, "//div/label[@for='checkbox2']").click()
        confirmpage.Checkbox().click()

        # self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
        confirmpage.Purchase().click()
        log.info("Placing the order")

        assert "Success" in confirmpage.getSuccessmsg().text

