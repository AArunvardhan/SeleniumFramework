from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self,driver):
        self.driver = driver

    country = (By.CSS_SELECTOR, "#country")
    selectCountry = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div/label[@for='checkbox2']")
    purchase = (By.XPATH, "//input[@value='Purchase']")
    successmsg = (By.CSS_SELECTOR, ".alert-success")

    def getcountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def clickcountry(self):
        return self.driver.find_element(*ConfirmPage.selectCountry)

    def Checkbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def Purchase(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def getSuccessmsg(self):
        return self.driver.find_element(*ConfirmPage.successmsg)